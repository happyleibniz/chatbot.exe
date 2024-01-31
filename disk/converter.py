from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from disk.print_delay import print_with_delay as print_with_delay


def select_folder():
    filepath = fd.askdirectory(
        title='Open a directory',
        initialdir='/',
    )

    showinfo(
        title='Selected Path',
        message=filepath
    )
    return filepath


def select_file():
    filetypes = (
        ('MPEG4 video files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    return filename


def convert_image_to_image(image_file, out_file, extension):
    # Open the *** image
    with Image.open(image_file) as img:
        # Save the image in *** format
        img.save(out_file, extension)# supports webp to png,jpg to png,png to jpg,png to webp


def handle_converter_command():
    print_with_delay("What do you want to convert?", delay=0.006)
    user_input = input("You: ")

    if "mp4 to mkv" in user_input:
        print_with_delay("Is this what you wanted? (y/n)", delay=0.006)
        user_input = input("You: ")
        if user_input.lower() == "yes" or user_input.lower() == "y":
            print_with_delay("Initializing converter, this may take a moment...", delay=0.006)
            try:
                import moviepy
                # Add your converter logic here
            except ImportError:
                print_with_delay("It looks like moviepy is not installed.", delay=0.006)
                print_with_delay("Please install it with:", delay=0.006)
                print_with_delay("``````````````````````", delay=0.006)
                print_with_delay("`pip3 install moviepy`", delay=0.006)
                print_with_delay("``````````````````````", delay=0.006)
                print_with_delay("moviepy requirements is:", delay=0.006)
                print_with_delay("``````````````````````", delay=0.006)
                print_with_delay("`tqdm<5.0,>=4.11.2`", delay=0.006)
                print_with_delay("`requests<3.0,>=2.8.1`", delay=0.006)
                print_with_delay("`proglog<=1.0.0`", delay=0.006)
                print_with_delay("`numpy>=1.17.3`", delay=0.006)
                print_with_delay("`imageio<3.0,>=2.5`", delay=0.006)
                print_with_delay("`imageio-ffmpeg>=0.2.0`", delay=0.006)
                print_with_delay("`pillow<10.1.0,>=8.3.2`", delay=0.006)
                print_with_delay("`charset-normalizer<4,>=2`", delay=0.006)
                print_with_delay("`idna<4,>=2.5`", delay=0.006)
                print_with_delay("`urllib3<3,>=1.21.1", delay=0.006)
                print_with_delay("`certifi>=2017.4.17", delay=0.006)
                print_with_delay("`colorama", delay=0.006)
                print_with_delay("``````````````````````", delay=0.006)
                print_with_delay("WARNING<!>moviepy may change over the year,suitable version moviepy-1.0.3(1/31/2024)",
                                 delay=0.006)
                return ModuleNotFoundError
            print_with_delay("WARNING<!>moviepy may change over the year,suitable version moviepy-1.0.3(1/31/2024)",
                             delay=0.006)

            print_with_delay("Importing necessary modules", delay=0.006)
            try:
                from moviepy.editor import VideoFileClip
                print_with_delay("Importing DONE", delay=0.006)

                def convert_mp4_to_mkv(input_file, output_file):
                    # Load the MP4 video clip
                    video_clip = VideoFileClip(input_file)

                    # Write the video clip to an MKV file
                    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

                showinfo(
                    title='Please select a file',
                    message='Please select a file'
                )
                file_name = select_file()
                # Replace 'input.mp4' and 'output.mkv' with your input and output file names
                showinfo(
                    title='Please select a directory',
                    message='Please select a directory'
                )
                file_dir = select_folder()
                convert_mp4_to_mkv(file_name, file_dir + '/output.mkv')
            except ImportError as e:
                print_with_delay("Unrecoverable error: Codec:ImportError, Error message:", e,
                                 "solution: please reinstall moviepy", delay=0.006)

# Function to print text with a slight delay
