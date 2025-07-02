import json
import datetime
import os

class ScoreManager:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0
        self.results_file = "results/quiz_results.json"
        self.ensure_results_file()
    
    def ensure_results_file(self):
        os.makedirs(os.path.dirname(self.results_file), exist_ok=True)
        if not os.path.exists(self.results_file) or os.path.getsize(self.results_file) == 0:
            with open(self.results_file, "w") as file:
                json.dump({"history": []}, file, indent=2)
    
    def add_answer(self, is_correct):
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1
    
    def get_score(self):
        return self.correct_answers
    
    def get_percentage(self):
        if self.total_questions > 0:
            return (self.correct_answers / self.total_questions) * 100
        return 0
    
    def reset(self):
        self.correct_answers = 0
        self.total_questions = 0
    
    def save_result(self, score, total):
        result = {
            "date": datetime.datetime.now().isoformat(),
            "score": score,
            "total": total,
            "percentage": round((score / total) * 100, 2) if total > 0 else 0
        }
        
        try:
            with open(self.results_file, "r") as file:
                content = file.read().strip()
                if content:
                    results = json.loads(content)
                else:
                    results = {"history": []}
        except (FileNotFoundError, json.JSONDecodeError):
            results = {"history": []}
        
        results["history"].append(result)
        
        with open(self.results_file, "w") as file:
            json.dump(results, file, indent=2)
    
    def load_history(self):
        try:
            with open(self.results_file, "r") as file:
                content = file.read().strip()
                if content:
                    data = json.loads(content)
                    return data.get("history", [])
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return []