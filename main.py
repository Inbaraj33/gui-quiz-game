# main.py
import tkinter as tk
from quiz_app import QuizGameApp

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()