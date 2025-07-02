

# quiz_app.py
import tkinter as tk
from tkinter import ttk, messagebox
from question_manager import QuestionManager
from ui_components import UIComponents
from score_manager import ScoreManager

class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")
        
        self.question_manager = QuestionManager()
        self.ui = UIComponents(root)
        self.score_manager = ScoreManager()
        
        self.current_question = 0
        self.selected_answer = tk.StringVar()
        
        self.setup_ui()
        self.load_question()
    
    def setup_ui(self):
        self.ui.create_main_frame()
        self.ui.create_question_label()
        self.ui.create_answer_buttons(self.selected_answer)
        self.ui.create_control_buttons(self.next_question, self.show_results)
        self.ui.create_progress_bar()
    
    def load_question(self):
        if self.current_question < len(self.question_manager.questions):
            question_data = self.question_manager.get_current_question(self.current_question)
            self.ui.update_question(question_data)
            self.ui.update_progress(self.current_question, len(self.question_manager.questions))
        else:
            self.show_results()
    
    def next_question(self):
        answer = self.selected_answer.get()
        if answer:
            is_correct = self.question_manager.check_answer(self.current_question, answer)
            self.score_manager.add_answer(is_correct)
            self.current_question += 1
            self.selected_answer.set("")
            self.load_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer!")
    
    def show_results(self):
        score = self.score_manager.get_score()
        total = len(self.question_manager.questions)
        self.score_manager.save_result(score, total)
        messagebox.showinfo("Results", f"Your score: {score}/{total}")
        self.reset_quiz()
    
    def reset_quiz(self):
        self.current_question = 0
        self.score_manager.reset()
        self.load_question()

