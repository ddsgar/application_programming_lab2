import tkinter as tk
from tkinter import filedialog
import vlc


root = tk.Tk()
root.title("Просмотр видео")

instance = vlc.Instance('--no-xlib')

player = instance.media_player_new()


def open_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mpg *.mpeg *.mov")])

    if file_path:
        media = instance.media_new(file_path)
        player.set_media(media)
        player.set_fullscreen(False)
        player.play()

open_button = tk.Button(root, text="Открыть видеофайл", command=open_video)
open_button.pack(pady=10)

def exit_app():
    player.stop()
    root.quit()


exit_button = tk.Button(root, text="Выход", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()
