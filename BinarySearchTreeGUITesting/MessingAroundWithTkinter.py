import tkinter as tk
import tkinter.ttk as ttk

from tkinter import *

def on_button_click():
    print("Button clicked!")
    

def on_radio_change(selected_option):
    print(f"Selected: {selected_option.get()}")

def main():
    
    window = tk.Tk()
    
    window.title("Stylized Button Example")
    
     # Create a Tkinter variable to store the selected option
    selected_option = tk.StringVar()
    selected_option.set("Option 1")  # Set default option

    # List of options for the radio buttons
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]

    # Create the radio buttons in a loop
    for option in options:
        radio_button = tk.Radiobutton(window,
                                      text=option,
                                      variable=selected_option,
                                      value=option,
                                      indicator=0,
                                      command=lambda: on_radio_change(selected_option),  # Pass selected_option to the function
                                      font=("Helvetica", 12),
                                      padx=20, 
                                      foreground="#F8F8F2", 
                                      background="#282A36", 
                                      activebackground="#44475A", 
                                      activeforeground="#FF79C6")
        
        radio_button.pack(anchor="w")
    
    # Start the event loop
    window.mainloop()
    
    """greeting = ttk.Label(text="Hello, Tkinter")
    greeting.pack()
    
    label = tk.Label(text="Hello, Tkinter", foreground="#F8F8F2", background="#282A36")
    label.pack()"""
    
    label = tk.Label(
    text="Hello, Tkinter",
    fg="#F8F8F2",
    bg="#282A36",
    width=100,
    height=100
)
    
    button = ttk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow")
    button.pack()
    label.pack()
    
    window.mainloop()  # Starts the event loop
    
#If there is a main method, run it
if __name__ == "__main__":
    main()
