import random
import tkinter as tk

class RockPaperScissorsGame:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Rock, Paper, Scissors")

        # Top Frame (Computer's side)
        self.top_frame = tk.Frame(self.master, width=400, height=150, bg="light blue")
        self.top_frame.pack_propagate(False)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.computer_label = tk.Label(self.top_frame, text="Computer", font=("Helvetica", 20), bg="light blue")
        self.computer_label.pack(pady=5)
        self.computer_choice_label = tk.Label(self.top_frame, text="", font=("Helvetica", 12), bg="light blue")
        self.computer_choice_label.pack(pady=5)
        self.computer_score_label = tk.Label(self.top_frame, text="Score: 0", font=("Helvetica", 12), bg="light blue")
        self.computer_score_label.pack(pady=5, padx=10, side=tk.LEFT)

        # Result Frame
        self.result_frame = tk.Frame(self.master, width=400, height=50, bg="white")
        self.result_frame.pack_propagate(False)
        self.result_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.result_label = tk.Label(self.result_frame, text="", font=("Helvetica", 14), bg="white")
        self.result_label.pack(pady=5)

        # Bottom Frame (User's side)
        self.bottom_frame = tk.Frame(self.master, width=400, height=150, bg="light pink")
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.user_label = tk.Label(self.bottom_frame, text="USER", font=("Helvetica", 20), bg="light pink")
        self.user_label.pack(pady=5)
        self.user_choice_label = tk.Label(self.bottom_frame, text="", font=("Helvetica", 12), bg="light pink")
        self.user_choice_label.pack(pady=5)
        self.user_score_label = tk.Label(self.bottom_frame, text="Score: 0", font=("Helvetica", 12), bg="light pink")
        self.user_score_label.pack(pady=5, padx=10, side=tk.LEFT)

        # Button Frame
        self.button_frame = tk.Frame(self.master, width=400, height=100, bg="white")
        self.button_frame.pack_propagate(False)
        self.button_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # Creating buttons with larger size
        self.rock_button = tk.Button(self.button_frame, text="Rock", width=12, height=3, command=lambda: self.play_game("rock"), bg="white")
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=12, height=3, command=lambda: self.play_game("paper"), bg="white")
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=12, height=3, command=lambda: self.play_game("scissors"), bg="white")
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

         # Bottom Button Frame
        self.bottom_button_frame = tk.Frame(self.master, width=400, height=50, bg="white")
        self.bottom_button_frame.pack_propagate(False)
        self.bottom_button_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.restart_button = tk.Button(self.bottom_button_frame, text="Restart", width=10, command=self.reset, bg="white")
        self.restart_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.quit_button = tk.Button(self.bottom_button_frame, text="Exit", width=10, command=self.master.destroy, bg="white")
        self.quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Adding hover effects to buttons
        self.add_hover_effect(self.rock_button)
        self.add_hover_effect(self.paper_button)
        self.add_hover_effect(self.scissors_button)
        self.add_hover_effect(self.restart_button)
        self.add_hover_effect(self.quit_button)

        self.user_score = 0
        self.computer_score = 0

    def add_hover_effect(self, button):
        button.bind("<Enter>", lambda e: button.config(bg="light gray"))
        button.bind("<Leave>", lambda e: button.config(bg="white"))

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.user_choice_label.config(text=f"{user_choice}")
        self.computer_choice_label.config(text=f"{computer_choice}")
        self.user_score_label.config(text=f"Score: {self.user_score}")
        self.computer_score_label.config(text=f"Score: {self.computer_score}")
        self.result_label.config(text=result)

    def reset(self):
        self.result_label.config(text="")
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="Score: 0")
        self.computer_score_label.config(text="Score: 0")

def main():
    app = RockPaperScissorsGame()
    app.master.mainloop()

if __name__ == "__main__":
    main()