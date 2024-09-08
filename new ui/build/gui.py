

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
    text="Digital Twin ",
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
window.resizable(False, False)
window.mainloop()
