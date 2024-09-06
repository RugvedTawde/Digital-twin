



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rugve\Desktop\python project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#28A6AF")


canvas = Canvas(
    window,
    bg = "#28A6AF",
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
    1231.0,
    797.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    305.0,
    376.0,
    image=image_image_2
)

canvas.create_text(
    1042.0,
    786.0,
    anchor="nw",
    text="Exercise Duration:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1294.5,
    748.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1275.0,
    y=725.0,
    width=39.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1162.5,
    868.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1063.0,
    y=845.0,
    width=199.0,
    height=44.0
)

canvas.create_text(
    1042.0,
    664.0,
    anchor="nw",
    text="Stress Levels:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1039.0,
    726.0,
    anchor="nw",
    text="Sleep Quality:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1291.0,
    846.0,
    anchor="nw",
    text="hrs",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1338.0,
    664.0,
    anchor="nw",
    text="1-10",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1338.0,
    726.0,
    anchor="nw",
    text="1-10",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    934.0,
    364.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    809.0,
    797.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    301.0,
    798.0,
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
    fill="#000000",
    font=("Lexend Regular", 64 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    301.0,
    187.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    914.0,
    180.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    809.0,
    603.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    282.0,
    599.0,
    image=image_image_10
)

canvas.create_text(
    54.0,
    158.0,
    anchor="nw",
    text="Enter Patient Details",
    fill="#000000",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    667.0,
    151.0,
    anchor="nw",
    text="Medical History:",
    fill="#000000",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    608.0,
    574.0,
    anchor="nw",
    text="Dietary Information:",
    fill="#000000",
    font=("Lexend Regular", 40 * -1)
)

canvas.create_text(
    35.0,
    570.0,
    anchor="nw",
    text="Current Health Status:",
    fill="#000000",
    font=("Lexend Regular", 40 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    301.5,
    299.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=69.0,
    y=276.0,
    width=465.0,
    height=44.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1069.0,
    255.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=1023.0,
    y=234.0,
    width=92.0,
    height=40.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    338.0,
    690.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=292.0,
    y=669.0,
    width=92.0,
    height=40.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    110.0,
    405.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=69.0,
    y=382.0,
    width=82.0,
    height=44.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    110.0,
    492.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=69.0,
    y=469.0,
    width=82.0,
    height=44.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    970.0,
    311.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=929.0,
    y=288.0,
    width=82.0,
    height=44.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    856.5,
    913.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=762.0,
    y=894.0,
    width=189.0,
    height=37.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    343.0,
    747.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=302.0,
    y=724.0,
    width=82.0,
    height=44.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    449.0,
    831.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=408.0,
    y=808.0,
    width=82.0,
    height=44.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    916.0,
    468.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=680.0,
    y=444.0,
    width=472.0,
    height=46.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    856.5,
    826.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=754.0,
    y=802.0,
    width=205.0,
    height=46.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    370.0,
    898.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=340.0,
    y=874.0,
    width=60.0,
    height=46.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    1059.0,
    364.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=948.5,
    y=343.0,
    width=221.0,
    height=41.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    799.5,
    733.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=640.0,
    y=712.0,
    width=319.0,
    height=41.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    343.0,
    799.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=302.0,
    y=778.0,
    width=82.0,
    height=41.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    250.0,
    407.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=209.0,
    y=386.0,
    width=82.0,
    height=40.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    441.0,
    406.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=400.0,
    y=385.0,
    width=82.0,
    height=40.0
)

canvas.create_text(
    58.0,
    231.0,
    anchor="nw",
    text="Name:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    231.0,
    anchor="nw",
    text="Duration of Diabetes:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    623.0,
    670.0,
    anchor="nw",
    text="Recent Meals:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    45.0,
    667.0,
    anchor="nw",
    text="Glucose level:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    58.0,
    340.0,
    anchor="nw",
    text="Age:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    58.0,
    427.0,
    anchor="nw",
    text="Gender:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    279.0,
    anchor="nw",
    text="Diabetes Type:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    45.0,
    722.0,
    anchor="nw",
    text="HbA1c Levels:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    340.0,
    anchor="nw",
    text="Known Allergies:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    618.0,
    853.0,
    anchor="nw",
    text="Usual Dietary Habits:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    45.0,
    776.0,
    anchor="nw",
    text="Insulin Intake:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    47.0,
    827.0,
    anchor="nw",
    text="Time since last intake",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    397.0,
    anchor="nw",
    text="Other Medical Conditions:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    620.0,
    759.0,
    anchor="nw",
    text="Planned Sugary Food Intake:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    47.0,
    874.0,
    anchor="nw",
    text="Physical Activity:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    190.0,
    340.0,
    anchor="nw",
    text="Weight:",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    314.0,
    376.0,
    anchor="nw",
    text="kg",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1042.0,
    286.0,
    anchor="nw",
    text="1/2",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    422.0,
    709.0,
    anchor="nw",
    text="%",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    422.0,
    764.0,
    anchor="nw",
    text="ml",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    513.0,
    807.0,
    anchor="nw",
    text="hrs",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    185.0,
    469.0,
    anchor="nw",
    text="M/F",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    514.0,
    379.0,
    anchor="nw",
    text="cm",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    1137.0,
    231.0,
    anchor="nw",
    text="yrs",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    422.0,
    654.0,
    anchor="nw",
    text="mg/dL",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)

canvas.create_text(
    385.0,
    343.0,
    anchor="nw",
    text="Height:",
    fill="#2427F9",
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
    x=1229.0,
    y=334.0,
    width=190.0,
    height=52.0
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1222.0,
    602.0,
    image=image_image_11
)

canvas.create_text(
    1048.0,
    573.0,
    anchor="nw",
    text="Lifestyle Factors:",
    fill="#000000",
    font=("Lexend Regular", 40 * -1)
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    1294.5,
    686.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=1275.0,
    y=663.0,
    width=39.0,
    height=44.0
)

canvas.create_text(
    440.0,
    866.0,
    anchor="nw",
    text="1-10",
    fill="#2427F9",
    font=("Lexend Regular", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
