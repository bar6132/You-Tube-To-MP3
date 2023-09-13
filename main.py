import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


# Function to download and convert the video to mp3
def download_and_convert():
    url = url_entry.get()

    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path='./Music')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        result_label.config(text=f'{yt.title} has been successfully downloaded.')
    except Exception as e:
        result_label.config(text=f'Error: {str(e)}')


# Create the main application window
app = tk.Tk()
app.title("YouTube Video to MP3 Converter")

# Create and pack widgets
url_label = tk.Label(app, text="Enter URL of YouTube video:")
url_label.pack()

url_entry = tk.Entry(app, width=50)
url_entry.pack()

convert_button = tk.Button(app, text="Convert to MP3", command=download_and_convert)
convert_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Start the main loop
app.mainloop()
