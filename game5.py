import tkinter as tk
import random

def start_bet():
    global available_balance, bet_amount, bet_entry, guess_entry, attempts, computer_number
    try:
        # Get the bet amount from the user
        bet_amount = int(bet_entry.get())
        if bet_amount <= 0:
            raise ValueError
        if bet_amount < 100:
            raise ValueError("Bet amount must be at least 100 rupees.")
        if available_balance >= bet_amount:
            # Deduct the bet amount from available balance
            available_balance -= bet_amount
            balance_label.config(text=f"Available Balance: {available_balance}")
            
            # Initialize the number of attempts and computer's random number
            attempts = 3
            computer_number = random.randint(1, 10)  # Random number between 1 and 10
            result_label.config(text=f"You have {attempts} attempts to guess the number between 1 and 10.")
            guess_button.config(state=tk.NORMAL)
            bet_button.config(state=tk.DISABLED)  # Disable the bet button while guessing
            guess_entry.delete(0, tk.END)
            guess_entry.focus()  # Focus on the guess entry
        else:
            result_label.config(text="Insufficient Balance!")
    except ValueError as e:
        result_label.config(text=str(e))

def guess_number():
    global available_balance, attempts, bet_amount
    try:
        user_guess = int(guess_entry.get())
        if user_guess < 1 or user_guess > 10:
            raise ValueError("Please guess a number between 1 and 10.")
        
        if attempts > 0:
            if user_guess == computer_number:
                available_balance += bet_amount * 2  # Win: Add double the bet amount
                result_label.config(text=f"You Win! The number was {computer_number}. Your new balance: {available_balance}.")
                guess_button.config(state=tk.DISABLED)  # Disable guessing after winning
                bet_button.config(state=tk.NORMAL)  # Enable betting again
            else:
                attempts -= 1
                if attempts > 0:
                    result_label.config(text=f"Wrong guess! You have {attempts} attempts left.")
                else:
                    result_label.config(text=f"You Lose! The number was {computer_number}. Your new balance: {available_balance}.")
                    bet_button.config(state=tk.NORMAL)  # Enable betting again
                    guess_button.config(state=tk.DISABLED)  # Disable guessing after losing
        guess_entry.delete(0, tk.END)  # Clear the guess entry
    except ValueError as e:
        result_label.config(text=str(e))

# Initialize variables
available_balance = 500
bet_amount = 100
attempts = 0
computer_number = 0

# Create the main window
window = tk.Tk()
window.title("Betting Game")

# Create labels, entry, and buttons
balance_label = tk.Label(window, text=f"Available Balance: {available_balance}", font=("Arial", 30))
balance_label.pack()

label2 = tk.Label(window, text="The Bet Should Be Started From Rupees 100", font=('Times', 20))
label2.pack()

bet_entry = tk.Entry(window, font=("Arial", 12))
bet_entry.pack()

label3 = tk.Label(window, text="Guess a number between 1 and 10:", font=("Arial", 14))
label3.pack()

guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack()

bet_button = tk.Button(window, text="Bet", command=start_bet, font=("Arial", 12))
bet_button.pack()

guess_button = tk.Button(window, text="Guess", command=guess_number, font=("Arial", 12), state=tk.DISABLED)
guess_button.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

# Start the main loop
window.mainloop()
