import subprocess
import json


def get_video_info(filename):
    command = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
               'stream=width,height,duration,codec_name,bit_rate', '-of', 'json', filename]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        video_info = json.loads(result.stdout)

        if 'streams' in video_info and len(video_info['streams']) > 0:
            stream = video_info['streams'][0]
            print(f"Video Width: {stream['width']} pixels")
            print(f"Video Height: {stream['height']} pixels")
            print(f"Duration: {stream['duration']} seconds")
            print(f"Video Codec: {stream['codec_name']}")
            print(f"Bitrate: {int(stream['bit_rate']) / 1000} kbps")
        else:
            print("No video streams found in the file.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


file_name = 'BigBuckBunny_512kb.mp4'
get_video_info(file_name)


#he fet un exemple a terminal i el resultat és
    #Video Width: 416 pixels
    #Video Height: 240 pixels
    #Duration: 596.416667 seconds
    #Video Codec: h264
    #Bitrate: 512.211 kbps
