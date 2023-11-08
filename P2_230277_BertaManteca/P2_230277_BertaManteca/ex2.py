import os

def create_new_container(new_name, new_width, new_height):

    command1 = 'ffmpeg -i BigBuckBunny_512kb.mp4 -ss 00:00:00 -to 00:01:00 -c:v copy -c:a copy tallat.mp4'
    os.system(command1)


    command2 = 'ffmpeg -i tallat.mp4 a1.mp3'
    os.system(command2)

    stereo = 'ffmpeg -i a1.mp3 -ac 2 a1_stereo.mp3'
    os.system(stereo)


    command3 = 'ffmpeg -i tallat.mp4 -vn -b:a 10k a2.aac'
    os.system(command3)

    # resolution
    resolution_command = 'ffmpeg -i tallat.mp4 -vf "scale={}:{}" -c:v libx264 -c:a copy modified_video.mp4'.format(new_width, new_height)
    os.system(resolution_command)

    command4 = 'ffmpeg -i modified_video.mp4 -i a1_stereo.mp3 -i a2.aac -map 0 -map 1 -map 2 -c copy ' \
               '-shortest {}'.format(new_name)
    os.system(command4)

name_new_container = 'new_container.mp4'
new_resolution_width = 1280
new_resolution_height = 720
create_new_container(name_new_container, new_resolution_width, new_resolution_height)
