import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Link Invalid")
    print("Download Complete")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filezise
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


# System 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(padx=10,pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


# Progress percentage
pPrecentage = customtkinter.CTkLabel(app, text="0%")
pPrecentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Link Button
Submit = customtkinter.CTkButton(app, text="Submit Link", command=startDownload)
Submit.pack()


# Run app
app.mainloop()