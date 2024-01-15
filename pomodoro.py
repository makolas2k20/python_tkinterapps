# =============================================================================
# DAY 28: Tkinter, Dynamic Typing
# Project - Pomodoro GUI App
# =============================================================================
import tkinter as tk
import time

# CONSTANTS
HOME_DIR = "./DAY28/"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MAX_REPS = 4
GREEN_CHECK = "✓"

# GLOBAL VARIABLES
reps = 0
timer = None

# TIMER RESET


def reset_all():
    global timer, reps
    root.after_cancel(timer)
    title_label.config(
        text="Press start",
        fg=GREEN,
    )
    canvas.itemconfig(
        timer_text,
        text="00:00",
    )
    checkmark_label.config(
        text=""
    )
    reps = 0

# TIMER MECHANISM


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(
            text=f"{LONG_BREAK_MIN} min. break",
            fg=RED
        )
        timer_sec = LONG_BREAK_MIN * 60
        reps = 1
    elif reps % 2 == 0:
        title_label.config(
            text=f"{SHORT_BREAK_MIN} min. break",
            fg=PINK
        )
        timer_sec = SHORT_BREAK_MIN * 60
        update_checks(reps // 2)
    else:
        title_label.config(
            text="Work",
            fg=GREEN
        )
        timer_sec = WORK_MIN * 60
    countdown_timer(timer_sec)


def update_checks(count):
    checkmarks = ""
    for _ in range(count):
        checkmarks += GREEN_CHECK

    checkmark_label.config(
        text=checkmarks,
    )


# COUNTDOWN MECHANISM


def countdown_timer(seconds):
    global timer
    display_time = format_time(seconds)
    canvas.itemconfig(
        timer_text,
        text=display_time,
    )
    if seconds > 0:
        timer = root.after(1000, countdown_timer, seconds-1)
    else:
        start_timer()


def format_time(seconds):
    timer = int(seconds)
    time_in_minutes = str(timer // 60).rjust(2, "0")
    seconds_remaining = str(timer % 60).rjust(2, "0")
    formatted_time = f"{time_in_minutes}:{seconds_remaining}"
    return formatted_time


# UI SETUP
# Main Window
root = tk.Tk()
root.title("Pomodoro App")
root.config(
    bg=YELLOW,
    padx=100,
    pady=50,
)

# Title
title_label = tk.Label(
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 40, "normal"),
    text="Press start",
    wraplength=300
)
title_label.grid(
    column=2,
    row=1,
)

# BG Image
bg_img = tk.PhotoImage(
    file=HOME_DIR + "tomato.png",
)
canvas = tk.Canvas(
    bg=YELLOW,
    highlightthickness=0,
    width=200,
    height=224,
)
canvas.create_image(
    100,
    112,
    image=bg_img,
)
# Timer text
timer_text = canvas.create_text(
    100,
    135,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold"),
)
canvas.grid(
    column=2,
    row=2
)


# Buttons
start_button = tk.Button(
    command=start_timer,
    text="Start",
)
start_button.grid(
    column=1,
    row=3
)

reset_button = tk.Button(
    command=reset_all,
    text="Reset"
)
reset_button.grid(
    column=3,
    row=3
)

# Check mark progress
checkmark_label = tk.Label(
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 20, "bold"),
)
checkmark_label.grid(
    column=2,
    row=4
)

root.mainloop()
