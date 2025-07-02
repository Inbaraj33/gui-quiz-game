import json
import random
import os

class QuestionManager:
    def __init__(self, category="general"):
        self.category = category
        self.questions = []
        self.load_questions()
    
    def load_questions(self):
        file_path = f"data/{self.category}.json"
        try:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, "r") as file:
                    content = file.read().strip()
                    if content:
                        data = json.loads(content)
                        self.questions = data.get("questions", [])
                        random.shuffle(self.questions)
                        return
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        self.load_default_questions()
    
    def load_default_questions(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct": "Mars"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "correct": "4"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
                "correct": "Pacific"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Van Gogh", "Da Vinci", "Picasso", "Monet"],
                "correct": "Da Vinci"
            }
        ]
    
    def get_current_question(self, index):
        if index < len(self.questions):
            return self.questions[index]
        return None
    
    def check_answer(self, index, answer):
        if index < len(self.questions):
            return self.questions[index]["correct"] == answer
        return False