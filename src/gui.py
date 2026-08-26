import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from game import Game


class AdventureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Quest")
        self.root.geometry("1100x720")
        self.root.minsize(1000, 650)

        self.game = Game()

        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_dir = os.path.join(self.base_dir, "assets", "images")

        self.images = {}
        self.load_images()

        self.build_interface()
        self.update_interface()

    # -----------------------------
    # IMAGE HANDLING
    # -----------------------------

    def load_images(self):
        image_names = [
            "player",
            "village",
            "forest",
            "cave",
            "merchant",
            "old_man",
            "wolf",
            "goblin",
            "crystal"
        ]

        for name in image_names:
            path = os.path.join(self.image_dir, name + ".png")

            if os.path.exists(path):
                try:
                    self.images[name] = Image.open(path).convert("RGBA")
                except Exception as error:
                    print(f"Could not load {name}: {error}")
            else:
                print(f"Missing image: {path}")

    def get_image(self, name, width, height):
        if name not in self.images:
            return None

        image = self.images[name].copy()
        image.thumbnail((width, height), Image.Resampling.LANCZOS)

        canvas = Image.new("RGBA", (width, height), "#151515")

        x = (width - image.width) // 2
        y = (height - image.height) // 2

        canvas.alpha_composite(image, (x, y))

        return ImageTk.PhotoImage(canvas)

    # -----------------------------
    # MAIN INTERFACE
    # -----------------------------

    def build_interface(self):

        self.root.configure(bg="#171717")

        # TITLE
        title = tk.Label(
            self.root,
            text="⚔  ADVENTURE QUEST  ⚔",
            font=("Georgia", 28, "bold"),
            fg="#f4c542",
            bg="#171717"
        )

        title.pack(pady=(12, 8))

        # MAIN AREA
        main_frame = tk.Frame(
            self.root,
            bg="#171717"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        # LEFT SIDE
        self.game_frame = tk.Frame(
            main_frame,
            bg="#222222",
            bd=2,
            relief="ridge"
        )

        self.game_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # LOCATION LABEL
        self.location_label = tk.Label(
            self.game_frame,
            text="",
            font=("Georgia", 20, "bold"),
            fg="#f4c542",
            bg="#222222"
        )

        self.location_label.pack(pady=8)

        # GAME IMAGE
        self.scene_label = tk.Label(
            self.game_frame,
            bg="#111111",
            bd=2,
            relief="sunken"
        )

        self.scene_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # EVENT LABEL
        self.event_label = tk.Label(
            self.game_frame,
            text="Welcome to Adventure Quest!",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#222222",
            wraplength=600
        )

        self.event_label.pack(pady=8)

        # STORY
        self.story_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 12),
            fg="#dddddd",
            bg="#222222",
            wraplength=650,
            justify="center"
        )

        self.story_label.pack(
            pady=(0, 10)
        )

        # BUTTONS
        button_frame = tk.Frame(
            self.game_frame,
            bg="#222222"
        )

        button_frame.pack(pady=10)

        self.event_button = tk.Button(
            button_frame,
            text="⚔ Trigger Event",
            font=("Arial", 12, "bold"),
            bg="#8b4513",
            fg="white",
            activebackground="#b5651d",
            activeforeground="white",
            width=18,
            command=self.trigger_event
        )

        self.event_button.grid(
            row=0,
            column=0,
            padx=5
        )

        self.restart_button = tk.Button(
            button_frame,
            text="↻ Restart",
            font=("Arial", 12, "bold"),
            bg="#333333",
            fg="white",
            width=12,
            command=self.restart
        )

        self.restart_button.grid(
            row=0,
            column=1,
            padx=5
        )

        # RIGHT SIDE
        self.side_frame = tk.Frame(
            main_frame,
            width=300,
            bg="#252525",
            bd=2,
            relief="ridge"
        )

        self.side_frame.pack(
            side="right",
            fill="y"
        )

        self.side_frame.pack_propagate(False)

        # PLAYER TITLE
        tk.Label(
            self.side_frame,
            text="PLAYER",
            font=("Georgia", 18, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(pady=10)

        # PLAYER IMAGE
        self.player_image_label = tk.Label(
            self.side_frame,
            bg="#252525"
        )

        self.player_image_label.pack(pady=5)

        # STATUS
        self.status_label = tk.Label(
            self.side_frame,
            text="",
            font=("Arial", 12),
            fg="white",
            bg="#252525",
            justify="left"
        )

        self.status_label.pack(
            pady=10,
            padx=10
        )

        # LOCATION TITLE
        tk.Label(
            self.side_frame,
            text="LOCATION",
            font=("Georgia", 17, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(pady=(15, 8))

        # LOCATION BUTTONS
        locations = [
            ("🏘 Village", "Village"),
            ("🌲 Forest", "Forest"),
            ("⛰ Cave", "Cave")
        ]

        for text, location in locations:

            button = tk.Button(
                self.side_frame,
                text=text,
                font=("Arial", 12, "bold"),
                bg="#333333",
                fg="white",
                activebackground="#555555",
                width=22,
                command=lambda loc=location: self.move(loc)
            )

            button.pack(
                pady=4,
                padx=15
            )

        # MISSION
        tk.Label(
            self.side_frame,
            text="MISSION",
            font=("Georgia", 16, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(pady=(20, 5))

        tk.Label(
            self.side_frame,
            text="Find the Ancient Crystal\nand complete your adventure.",
            font=("Arial", 10),
            fg="#dddddd",
            bg="#252525",
            justify="center"
        ).pack()

    # -----------------------------
    # GAME FUNCTIONS
    # -----------------------------

    def move(self, location):

        self.game.player.location = location

        self.event_label.config(
            text=f"You arrived at the {location}."
        )

        self.story_label.config(
            text="Explore this area and trigger an event."
        )

        self.update_interface()

    def trigger_event(self):

        if not self.game.player.is_alive():

            messagebox.showinfo(
                "Game Over",
                "Your health has reached zero.\nRestart the game."
            )

            return

        name, result = self.game.next_event()

        self.event_label.config(
            text=f"⚔ {name}"
        )

        self.story_label.config(
            text=result
        )

        self.show_event_image(name)
        self.update_interface()

        # Crystal ending
        if self.game.player.crystal:

            messagebox.showinfo(
                "Adventure Complete!",
                "You found the Ancient Crystal!\n\n"
                "Congratulations, Adventurer!"
            )

        # Death ending
        elif not self.game.player.is_alive():

            messagebox.showinfo(
                "Game Over",
                "You were defeated.\n\n"
                "Try again!"
            )

    # -----------------------------
    # DISPLAY EVENT IMAGE
    # -----------------------------

    def show_event_image(self, event_name):

        image_map = {
            "Merchant": "merchant",
            "Old Man": "old_man",
            "Wolf Attack": "wolf",
            "Hidden Treasure": "crystal",
            "Lost Traveler": "old_man",
            "Goblin Battle": "goblin",
            "Ancient Crystal": "crystal",
            "Final Guardian": "goblin"
        }

        image_name = image_map.get(event_name)

        if image_name:

            photo = self.get_image(
                image_name,
                650,
                300
            )

            if photo:

                self.scene_label.config(
                    image=photo
                )

                self.scene_label.image = photo

                return

        self.show_location_image()

    # -----------------------------
    # LOCATION IMAGE
    # -----------------------------

    def show_location_image(self):

        location_map = {
            "Village": "village",
            "Forest": "forest",
            "Cave": "cave"
        }

        image_name = location_map.get(
            self.game.player.location,
            "village"
        )

        photo = self.get_image(
            image_name,
            650,
            300
        )

        if photo:

            self.scene_label.config(
                image=photo
            )

            self.scene_label.image = photo

    # -----------------------------
    # UPDATE SCREEN
    # -----------------------------

    def update_interface(self):

        player = self.game.player

        self.location_label.config(
            text=f"📍 {player.location}"
        )

        status = (
            f"❤️ Health: {player.health}/100\n\n"
            f"💰 Gold: {player.gold}\n\n"
            f"⚔ Weapon: "
            f"{'Yes' if player.weapon else 'No'}\n\n"
            f"⭐ Reputation: {player.reputation}"
        )

        self.status_label.config(
            text=status
        )

        # Player image
        player_photo = self.get_image(
            "player",
            180,
            190
        )

        if player_photo:

            self.player_image_label.config(
                image=player_photo
            )

            self.player_image_label.image = player_photo

        # Location image
        self.show_location_image()

    # -----------------------------
    # RESTART
    # -----------------------------

    def restart(self):

        self.game = Game()

        self.event_label.config(
            text="Welcome back, Adventurer!"
        )

        self.story_label.config(
            text=(
                "Your mission is to find the Ancient Crystal.\n"
                "Choose a location and explore."
            )
        )

        self.update_interface()