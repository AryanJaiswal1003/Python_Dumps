from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT = ("Times New Roman", 35, "bold")
TIMER_FONT = ("Times New Roman", 18, "bold")

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0 # Keeps track of how many sessions have passed
timer = None  # Stores the reference for window.after() so it can be cancelled

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Stops the current timer and resets everything back to initial state."""
    global reps
    reps = 0
    window.after_cancel(timer) # Cancels the scheduled countdown
    tick_label.config(text="") # Removes all check marks
    pomodoro_canvas.itemconfig(timer_text, text="00:00") # Reset timer text
    timer_label.config(text="Timer") # Reset title label


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """Decides whether to start a Work session, Short Break, or Long Break."""
    global reps
    reps += 1 # Increment number of sessions

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # Every 8th rep → Long Break
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0: # Every 2nd rep → Short Break
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else: # Otherwise → Work Session
        count_down(work_sec)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """Handles the countdown timer display and continues until 0 is reached."""

    # Convert seconds into minutes:seconds format
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Formatting seconds and minutes to show leading zero (e.g., 05:09)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    # Update the timer text on the canvas
    pomodoro_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continue countdown if time is left
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # Call count_down again after 1 second with decremented count

    # Once timer finishes, start the next session automatically
    else:
        start_timer()

        tick = "" # Add ✔ for each completed work session
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            tick += "✔"
        tick_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


# Canvas for tomato image and timer text
pomodoro_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Load tomato image
pomodoro_canvas.create_image(100, 112, image=tomato_img)
timer_text = pomodoro_canvas.create_text(100, 130,text="00:00", fill="white", font=FONT)
pomodoro_canvas.grid(row=1, column=1)


# Main "Timer" label
timer_label = Label(text="Timer", font=FONT, background=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)


# Start button
start_button = Button(text="Start", font=TIMER_FONT, background=YELLOW, borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)


# Reset button
reset_button = Button(text="Reset", font=TIMER_FONT, background=YELLOW, borderwidth=0, command=reset_timer)
reset_button.grid(row=2,column=2)


# Label to show check marks after each completed work session
tick_label = Label(font=("Times New Roman", 15, "bold"), fg=GREEN, background=YELLOW, borderwidth=0)
tick_label.grid(row=3,column=1)


window.mainloop()