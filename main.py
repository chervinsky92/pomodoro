from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND = '#e4f9ff'
GREEN = '#379B46'
PINK = '#e2979c'
RED = '#e7305b'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_text.config(text='Timer', fg='black')
    check_marks.config(text='')
    global reps
    reps = 0

    # Start button is no longer disabled
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # Disable start button while timer is running
    start_button.config(state="disabled")

    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    global reps
    reps += 1

    # Keep window on screen
    window.attributes('-topmost', 1)

    # Work reps
    if reps in (1, 3, 5, 7):
        countdown(work_sec)
        title_text.config(text=' Work ', fg=GREEN)
    # Short break reps
    elif reps in (2, 4, 6):
        countdown(short_break_sec)
        title_text.config(text='Break', fg=PINK)
    # Long break rep
    elif reps == 8:
        countdown(long_break_sec)
        title_text.config(text='Break', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # Format count into (M)M:SS format
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec:02}')

    # Reduce seconds count by 1 every second
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    # Start next rep when count is 0
    else:
        start_timer()

        # Add a check mark for every completed work rep
        checks = '✔' * (reps // 2)
        check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=BACKGROUND)

title_text = Label(text='Timer', font=(FONT_NAME, 50), bg=BACKGROUND)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(106, 135, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))

start_button = Button(text='Start', highlightthickness=0, command=start_timer)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)

check_marks = Label(fg=GREEN, font=(FONT_NAME, 30), bg=BACKGROUND)

# Grid layout
title_text.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_marks.grid(column=1, row=3)

window.mainloop()