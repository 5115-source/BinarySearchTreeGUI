import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
         # Set background color for the window
        self.root.config(bg="pink")  # You can change "lightblue" to any color you like
        
        # Generate a random number between 1 and 100
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        
        # Create GUI components
        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 100:", font=('Helvetica', 12))
        self.instruction_label.pack(pady=10)
        
        self.input_box = tk.Entry(root, font=('Helvetica', 14))
        self.input_box.pack(pady=10)
        
        self.guess_button = tk.Button(root, text="Guess", font=('Helvetica', 14), command=self.check_guess)
        self.guess_button.pack(pady=10)
        
        self.feedback_label = tk.Label(root, text="", font=('Helvetica', 12))
        self.feedback_label.pack(pady=10)
    
    def check_guess(self):
        try:
            # Get the guess from the input box
            user_guess = int(self.input_box.get())
            self.guess_count += 1
            
            if user_guess < self.target_number:
                self.feedback_label.config(text="Too low! Try again.", fg="red")
            elif user_guess > self.target_number:
                self.feedback_label.config(text="Too high! Try again.", fg="red")
            else:
                self.feedback_label.config(text=f"Correct! You guessed it in {self.guess_count} tries.", fg="green")
                self.ask_play_again()
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")
    
    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again", "You guessed the number! Would you like to play again?")
        if play_again:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.feedback_label.config(text="")
        self.input_box.delete(0, tk.END)

# Main program to start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
