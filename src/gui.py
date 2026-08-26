import tkinter as tk
from tkinter import messagebox

from game import Game


class AdventureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Quest")
        self.root.geometry("700x500")

        self.game = Game()

        title = tk.Label(
            root,
            text="ADVENTURE QUEST",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        self.story = tk.Text(
            root,
            height=12,
            width=75,
            state="disabled"
        )
        self.story.pack(pady=10)

        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Village",
            width=12,
            command=lambda: self.move("Village")
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Forest",
            width=12,
            command=lambda: self.move("Forest")
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Cave",
            width=12,
            command=lambda: self.move("Cave")
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            root,
            text="Trigger Event",
            width=20,
            command=self.trigger_event
        ).pack(pady=10)

        tk.Button(
            root,
            text="Restart",
            width=20,
            command=self.restart
        ).pack()

        self.write(
            "Welcome to Adventure Quest!\n\n"
            "Your mission is to find the Ancient Crystal.\n"
            "Choose a location and trigger an event."
        )

        self.update_status()

    def write(self, text):
        self.story.config(state="normal")
        self.story.delete("1.0", tk.END)
        self.story.insert(tk.END, text)
        self.story.config(state="disabled")

    def update_status(self):
        self.status_label.config(
            text=self.game.player.status()
        )

    def move(self, location):
        self.game.player.location = location

        self.write(
            f"You traveled to the {location}.\n\n"
            "Click 'Trigger Event' to continue."
        )

        self.update_status()

    def trigger_event(self):
        if not self.game.player.is_alive():
            messagebox.showinfo(
                "Game Over",
                "You have no health left. Restart the game."
            )
            return

        name, result = self.game.next_event()

        self.write(
            f"EVENT: {name}\n\n"
            f"{result}"
        )

        self.update_status()

        if self.game.player.crystal:
            messagebox.showinfo(
                "Adventure Complete",
                "You obtained the Ancient Crystal!\n"
                "Congratulations!"
            )

        elif not self.game.player.is_alive():
            messagebox.showinfo(
                "Game Over",
                "Your health reached zero."
            )

    def restart(self):
        self.game = Game()

        self.write(
            "Game restarted.\n\n"
            "Your mission is to find the Ancient Crystal."
        )

        self.update_status()