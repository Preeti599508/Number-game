import tkinter as tk
import random

def start_bet():
    global available_balance, bet_amount, bet_entry
    try:
        bet_amount = int(bet_entry.get())
        if bet_amount <= 0:
            raise ValueError
        if bet_amount < 100:
            raise ValueError("Bet amount must be at least 100 rupees.")
        if available_balance >= bet_amount:
            result = simulate_game()
            if result == "win":
                available_balance += bet_amount
                balance_label.config(text=f"Available balance {available_balance}")
                bet_entry.delete(0, tk.END)
                result_label.config(text="You Win!")
            else:
                available_balance -= bet_amount
                balance_label.config(text=f"Available Balance {available_balance}")
                bet_entry.delete(0, tk.END)
                result_label.config(text="You Lose! ")
                if available_balance == 0:
                    bet_button.config(state=tk.DISABLED)
                    result_label.config(text="Game Over!")
        else:
            result_label.config(text="Insufficient Balance!")
    except ValueError as e:
        result_label.config(text=str(e))

def simulate_game():
    # Replace this with your actual game logic
    # For example, you could use random numbers to determine a win or loss
    return "win" if random.random() > 0.5 else "lose"

# Initialize variables
available_balance = 500
bet_amount = 100

# Create the main window
window = tk.Tk()
window.title("Betting Game")

# Create labels, entry, and buttons
balance_label = tk.Label(window, text=f"Available balance {available_balance}", font=("Arial", 30))
balance_label.pack()

label2=tk.Label(window,text="The Bet Should Be Started From Rupees 100",font=('Times',20))
label2.pack()

bet_entry = tk.Entry(window, font=("Arial", 12))
bet_entry.pack()

bet_button = tk.Button(window, text="Bet", command=start_bet, font=("Arial", 12))
bet_button.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

# Start the main loop
window.mainloop()