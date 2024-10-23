

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rugve\Desktop\python project\new ui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#30313A")


canvas = Canvas(
    window,
    bg = "#30313A",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1238.0,
    843.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    291.0,
    379.0,
    image=image_image_2
)

canvas.create_text(
    1063.0,
    879.0,
    anchor="nw",
    text="Exercise Duration:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1310.5,
    819.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1291.0,
    y=796.0,
    width=39.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1204.5,
    959.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1079.0,
    y=936.0,
    width=251.0,
    height=44.0
)

canvas.create_text(
    1058.0,
    708.0,
    anchor="nw",
    text="Stress Levels:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1055.0,
    796.0,
    anchor="nw",
    text="Sleep Quality:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1359.0,
    936.0,
    anchor="nw",
    text="hrs",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1353.0,
    708.0,
    anchor="nw",
    text="1-10",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1353.0,
    799.0,
    anchor="nw",
    text="1-10",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    888.0,
    378.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    812.0,
    843.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    294.0,
    845.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    721.0,
    66.0,
    image=image_image_6
)

canvas.create_text(
    31.0,
    23.0,
    anchor="nw",
    text="Diabetes Care System ",
    fill="#FFFFFF",
    font=("Lexend Regular", 64 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    287.0,
    190.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    889.0,
    187.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    810.0,
    632.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    297.0,
    633.0,
    image=image_image_10
)

canvas.create_text(
    40.0,
    161.0,
    anchor="nw",
    text="Enter Patient Details",
    fill="#FFFFFF",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    611.0,
    158.0,
    anchor="nw",
    text="Medical History:",
    fill="#FFFFFF",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    587.0,
    603.0,
    anchor="nw",
    text="Dietary Information:",
    fill="#FFFFFF",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    48.0,
    604.0,
    anchor="nw",
    text="Current Health Status:",
    fill="#FFFFFF",
    font=("Lexend Regular", 40 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    287.5,
    302.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=55.0,
    y=279.0,
    width=465.0,
    height=44.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1030.5,
    262.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=982.0,
    y=241.0,
    width=97.0,
    height=40.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    352.0,
    734.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=306.0,
    y=713.0,
    width=92.0,
    height=40.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    96.0,
    408.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=55.0,
    y=385.0,
    width=82.0,
    height=44.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    96.0,
    495.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=55.0,
    y=472.0,
    width=82.0,
    height=44.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    927.0,
    318.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=884.0,
    y=295.0,
    width=86.0,
    height=44.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    805.5,
    968.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=602.0,
    y=947.0,
    width=407.0,
    height=40.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    347.0,
    791.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=306.0,
    y=768.0,
    width=82.0,
    height=44.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    441.0,
    901.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=400.0,
    y=878.0,
    width=82.0,
    height=44.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    870.5,
    475.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=624.0,
    y=451.0,
    width=493.0,
    height=46.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    805.5,
    875.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=602.0,
    y=849.0,
    width=407.0,
    height=50.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    373.0,
    962.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=343.0,
    y=938.0,
    width=60.0,
    height=46.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    1019.5,
    371.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=904.0,
    y=350.0,
    width=231.0,
    height=41.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    780.0,
    763.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=612.0,
    y=740.0,
    width=336.0,
    height=44.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    340.0,
    852.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=299.0,
    y=831.0,
    width=82.0,
    height=41.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    236.0,
    410.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=195.0,
    y=389.0,
    width=82.0,
    height=40.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    427.0,
    409.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=386.0,
    y=388.0,
    width=82.0,
    height=40.0
)

canvas.create_text(
    44.0,
    234.0,
    anchor="nw",
    text="Name:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    616.0,
    238.0,
    anchor="nw",
    text="Duration of Diabetes:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    597.0,
    685.0,
    anchor="nw",
    text="Recent Meals:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    32.0,
    710.0,
    anchor="nw",
    text="Glucose level:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    44.0,
    336.0,
    anchor="nw",
    text="Age:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    44.0,
    430.0,
    anchor="nw",
    text="Gender:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    616.0,
    286.0,
    anchor="nw",
    text="Diabetes Type:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    31.0,
    766.0,
    anchor="nw",
    text="HbA1c Levels:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    616.0,
    347.0,
    anchor="nw",
    text="Known Allergies:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    597.0,
    904.0,
    anchor="nw",
    text="Usual Dietary Habits:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    33.0,
    834.0,
    anchor="nw",
    text="Insulin Intake:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    34.0,
    880.0,
    anchor="nw",
    text="Time since last intake:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    617.0,
    404.0,
    anchor="nw",
    text="Other Medical Conditions:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    583.0,
    796.0,
    anchor="nw",
    text="Planned Sugary Food Intake:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    34.0,
    938.0,
    anchor="nw",
    text="Physical Activity:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    182.0,
    336.0,
    anchor="nw",
    text="Weight:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    300.0,
    379.0,
    anchor="nw",
    text="kg",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1002.0,
    293.0,
    anchor="nw",
    text="1/2",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    428.0,
    769.0,
    anchor="nw",
    text="%",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    419.0,
    828.0,
    anchor="nw",
    text="ml",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    509.0,
    880.0,
    anchor="nw",
    text="hrs",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    171.0,
    472.0,
    anchor="nw",
    text="M/F",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    500.0,
    382.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1101.0,
    238.0,
    anchor="nw",
    text="yrs",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    432.0,
    711.0,
    anchor="nw",
    text="mg/dL",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    372.0,
    332.0,
    anchor="nw",
    text="Height:",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1208.0,
    y=326.0,
    width=206.0,
    height=63.0
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1238.0,
    627.0,
    image=image_image_11
)

canvas.create_text(
    1064.0,
    603.0,
    anchor="nw",
    text="Lifestyle Factors:",
    fill="#FFFFFF",
    font=("Lexend Regular", 40 * -1)
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    1310.5,
    730.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=1291.0,
    y=707.0,
    width=39.0,
    height=44.0
)

canvas.create_text(
    446.0,
    941.0,
    anchor="nw",
    text="1-10",
    fill="#FFFFFF",
    font=("Lexend Regular", 32 * -1)
)



# Global variables to store user inputs
name = ""
age = 0
gender = ""
duration_of_diabetes = 0
glucose_levels = 0
diabetes_type = ""
usual_dietary_habits = ""
hbA1c_levels = 0
time_since_last_intake = 0
other_medical_conditions = ""
planned_sugar_intake = 0
physical_activity = 0
known_allergies = ""
recent_meals = ""
insulin_intake = 0
weight = 0
height = 0
stress_level = 0
sleep_quality = 0
exercise_duration = 0

def save_input():
    # Update global variables with input data
    global name, age, gender, duration_of_diabetes, glucose_levels, diabetes_type
    global usual_dietary_habits, hbA1c_levels, time_since_last_intake, other_medical_conditions
    global planned_sugar_intake, physical_activity, known_allergies, recent_meals
    global insulin_intake, weight, height, stress_level, sleep_quality, exercise_duration

    name = entry_3.get()
    age = entry_6.get()
    gender = entry_7.get()
    duration_of_diabetes = entry_4.get()
    glucose_levels = entry_5.get()
    diabetes_type = entry_8.get()
    usual_dietary_habits = entry_9.get()
    hbA1c_levels = entry_10.get()
    time_since_last_intake = entry_11.get()
    other_medical_conditions = entry_12.get()
    planned_sugar_intake = entry_13.get()
    physical_activity = entry_14.get()
    known_allergies = entry_15.get()
    recent_meals = entry_16.get()
    insulin_intake = entry_17.get()
    weight = entry_18.get()
    height = entry_19.get()
    stress_level = entry_20.get()
    sleep_quality = entry_1.get()
    exercise_duration = entry_2.get()

    # Convert numeric inputs if possible
    try:
        stress_level = float(stress_level)
        sleep_quality = float(sleep_quality)
        exercise_duration = float(exercise_duration)
        glucose_levels = float(glucose_levels)
        age = float(age)
        hbA1c_levels = float(hbA1c_levels)
        duration_of_diabetes = float(duration_of_diabetes)
        time_since_last_intake = float(time_since_last_intake)
        insulin_intake = float(insulin_intake)
        physical_activity = float(physical_activity)
        weight = float(weight)
        height = float(height)
    except ValueError:
        pass  # If conversion fails, just keep the original value


    print("Stress level saved:", stress_level)
    print("Sleep quality saved:", sleep_quality)
    print("Exercise duration saved:", exercise_duration)
    print("Name saved:", name)
    print("Duration of diabetes saved:", duration_of_diabetes)
    print("Glucose levels saved:", glucose_levels)
    print("Age saved:", age)
    print("Gender saved:", gender)
    print("Diabetes type saved:", diabetes_type)
    print("Usual dietary habits saved:", usual_dietary_habits)
    print("HbA1c levels saved:", hbA1c_levels)
    print("Time since last intake saved:", time_since_last_intake)
    print("Other medical conditions saved:", other_medical_conditions)
    print("Planned sugar intake saved:", planned_sugar_intake)
    print("Physical activity saved:", physical_activity)
    print("Known allergies saved:", known_allergies)
    print("Recent meals saved:", recent_meals)
    print("Insulin intake saved:", insulin_intake)
    print("Weight saved:", weight)
    print("Height saved:", height)


# Modify the button command to call the save_input function
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=save_input,
    relief="flat"
)
button_1.place(
    x=1208.0,
    y=326.0,
    width=206.0,
    height=63.0
)
window.resizable(False, False)
window.mainloop()



#frame 2


import time
import os
import google.oauth2.credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Google Fit API settings
SCOPES = ['https://www.googleapis.com/auth/fitness.heart_rate.read']

# Path for Google Fit credentials
CLIENT_SECRET_FILE = 'client_secret.json'  # Replace this with your actual client secret path
TOKEN_FILE = 'token.json'

#############################################################################################
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rugve\Desktop\python project\new ui\frame 2\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("1200x900")
window.configure(bg = "#171821")


canvas = Canvas(
    window,
    bg = "#171821",
    height = 900,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1110.0,
    y=17.0,
    width=40.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1049.0,
    169.0,
    image=image_image_1
)

canvas.create_text(
    942.0,
    75.0,
    anchor="nw",
    text="HEART RATE ",
    fill="#FFFFFF",
    font=("DeterminationMono", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1048.0,
    184.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    993.0,
    443.0,
    image=image_image_3
)

canvas.create_text(
    827.0,
    315.0,
    anchor="nw",
    text="OXYGEN LEVEL SpO2",
    fill="#FFFFFF",
    font=("DeterminationMono", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1093.0,
    449.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    990.0,
    730.0,
    image=image_image_5
)

canvas.create_text(
    827.0,
    606.0,
    anchor="nw",
    text="BODY TEMPERATURE",
    fill="#FFFFFF",
    font=("DeterminationMono", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    900.0,
    744.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    565.0,
    473.0,
    image=image_image_7
)
#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
canvas.create_rectangle(
    991.0,
    157.0,
    1094.0,
    211.0,
    fill="#393A4A",
    outline="")

########################################################################
import os
import json
import time  # Make sure to import time
import tkinter as tk
from tkinter import Canvas
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from pathlib import Path

# Define the scopes for Google Fit
SCOPES = ['https://www.googleapis.com/auth/fitness.heart_rate.read']


# Function to authenticate and get Google Fit service
def get_google_fit_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('fitness', 'v1', credentials=creds)
    return service


# Function to fetch heart rate data from Google Fit
def fetch_heart_rate_data():
    service = get_google_fit_service()
    data_sources = service.users().dataSources().list(userId='me').execute()

    # Look for the heart rate data source
    for data_source in data_sources['dataSource']:
        if 'heart_rate' in data_source['dataStreamName'].lower():
            dataset = service.users().dataSources().datasets().get(
                userId='me',
                dataSourceId=data_source['dataStreamId'],
                datasetId=f'0-{int(time.time() * 1000000000)}').execute()

            heart_rates = []
            for point in dataset['point']:
                for value in point['value']:
                    heart_rate = value.get('fpVal')
                    if heart_rate is not None:
                        heart_rates.append(heart_rate)

            if heart_rates:
                return heart_rates[-1]  # Return the latest heart rate
    return None


# Tkinter window to display heart rate on an existing canvas
class HeartRateApp:
    def __init__(self, canvas):
        self.canvas = canvas
        self.heart_rate_label = self.canvas.create_text(
            1040, 184,  # Coordinates for your label
            text="Heart Rate: Fetching...",
            font=("Arial", 20),
            fill="white"  # Change color if needed
        )
        self.update_heart_rate()

    def update_heart_rate(self):
        heart_rate = fetch_heart_rate_data()
        if heart_rate is not None:
            # Limit heart rate to the first 3 digits
            display_rate = int(round(heart_rate))
            self.canvas.itemconfig(self.heart_rate_label, text=f" {display_rate} BPM")
        else:
            self.canvas.itemconfig(self.heart_rate_label, text="Heart Rate: No data")

        # Update every 60 seconds
        self.canvas.after(60000, self.update_heart_rate)


if __name__ == "__main__":
    # Existing Tkinter window setup


    canvas.pack()

    # Initialize the heart rate display in the existing canvas
    heart_rate_app = HeartRateApp(canvas)







####################################################################################
def create_bar_diagram(canvas):
    # Define the dimensions of the canvas and the bars
    bar_width = 30
    spacing = 6
    start_x = 850  # Starting position for the bars on the x-axis
    start_y = 550  # Starting position for the bars on the y-axis
    max_height = 200  # Maximum height for the bars

    # Bar values
    bar_values = [98, 97, 96, 99]
    bar_colors = ["#4CAF50", "#4CAF50", "#4CAF50", "#4CAF50"]  # Green color for bars

    # Create the bars
    for i, value in enumerate(bar_values):
        # Calculate the height of the bar based on the value
        bar_height = (value / 100) * max_height

        # Create a rectangle for the bar
        canvas.create_rectangle(
            start_x + (bar_width + spacing) * i,
            start_y - bar_height,
            start_x + (bar_width + spacing) * i + bar_width,
            start_y,
            fill=bar_colors[i],
            outline=""
        )

        # Create text below the bar
        canvas.create_text(
            start_x + (bar_width + spacing) * i + bar_width / 2,
            start_y + 5,  # Position slightly below the bar
            text=str(value),
            fill="#FFFFFF",
            font=("Arial", 12)
        )

    # Create the y-axis labels (100 at the top and 0 at the bottom)
    y_labels = [0, 70, 80, 90, 100]
    for i, label in enumerate(y_labels):
        canvas.create_text(
            start_x - 30,  # Position to the left of the bars
            start_y - (i * (max_height / 4)),  # Calculate the position based on the label
            text=str(label),
            fill="#FFFFFF",
            font=("Arial", 10)
        )
create_bar_diagram(canvas)
#######################################################################

canvas.create_rectangle(
    972.0,
    644.0,
    1158.0,
    841.0,
    fill="#393A4A",
    outline="")
##############################################################################
import math


def draw_wave_graph(canvas):
    # Rectangle area (using your values)
    rect_left = 972.0
    rect_right = 1158.0
    rect_top = 644.0
    rect_bottom = 841.0
    graph_height = rect_bottom - rect_top
    graph_width = rect_right - rect_left

    # Draw temperature labels on the y-axis
    y_labels = [38.0, 37.5, 37.0, 36.5, 36.0]
    y_label_positions = [(rect_top + i * (graph_height / 4)) for i in range(5)]
    for i, label in enumerate(y_labels):
        canvas.create_text(
            rect_left - 20,  # Position to the left of the graph
            y_label_positions[i],
            text=str(label),
            fill="#FFFFFF",
            font=("Arial", 10)
        )

    # Draw time labels on the x-axis
    x_labels = [0, 12, 24]
    for i, label in enumerate(x_labels):
        canvas.create_text(
            rect_left + (i * (graph_width / 2)),
            rect_bottom + 10,  # Position below the graph
            text=str(label),
            fill="#FFFFFF",
            font=("Arial", 10)
        )

    # Draw sine wave curve for temperature change (simulated)
    prev_x, prev_y = None, None
    for x in range(int(graph_width)):
        time_hour = x * 24 / graph_width  # Scale x value to time in hours
        temp = 37 + math.sin(math.radians(time_hour * 15))  # Sine wave for temp

        # Scale the temperature value to fit within the graph height
        scaled_temp = rect_bottom - ((temp - 36.0) / (38.0 - 36.0) * graph_height)

        if prev_x is not None and prev_y is not None:
            canvas.create_line(
                rect_left + prev_x, prev_y, rect_left + x, scaled_temp,
                fill="#00FF00",  # Green line
                width=2
            )
        prev_x, prev_y = x, scaled_temp
draw_wave_graph(canvas)
#############################################################################
image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    169.0,
    443.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    161.0,
    72.0,
    image=image_image_9
)



# Function to create the analysis window
def create_analysis():
    analysis_window = tk.Toplevel(window)
    analysis_window.title("Analysis")
    analysis_window.geometry("600x400")
    analysis_window.configure(bg="#30313A")  # Set background color

    # Create a frame for the analysis
    frame = tk.Frame(analysis_window, bg="#30313A")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Analysis title
    tk.Label(frame, text="Blood Sugar Analysis", bg="#30313A", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

    # Analysis results
    analysis_results = []

    # Hyperglycemia and hypoglycemia predictions
    if glucose_levels > 180:
        analysis_results.append("Warning: Possible Hyperglycemia detected! Immediate action needed.")
    elif glucose_levels < 70:
        analysis_results.append("Warning: Possible Hypoglycemia detected! Immediate action needed.")
    else:
        analysis_results.append("Blood sugar levels are within the normal range.")

    # Additional context based on input data
    if hbA1c_levels > 7:
        analysis_results.append("Consider adjusting your treatment plan due to high HbA1c levels.")

    if stress_level > 7:
        analysis_results.append(
            "High stress levels can impact blood sugar control. Consider stress-reducing techniques.")

    if physical_activity < 4:
        analysis_results.append("Increasing physical activity can help manage blood sugar levels.")

    # Display analysis results
    tk.Label(frame, text="Analysis Results:", bg="#30313A", fg="white", font=("Arial", 14)).pack(pady=10)

    # Create rectangles and display analysis results
    for result in analysis_results:
        # Create a frame for each analysis result with a specific background color
        result_frame = tk.Frame(frame, bg="#171f33", padx=10, pady=5)
        result_frame.pack(fill="x", pady=5)
        tk.Label(result_frame, text=f"- {result}", bg="#171f33", fg="white").pack(anchor="w")

    # Close button
    tk.Button(frame, text="Close", command=analysis_window.destroy, bg="#FF6347", fg="white").pack(pady=20)


# Button to trigger analysis
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")) # Adjust the file path as necessary
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_analysis,  # Change command to call the function
    relief="flat"
)
button_2.place(
    x=34.0,
    y=251.0,
    width=165.0,
    height=73.0
)

######################
heart_bpm = 98
spo2 = 99
body_temperature = 37.8
######################

import tkinter as tk
from tkinter import PhotoImage, Button

# Sample input data
name = "John Doe"
age = 45
gender = "Male"
duration_of_diabetes = 10
diabetes_type = "Type 2"
glucose_levels = 185  # Example of high glucose
hbA1c_levels = 7.5
stress_level = 8
sleep_quality = 5
physical_activity = 3
exercise_duration = 1
insulin_intake = 8
time_since_last_intake = 6
recent_meals = "Rice, chicken, salad"
planned_sugar_intake = 50
usual_dietary_habits = "Moderate sugar, high carb"
known_allergies = "Peanuts"
other_medical_conditions = "Hypertension"



# Function to create the notification window
def create_notification():
    notification_window = tk.Toplevel(window)
    notification_window.title("Notifications")
    notification_window.geometry("500x500")
    notification_window.configure(bg="#30313A")  # Set background color

    # Create a frame for the notifications
    frame = tk.Frame(notification_window, bg="#30313A")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Notification title
    tk.Label(frame, text="Health Notifications", bg="#30313A", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

    notifications = []

    # Check for critical conditions
    if glucose_levels > 180:
        notifications.append("⚠️ High Glucose Levels Detected! Immediate action needed.")
    if hbA1c_levels > 7:
        notifications.append("⚠️ High HbA1c Levels Detected! Consider adjusting your treatment plan.")
    if stress_level > 7:
        notifications.append("⚠️ High Stress Level Detected! Consider stress management techniques.")
    if sleep_quality < 5:
        notifications.append("⚠️ Low Sleep Quality! Aim for better sleep hygiene.")
    if physical_activity < 4:
        notifications.append("⚠️ Insufficient Physical Activity! Consider increasing your activity levels.")

    if notifications:
        # Create a rectangle for each notification
        for notification in notifications:
            # Create a frame for each notification with a specific background color
            notification_frame = tk.Frame(frame, bg="#171f33", padx=10, pady=5)
            notification_frame.pack(fill="x", pady=5)
            tk.Label(notification_frame, text=notification, bg="#171f33", fg="white").pack(anchor="w")
    else:
        # No notifications
        no_alert_frame = tk.Frame(frame, bg="#171f33", padx=10, pady=5)
        no_alert_frame.pack(fill="x", pady=5)
        tk.Label(no_alert_frame, text="No Critical Notifications at this time.", bg="#171f33", fg="white").pack(anchor="w")

    # Close button
    tk.Button(frame, text="Close", command=notification_window.destroy, bg="#FF6347", fg="white").pack(pady=20)

# Button to trigger notification

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=create_notification,  # Call the function to create notifications
    relief="flat"
)
button_4.place(
    x=34.0,
    y=340.0,
    width=209.0,
    height=70.0
)




# Function to create the recommendations window
def create_recommendations():
    recommendations_window = tk.Toplevel(window)
    recommendations_window.title("Recommendations")
    recommendations_window.geometry("600x400")
    recommendations_window.configure(bg="#30313A")  # Set background color

    # Create a frame for the recommendations
    frame = tk.Frame(recommendations_window, bg="#30313A")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Recommendations title
    tk.Label(frame, text="Health Recommendations", bg="#30313A", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

    # Recommendations based on input data
    recommendations = []

    # Insulin adjustment recommendation
    if glucose_levels > 180:
        recommendations.append(f"Consider increasing insulin dosage by 2 units.")

    # Dietary changes recommendation
    if planned_sugar_intake > 40:
        recommendations.append(f"Reduce planned sugary food intake to below 40 grams.")

    # Checkup suggestion
    if hbA1c_levels > 7:
        recommendations.append(f"Schedule a medical check-up for further assessment of HbA1c levels.")

    # Exercise recommendation
    if physical_activity < 4:
        recommendations.append(f"Increase physical activity to at least 4/10.")

    # Stress management
    if stress_level > 7:
        recommendations.append(f"Consider stress management techniques such as yoga or meditation.")

    # Display recommendations
    tk.Label(frame, text="Recommendations:", bg="#30313A", fg="white", font=("Arial", 14)).pack(pady=10)

    # Create rectangles and display recommendations
    for rec in recommendations:
        # Create a frame for each recommendation with a specific background color
        rec_frame = tk.Frame(frame, bg="#171f33", padx=10, pady=5)
        rec_frame.pack(fill="x", pady=5)
        tk.Label(rec_frame, text=f"- {rec}", bg="#171f33", fg="white").pack(anchor="w")

    # Close button
    tk.Button(frame, text="Close", command=recommendations_window.destroy, bg="#FF6347", fg="white").pack(pady=20)


# Button to trigger recommendations
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=create_recommendations,  # Change command to call the function
    relief="flat"
)
button_5.place(
    x=34.0,
    y=192.0,
    width=271.0,
    height=51.0
)

import tkinter as tk

name = "John Doe"
age = 45
gender = "Male"
duration_of_diabetes = 10
diabetes_type = "Type 2"
glucose_levels = 185
hbA1c_levels = 7.5

stress_level = 8
sleep_quality = 5
physical_activity = 3
exercise_duration = 1
insulin_intake = 8
time_since_last_intake = 6
recent_meals = "Rice, chicken, salad"
planned_sugar_intake = 50
usual_dietary_habits = "Moderate sugar, high carb"
known_allergies = "Peanuts"
other_medical_conditions = "Hypertension"

def create_health_report():
    # Create a new window for the health report
    report_window = tk.Toplevel(window)
    report_window.title("Health Report")
    report_window.geometry("600x600")
    report_window.configure(bg="#30313A")  # Set background color

    # Create main frame for layout
    main_frame = tk.Frame(report_window, bg="#30313A")
    main_frame.pack(expand=True, fill="both")

    # Left frame for basic info
    left_frame = tk.Frame(main_frame, bg="#171f33", width=300)  # Changed to #171f33
    left_frame.pack(side="left", fill="both", padx=10, pady=10)

    # Right frame for other info
    right_frame = tk.Frame(main_frame, bg="#171f33", width=250)  # Changed to #171f33
    right_frame.pack(side="right", fill="both", padx=10, pady=10)

    # Create labels in left frame
    tk.Label(left_frame, text="Patient Information", bg="#171f33", fg="white", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(left_frame, text=f"Name: {name}", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(left_frame, text=f"Age: {age}", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(left_frame, text=f"Gender: {gender}", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(left_frame, text=f"Duration of Diabetes: {duration_of_diabetes} years", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(left_frame, text=f"Diabetes Type: {diabetes_type}", bg="#171f33", fg="white").pack(anchor="w", padx=10)

    # Create labels in right frame for other info
    tk.Label(right_frame, text="Other Information", bg="#171f33", fg="white", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(right_frame, text="Vital Signs:", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Glucose Levels: {glucose_levels} mg/dL", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- HbA1c Levels: {hbA1c_levels}%", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Heart Rate: {heart_bpm} bpm", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Oxygen Level: {spo2}%", bg="#171f33", fg="white").pack(anchor="w", padx=10)

    # Additional sections
    tk.Label(right_frame, text="Lifestyle Factors:", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Stress Level: {stress_level}/10", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Sleep Quality: {sleep_quality}/10", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Physical Activity: {physical_activity}/10", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(right_frame, text=f"- Exercise Duration: {exercise_duration} hrs", bg="#171f33", fg="white").pack(anchor="w", padx=10)

    # Create two bottom rectangles for insulin and dietary info
    insulin_frame = tk.Frame(report_window, bg="#171f33", height=100)  # Changed to #171f33
    insulin_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    tk.Label(insulin_frame, text="Insulin Intake", bg="#171f33", fg="white", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(insulin_frame, text=f"- Insulin Intake: {insulin_intake} ml", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(insulin_frame, text=f"- Time Since Last Intake: {time_since_last_intake} hrs", bg="#171f33", fg="white").pack(anchor="w", padx=10)

    dietary_frame = tk.Frame(report_window, bg="#171f33", height=100)  # Changed to #171f33
    dietary_frame.pack(side="bottom", fill="x", padx=10)

    tk.Label(dietary_frame, text="Dietary Information", bg="#171f33", fg="white", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(dietary_frame, text=f"- Recent Meals: {recent_meals}", bg="#171f33", fg="white").pack(anchor="w", padx=10)
    tk.Label(dietary_frame, text=f"- Planned Sugary Food Intake: {planned_sugar_intake} grams", bg="#171f33", fg="white").pack(anchor="w", padx=10)

    # Highlighting Critical Events
    critical_events_frame = tk.Frame(report_window, bg="#171f33")  # Changed to #171f33
    critical_events_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    tk.Label(critical_events_frame, text="Critical Events:", bg="#171f33", fg="red", font=("Arial", 14, "bold")).pack(pady=5)


    high_glucose_threshold = 180
    low_glucose_threshold = 70
    high_heart_rate_threshold = 100
    low_oxygen_threshold = 95
    abnormal_hba1c_threshold = 7


    # Check for critical events and display
    if glucose_levels > high_glucose_threshold:
        tk.Label(critical_events_frame, text="- High Glucose Levels Detected!", bg="#171f33", fg="red", font=("Arial", 12)).pack(anchor="w", padx=10)
    elif glucose_levels < low_glucose_threshold:
        tk.Label(critical_events_frame, text="- Low Glucose Levels Detected!", bg="#171f33", fg="red", font=("Arial", 12)).pack(anchor="w", padx=10)
    if heart_bpm > high_heart_rate_threshold:
        tk.Label(critical_events_frame, text="- High Heart Rate Detected!", bg="#171f33", fg="red", font=("Arial", 12)).pack(anchor="w", padx=10)
    if spo2 < low_oxygen_threshold:
        tk.Label(critical_events_frame, text="- Low Oxygen Level Detected!", bg="#171f33", fg="red", font=("Arial", 12)).pack(anchor="w", padx=10)
    if hbA1c_levels > abnormal_hba1c_threshold:
        tk.Label(critical_events_frame, text="- Abnormal HbA1c Levels Detected!", bg="#171f33", fg="red", font=("Arial", 12)).pack(anchor="w", padx=10)

    # Run the Tkinter main loop


# Load button image (replace with the path to your actual image)
button_image_3 = tk.PhotoImage(file=relative_to_assets("button_3.png"))

# Button setup to generate the health report
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_health_report,  # Call the create_health_report function
    relief="flat"
)
button_3.place(
    x=34.0,
    y=125.0,
    width=212.0,
    height=59.0
)


window.resizable(False, False)
window.mainloop()


