import subprocess
import os

def convertmp2_and_parse(filename):
    # pass a mp2
    output_filename = os.path.splitext(filename)[0] + '.mp2'
    convert_command = ['ffmpeg', '-i', filename, output_filename]
    subprocess.run(convert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Parse
    info_command = ['ffmpeg', '-i', output_filename]
    process = subprocess.Popen(info_command, stderr=subprocess.PIPE, universal_newlines=True)

    with open('video_info.txt', 'w') as info_file:
        for line in process.stderr:
            info_file.write(line)

file_name = 'BigBuckBunny_512kb.mp4'
convertmp2_and_parse(file_name)

