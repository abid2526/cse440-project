import tkinter as tk

from gui import AdventureGUI


def main():
    root = tk.Tk()
    AdventureGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()