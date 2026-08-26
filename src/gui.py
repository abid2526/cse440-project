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

        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.image_dir = os.path.join(
            self.base_dir,
            "assets",
            "images"
        )

        self.images = {}

        self.choice_frame = None

        self.load_images()
        self.build_interface()
        self.update_interface()

    # =========================================================
    # IMAGE HANDLING
    # =========================================================

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

            path = os.path.join(
                self.image_dir,
                name + ".png"
            )

            if os.path.exists(path):

                try:
                    self.images[name] = Image.open(
                        path
                    ).convert("RGBA")

                except Exception as error:

                    print(
                        f"Could not load {name}: {error}"
                    )

            else:

                print(
                    f"Missing image: {path}"
                )

    def get_image(self, name, width, height):

        if name not in self.images:
            return None

        image = self.images[name].copy()

        image.thumbnail(
            (width, height),
            Image.Resampling.LANCZOS
        )

        canvas = Image.new(
            "RGBA",
            (width, height),
            "#151515"
        )

        x = (width - image.width) // 2
        y = (height - image.height) // 2

        canvas.alpha_composite(
            image,
            (x, y)
        )

        return ImageTk.PhotoImage(canvas)

    # =========================================================
    # MAIN INTERFACE
    # =========================================================

    def build_interface(self):

        self.root.configure(
            bg="#171717"
        )

        # -----------------------------------------------------
        # TITLE
        # -----------------------------------------------------

        title = tk.Label(
            self.root,
            text="⚔  ADVENTURE QUEST  ⚔",
            font=("Menlo", 28, "bold"),
            fg="#f4c542",
            bg="#171717"
        )

        title.pack(
            pady=(12, 8)
        )

        # -----------------------------------------------------
        # MAIN AREA
        # -----------------------------------------------------

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

        # =====================================================
        # LEFT GAME AREA
        # =====================================================

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

        # -----------------------------------------------------
        # LOCATION
        # -----------------------------------------------------

        self.location_label = tk.Label(
            self.game_frame,
            text="",
            font=("Menlo", 20, "bold"),
            fg="#f4c542",
            bg="#222222"
        )

        self.location_label.pack(
            pady=8
        )

        # -----------------------------------------------------
        # SCENE IMAGE
        # -----------------------------------------------------

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

        # -----------------------------------------------------
        # EVENT TITLE
        # -----------------------------------------------------

        self.event_label = tk.Label(
            self.game_frame,
            text="Welcome to Adventure Quest!",
            font=("Menlo", 25, "bold"),
            fg="#f4c542",
            bg="#222222",
            wraplength=650,
            justify="center",
            anchor="center"
        )

        self.event_label.pack(
            pady=(12, 5),
            padx=20,
            fill="x"
        )

        # -----------------------------------------------------
        # STORY
        # -----------------------------------------------------

        self.story_label = tk.Label(
            self.game_frame,
            text="",
            font=("Menlo", 15),
            fg="#ffffff",
            bg="#222222",
            wraplength=700,
            justify="center",
            anchor="center"
        )

        self.story_label.pack(
            pady=(5, 15),
            padx=20,
            fill="x"
        )

        # -----------------------------------------------------
        # MAIN BUTTONS
        # -----------------------------------------------------

        button_frame = tk.Frame(
            self.game_frame,
            bg="#222222"
        )

        button_frame.pack(
            pady=10
        )

        # TRIGGER EVENT

        self.event_button = tk.Button(
            button_frame,
            text="⚔ Trigger Event",
            font=("Menlo", 15, "bold"),
            bg="#8b4513",
            fg="black",
            activebackground="#b5651d",
            activeforeground="black",
            width=24,
            height=3,
            cursor="hand2",
            relief="raised",
            bd=4,
            command=self.trigger_event
        )

        self.event_button.grid(
            row=0,
            column=0,
            padx=5
        )

        # RESTART

        self.restart_button = tk.Button(
            button_frame,
            text="↻ Restart",
            font=("Menlo", 15, "bold"),
            bg="#444444",
            fg="black",
            activebackground="#666666",
            activeforeground="black",
            width=18,
            height=3,
            cursor="hand2",
            relief="raised",
            bd=4,
            command=self.restart
        )

        self.restart_button.grid(
            row=0,
            column=1,
            padx=5
        )

        # =====================================================
        # RIGHT SIDE
        # =====================================================

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

        self.side_frame.pack_propagate(
            False
        )

        # -----------------------------------------------------
        # PLAYER TITLE
        # -----------------------------------------------------

        tk.Label(
            self.side_frame,
            text="PLAYER",
            font=("Menlo", 18, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(
            pady=10
        )

        # -----------------------------------------------------
        # PLAYER IMAGE
        # -----------------------------------------------------

        self.player_image_label = tk.Label(
            self.side_frame,
            bg="#252525"
        )

        self.player_image_label.pack(
            pady=5
        )

        # -----------------------------------------------------
        # PLAYER STATUS
        # -----------------------------------------------------

        self.status_label = tk.Label(
            self.side_frame,
            text="",
            font=("Menlo", 12),
            fg="white",
            bg="#252525",
            justify="left"
        )

        self.status_label.pack(
            pady=10,
            padx=10
        )

        # -----------------------------------------------------
        # LOCATION TITLE
        # -----------------------------------------------------

        tk.Label(
            self.side_frame,
            text="LOCATION",
            font=("Menlo", 17, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(
            pady=(15, 8)
        )

        # -----------------------------------------------------
        # LOCATION BUTTONS
        # -----------------------------------------------------

        locations = [
            ("🏘 Village", "Village"),
            ("🌲 Forest", "Forest"),
            ("⛰ Cave", "Cave")
        ]

        for text, location in locations:

            button = tk.Button(
                self.side_frame,
                text=text,
                font=("Menlo", 15, "bold"),
                bg="#333333",
                fg="black",
                activebackground="#555555",
                activeforeground="black",
                width=24,
                height=3,
                cursor="hand2",
                relief="raised",
                bd=4,
                command=lambda loc=location: self.move(loc)
            )

            button.pack(
                pady=4,
                padx=15
            )

        # -----------------------------------------------------
        # MISSION
        # -----------------------------------------------------

        tk.Label(
            self.side_frame,
            text="MISSION",
            font=("Menlo", 16, "bold"),
            fg="#f4c542",
            bg="#252525"
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            self.side_frame,
            text=(
                "Find the Ancient Crystal\n"
                "and complete your adventure."
            ),
            font=("Menlo", 13),
            fg="#e0dada",
            bg="#252525",
            justify="center"
        ).pack()

    # =========================================================
    # LOCATION
    # =========================================================

    def move(self, location):

        self.game.player.location = location

        self.clear_choices()

        self.event_label.config(
            text=f"You arrived at the {location}."
        )

        self.story_label.config(
            text=(
                "Explore this area and "
                "trigger an event."
            )
        )

        self.update_interface()

    # =========================================================
    # TRIGGER EVENT
    # =========================================================

    def trigger_event(self):

        if not self.game.player.is_alive():

            messagebox.showinfo(
                "Game Over",
                "Your health has reached zero.\n"
                "Restart the game."
            )

            return

        self.clear_choices()

        event = self.game.next_event()

        # -----------------------------------------------------
        # SUPPORT FOR DICTIONARY-BASED EVENTS
        # -----------------------------------------------------

        if isinstance(event, dict):

            title = event.get(
                "title",
                "EVENT"
            )

            description = event.get(
                "description",
                ""
            )

            choices = event.get(
                "choices",
                []
            )

            self.event_label.config(
                text=title
            )

            self.story_label.config(
                text=description
            )

            self.show_event_image(
                title
            )

            if choices:
                self.show_choices(
                    choices
                )

            self.update_interface()

            return

        # -----------------------------------------------------
        # EXISTING NAME/RESULT EVENTS
        # -----------------------------------------------------

        if isinstance(event, tuple):

            name, result = event

            self.event_label.config(
                text=f"⚔ {name}"
            )

            self.story_label.config(
                text=result
            )

            self.show_event_image(
                name
            )

            self.update_interface()

            self.check_game_end()

    # =========================================================
    # FOREST CHOICES
    # =========================================================

    def show_choices(self, choices):

        self.clear_choices()

        self.choice_frame = tk.Frame(
            self.game_frame,
            bg="#222222"
        )

        self.choice_frame.pack(
            pady=10
        )

        for text, action in choices:

            button = tk.Button(
                self.choice_frame,
                text=text,
                font=("Menlo", 13, "bold"),
                bg="#333333",
                fg="black",
                activebackground="#555555",
                activeforeground="black",
                width=16,
                height=2,
                cursor="hand2",
                relief="raised",
                bd=4,
                command=lambda a=action:
                    self.execute_choice(a)
            )

            button.pack(
                side="left",
                padx=8
            )

    def clear_choices(self):

        if self.choice_frame is not None:

            self.choice_frame.destroy()

            self.choice_frame = None

    # =========================================================
    # EXECUTE PLAYER CHOICE
    # =========================================================

    def execute_choice(self, action):

        player = self.game.player

        # -----------------------------------------------------
        # WOLF
        # -----------------------------------------------------

        if action == "wolf_fight":

            if player.weapon:

                player.health -= 10
                player.gold += 15

                result = (
                    "You fought the wolf and "
                    "defeated it!\n\n"
                    "You lost 10 health but "
                    "gained 15 gold."
                )

            else:

                player.health -= 40

                result = (
                    "You fought the wolf without "
                    "a weapon.\n\n"
                    "You were badly injured and "
                    "lost 40 health."
                )

        elif action == "wolf_run":

            player.health -= 5

            result = (
                "You escaped from the wolf.\n\n"
                "You lost 5 health while "
                "running away."
            )

        # -----------------------------------------------------
        # LOST TRAVELER
        # -----------------------------------------------------

        elif action == "traveler_help":

            player.reputation += 1
            player.gold += 15

            result = (
                "You helped the lost traveler.\n\n"
                "Your reputation increased "
                "and you received 15 gold."
            )

        elif action == "traveler_ignore":

            player.reputation -= 1

            result = (
                "You ignored the traveler.\n\n"
                "Your reputation decreased."
            )

        # -----------------------------------------------------
        # HIDDEN TREASURE
        # -----------------------------------------------------

        elif action == "treasure_search":

            player.gold += 30

            result = (
                "You searched the hidden area "
                "and found 30 gold!"
            )

        elif action == "treasure_leave":

            result = (
                "You decided to leave the "
                "treasure behind."
            )

        else:

            result = (
                "You made your choice."
            )

        # -----------------------------------------------------
        # SHOW RESULT
        # -----------------------------------------------------

        self.clear_choices()

        self.event_label.config(
            text="EVENT RESULT"
        )

        self.story_label.config(
            text=result
        )

        self.update_interface()

        self.check_game_end()

    # =========================================================
    # GAME END CHECK
    # =========================================================

    def check_game_end(self):

        if self.game.player.crystal:

            messagebox.showinfo(
                "Adventure Complete!",
                "You found the Ancient Crystal!\n\n"
                "Congratulations, Adventurer!"
            )

        elif not self.game.player.is_alive():

            messagebox.showinfo(
                "Game Over",
                "You were defeated.\n\n"
                "Try again!"
            )

    # =========================================================
    # EVENT IMAGE
    # =========================================================

    def show_event_image(self, event_name):

        image_map = {
            "Merchant": "merchant",
            "Old Man": "old_man",
            "Wolf Attack": "wolf",
            "🐺 WOLF ATTACK": "wolf",
            "Lost Traveler": "old_man",
            "🧑 LOST TRAVELER": "old_man",
            "Hidden Treasure": "crystal",
            "💰 HIDDEN TREASURE": "crystal",
            "Goblin Battle": "goblin",
            "Ancient Crystal": "crystal",
            "Final Guardian": "goblin"
        }

        image_name = image_map.get(
            event_name
        )

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

    # =========================================================
    # LOCATION IMAGE
    # =========================================================

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

    # =========================================================
    # UPDATE_SCREEN
    # =========================================================

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
            f"⭐ Reputation: "
            f"{player.reputation}"
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

    # =========================================================
    # RESTART
    # =========================================================

    def restart(self):

        self.game = Game()

        self.clear_choices()

        self.event_label.config(
            text="Welcome back, Adventurer!"
        )

        self.story_label.config(
            text=(
                "Your mission is to find "
                "the Ancient Crystal.\n"
                "Choose a location and explore."
            )
        )

        self.update_interface()