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
    y_labels = [36.0, 36.5, 37.0, 37.5, 38.0]
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


# Create Tkinter window
window = Tk()
window.geometry("1200x900")
canvas = Canvas(window, bg="#171821", height=900, width=1200)
canvas.pack()

# Create the rectangle background
canvas.create_rectangle(972.0, 644.0, 1158.0, 841.0, fill="#393A4A", outline="")

# Call the function to draw the wave graph on top of the rectangle
draw_wave_graph(canvas)

window.mainloop()
