import tkinter as tk
import random

class CoinTossApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coin Toss")
        self.result = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Coin Toss", font=("Arial", 16))
        title_label.pack(pady=10)

        toss_button = tk.Button(self, text="Toss Coin", command=self.coin_toss)
        toss_button.pack(pady=10)

        result_label = tk.Label(self, textvariable=self.result, font=("Arial", 14))
        result_label.pack(pady=10)

        self.result.set("Click 'Toss Coin' to begin.")

    def coin_toss(self):
        outcomes = ['Heads', 'Tails']
        result = random.choice(outcomes)
        self.result.set(result)

# Create the application instance
app = CoinTossApp()

# Start the GUI event loop
app.mainloop()
