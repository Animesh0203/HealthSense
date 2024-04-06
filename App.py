import csv
from tkinter import Tk, Canvas, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def read_last_row(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    return rows[-1]


def main():
    window = Tk()
    window.geometry("700x550")
    window.configure(bg="#110E0E")

    canvas = Canvas(
        window,
        bg="#110E0E",
        height=550,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        53.0,
        fill="#CAC8C8",
        outline=""
    )

    canvas.create_text(
        12.0,
        10.0,
        anchor="nw",
        text="Physical Activity & Ambience Tracker",
        fill="#000000",
        font=("K2D Regular", 24 * -1)
    )

    # Load images
    image_names = ["image_1.png", "image_2.png", "image_3.png", "image_4.png", "image_5.png", "image_6.png"]
    image_objects = []
    for i, name in enumerate(image_names):
        image = PhotoImage(file=relative_to_assets(name))
        image_objects.append(image)
        canvas.create_image(
            113.0 + i * 237,
            119.0 if i < 3 else 169.0,
            image=image
        )

    canvas.create_text(
        68.0,
        206.0,
        anchor="nw",
        text="Steps",
        fill="#F2F2F2",
        font=("K2D Regular", 13 * -1)
    )

    canvas.create_text(
        305.0,
        206.0,
        anchor="nw",
        text="Temperature",
        fill="#F2F2F2",
        font=("K2D Regular", 13 * -1)
    )

    canvas.create_text(
        542.0,
        206.0,
        anchor="nw",
        text="Humidity",
        fill="#F2F2F2",
        font=("K2D Regular", 13 * -1)
    )

    def update_data():
        csv_data = read_last_row("data.csv")

        # X positions of labels
        label_x_positions = {
            "Steps": 95.0,
            "Temperature": 1000000.0,
            "Humidity": 569.0
        }

        # Y positions of labels
        label_y_positions = {
            "Steps": 92.0,
            "Temperature": 206.0,
            "Humidity": 206.0
        }

        # Calculate y position of each data element
        y_offsets = {
            "Steps": 0,
            "Temperature": 1000,
            "Humidity": 100
        }

        for j, (label, value) in enumerate(zip(["Steps", "Temperature", "Humidity"], csv_data)):
            canvas.create_text(
                label_x_positions[label],  # X position based on the label's position
                label_y_positions[label] + y_offsets[label],  # Y position based on the label's position and offset
                anchor="nw",
                text=value,
                fill="#FFFFFF",
                font=("ArialMT", 16 * -1)
            )

        window.after(5000, update_data)

    update_data()

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
