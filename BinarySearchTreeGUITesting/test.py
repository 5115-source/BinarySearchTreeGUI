import tkinter as tk

def change_color():
    # Update the background color of all radio buttons based on the selected one
    for radio_button in radio_buttons:
        if radio_button_var.get() == radio_button['value']:
            radio_button.config(bg="lightblue")
        else:
            radio_button.config(bg="white")

root = tk.Tk()
root.title("Radio Buttons with Color Change")

# Create a variable to hold the value of the selected radio button
radio_button_var = tk.IntVar()

# List of radio button values and their labels
options = [("Option 1", 1), ("Option 2", 2), ("Option 3", 3)]

# Create the radio buttons and add them to the window
radio_buttons = []
for text, value in options:
    radio_button = tk.Radiobutton(root, text=text, variable=radio_button_var, value=value,
                                  command=change_color, width=20, height=2)
    radio_button.pack(pady=5)
    radio_buttons.append(radio_button)

root.mainloop()
