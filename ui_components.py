
# ui_components.py
import tkinter as tk
from tkinter import ttk

class UIComponents:
    def __init__(self, root):
        self.root = root
        self.main_frame = None
        self.question_label = None
        self.answer_buttons = []
        self.next_button = None
        self.results_button = None
        self.progress_bar = None
    
    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def create_question_label(self):
        self.question_label = ttk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", 14, "bold"),
            wraplength=700
        )
        self.question_label.pack(pady=20)
    
    def create_answer_buttons(self, selected_var):
        self.answer_frame = ttk.Frame(self.main_frame)
        self.answer_frame.pack(pady=20)
        
        for i in range(4):
            btn = ttk.Radiobutton(
                self.answer_frame,
                text="",
                variable=selected_var,
                value=""
            )
            btn.pack(anchor=tk.W, pady=5)
            self.answer_buttons.append(btn)
    
    def create_control_buttons(self, next_callback, results_callback):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        self.next_button = ttk.Button(
            button_frame,
            text="Next Question",
            command=next_callback
        )
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        self.results_button = ttk.Button(
            button_frame,
            text="Show Results",
            command=results_callback
        )
        self.results_button.pack(side=tk.LEFT, padx=10)
    
    def create_progress_bar(self):
        self.progress_bar = ttk.Progressbar(
            self.main_frame,
            mode='determinate'
        )
        self.progress_bar.pack(fill=tk.X, pady=20)
    
    def update_question(self, question_data):
        if question_data:
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.answer_buttons[i].config(text=option, value=option)
    
    def update_progress(self, current, total):
        if total > 0:
            progress = (current / total) * 100
            self.progress_bar['value'] = progress
