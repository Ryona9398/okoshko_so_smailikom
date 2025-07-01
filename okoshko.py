import tkinter as tk
import random
import time
import threading


emoticons = [
    "(*ˊᗜˋ*)", "(⌒▽⌒)", "(*´▽*)", "(・∀・)", "(o^∀^o)",
    "ヾ(•ω•)o", "o(≧∇≦o)", "(╯°Д°)╯", "٩(๑❛ᴗ❛๑)۶", "(*・ω・)ﾉ", "XD", "XP", "=＾● ⋏ ●＾="
]


def update_emoticon(label):

    while True:
        random_emoticon = random.choice(emoticons)
        label.config(text=random_emoticon)
        time.sleep(60)


def create_emoticon_window():

    root = tk.Tk()
    root.title("xD")


    root.overrideredirect(True)

    emoticon_label = tk.Label(root,
                              text="",
                              font=("VT323", 36),
                              bg="black",
                              fg="red",
                              padx=20,
                              pady=20)
    emoticon_label.pack()


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 200
    window_height = 100
    x_coordinate = screen_width - window_width - 20
    y_coordinate = screen_height - window_height - 60

    root.geometry(f"+{x_coordinate}+{y_coordinate}")

    update_thread = threading.Thread(target=update_emoticon, args=(emoticon_label,))
    update_thread.daemon = True
    update_thread.start()

    root.mainloop()


if __name__ == "__main__":
    create_emoticon_window()
