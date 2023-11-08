from ex5funct import VideoProcessor  # Import the VideoProcessor class

class ExtendedVideoProcessor(VideoProcessor):
    def ex5(self):
        print("Extended method: ex5")
        # You can add your code here to extend the functionality

if __name__ == '__main__':
    # Interaction with the ExtendedVideoProcessor class
    input_video = 'BigBuckBunny_512kb.mp4'
    processor = ExtendedVideoProcessor(input_video)

    # Call the extended method ex5
    processor.ex5()

