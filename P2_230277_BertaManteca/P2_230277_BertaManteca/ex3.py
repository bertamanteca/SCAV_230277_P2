import os

def change_chroma_subsampling(input_file, output_file, pixel_format):
    command = f'ffmpeg -i {input_file} -pix_fmt {pixel_format} {output_file}'
    os.system(command)


input_file = 'BigBuckBunny_512kb.mp4'
output_file = 'BigBuckBunny_change_chroma.mp4'
print('Choose a pixel format (e.g., yuv420p, yuv422p, yuv444p):')
pixel_format = input()

change_chroma_subsampling(input_file, output_file, pixel_format)
