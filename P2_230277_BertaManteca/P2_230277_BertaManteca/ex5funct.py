import subprocess
import json

class VideoProcessor:
    def __init__(self, input_file):
        self.input_file = input_file

    def modify_resolution(self, output_file, new_width, new_height):
        command = f'ffmpeg -i {self.input_file} -vf "scale={new_width}:{new_height}" {output_file}'
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    def change_chroma_subsampling(self, output_file, pixel_format):
        command = f'ffmpeg -i {self.input_file} -pix_fmt {pixel_format} {output_file}'
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    def get_video_info(self):
        command = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,duration,codec_name,bit_rate', '-of', 'json', self.input_file]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        video_info = json.loads(result.stdout)

        if 'streams' in video_info and len(video_info['streams']) > 0:
            stream = video_info['streams'][0]
            return {
                "Video Width": stream['width'],
                "Video Height": stream['height'],
                "Duration": stream['duration'],
                "Video Codec": stream['codec_name'],
                "Bitrate": int(stream['bit_rate']) / 1000
            }
        else:
            return {"Error": "No video streams found in the file."}

# Interaction with the VideoProcessor class
def main():
    input_video = 'BigBuckBunny_512kb.mp4'
    processor = VideoProcessor(input_video)

    # Modify resolution
    output_resolution = 'output_resolution.mp4'
    new_width = 1280
    new_height = 720
    processor.modify_resolution(output_resolution, new_width, new_height)

    # Change chroma subsampling
    output_subsampling = 'output_subsampling.mp4'
    pixel_format = 'yuv422p'
    processor.change_chroma_subsampling(output_subsampling, pixel_format)

    # Get and print video information
    video_info = processor.get_video_info()
    print("Video Information:")
    for key, value in video_info.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()
