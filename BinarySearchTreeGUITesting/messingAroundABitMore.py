import tkinter as tk

# Function to handle radio button change and update color
def on_radio_change(selected_option):
    # Update the color of the clicked radio button
    for radio_button in radio_buttons:
        # Check if the radio button is the selected one
        if radio_button.cget('value') == selected_option.get():
            radio_button.config(
                foreground="red",  # Text color (white)
                background="yellow"  # Background color for selected option

            )
        else:
            radio_button.config(
                foreground="blue",  # Default text color
                background="yellow",  # Default background color
                activebackground="#44475A",  # Active background color
                activeforeground="#FF79C6",  # Active text color
                relief="flat"  # Keep the others flat for distinction
            )
    print(f"Selected option: {selected_option.get()}")

# Create the main window
window = tk.Tk()
window.title("Stylized Button Example")

# Create a Tkinter variable to store the selected option
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default option

# List of options for the radio buttons
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create an empty list to store the radio buttons
radio_buttons = []

# Create the radio buttons in a loop
for option in options:
    radio_button = tk.Radiobutton(window,
                                  text=option,
                                  variable=selected_option,
                                  value=option,
                                  indicator=0,  # Remove the round indicator
                                  command=lambda: on_radio_change(selected_option),  # Pass selected_option to the function
                                  font=("Helvetica", 12),
                                  padx=20, 
                                  )  # Active text color
    
    radio_button.pack(anchor="w", pady=5)
    radio_buttons.append(radio_button)

# Start the Tkinter main loop
window.mainloop()

