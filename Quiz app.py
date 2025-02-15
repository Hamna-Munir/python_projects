import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import pygame

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Quiz App")
        self.root.geometry("500x500")
        
        pygame.mixer.init()
        
        self.username = simpledialog.askstring("Username", "Enter your name:")
        self.category = self.select_category()
        self.difficulty = self.select_difficulty()
        self.questions = self.load_questions()
        
        self.question_index = 0
        self.score = 0
        self.time_left = self.difficulty
        self.lifelines = {"50/50": True, "Extra Time": True, "Skip": True}

        self.question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=25, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left} sec", font=("Arial", 12))
        self.timer_label.pack(pady=5)

        self.lifeline_frame = tk.Frame(root)
        self.lifeline_frame.pack(pady=10)
        
        self.lifeline_buttons = {}
        for lifeline in self.lifelines:
            btn = tk.Button(self.lifeline_frame, text=lifeline, command=lambda l=lifeline: self.use_lifeline(l))
            btn.pack(side=tk.LEFT, padx=5)
            self.lifeline_buttons[lifeline] = btn
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)
        
        self.display_question()
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left} sec")
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    def select_category(self):
        categories = ["Math", "Science", "History", "Geography", "Technology", "Sports"]
        category = simpledialog.askstring("Category", "Choose a category: " + ", ".join(categories))
        return category.capitalize() if category.capitalize() in categories else "Math"

    def select_difficulty(self):
        levels = {"Easy": 10, "Medium": 7, "Hard": 5, "Very Hard": 3}
        difficulty = simpledialog.askstring("Difficulty", "Choose difficulty (Easy, Medium, Hard, Very Hard):")
        return levels.get(difficulty.capitalize(), 10)
    
    def load_questions(self):
        all_questions = {
            "Math": [
                ("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
                ("Solve: 15 * 2 - 5", ["20", "25", "30", "35"], "25"),
                ("What is 9 / 3?", ["1", "2", "3", "4"], "3"),
                ("Solve: 8 * 7", ["50", "56", "60", "70"], "56"),
                ("What is 6 * 6?", ["36", "30", "40", "45"], "36")
            ],
            "Science": [
                ("What is H2O?", ["Oxygen", "Helium", "Water", "Hydrogen"], "Water"),
                ("Which element has atomic number 1?", ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], "Hydrogen"),
                ("What is the chemical symbol for gold?", ["Ag", "Au", "Pb", "Fe"], "Au"),
                ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
                ("What is the freezing point of water in Celsius?", ["0", "32", "100", "-10"], "0")
            ],
            "History": [
                ("Who was the first president of the United States?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "George Washington"),
                ("In which year did World War II end?", ["1940", "1945", "1950", "1960"], "1945"),
                ("Who discovered America?", ["Christopher Columbus", "Vasco da Gama", "Marco Polo", "Ferdinand Magellan"], "Christopher Columbus"),
                ("Who was the first emperor of China?", ["Qin Shi Huang", "Liu Bang", "Wang Mang", "Li Shimin"], "Qin Shi Huang"),
                ("What year did the Titanic sink?", ["1912", "1900", "1920", "1898"], "1912")
            ],
            "Geography": [
                ("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
                ("Which is the largest continent?", ["Asia", "Africa", "Europe", "America"], "Asia"),
                ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
                ("Which country has the most population?", ["India", "USA", "China", "Russia"], "China"),
                ("What is the highest mountain in the world?", ["K2", "Everest", "Makalu", "Kanchenjunga"], "Everest")
            ],
            "Technology": [
                ("What does HTML stand for?", ["HyperText Markup Language", "HighText Machine Language", "HyperText Making Language", "None of the above"], "HyperText Markup Language"),
                ("Who is the founder of Microsoft?", ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"], "Bill Gates"),
                ("What is the latest version of Python?", ["3.8", "3.9", "3.10", "3.11"], "3.10"),
                ("What year was the first iPhone released?", ["2005", "2007", "2009", "2010"], "2007"),
                ("What is the name of Tesla's electric car model?", ["Model S", "Model X", "Model 3", "Model Y"], "Model S")
            ],
            "Sports": [
                ("Who won the 2018 FIFA World Cup?", ["France", "Brazil", "Germany", "Argentina"], "France"),
                ("How many players are on a basketball team?", ["5", "6", "7", "8"], "5"),
                ("Which country is known for cricket?", ["USA", "India", "France", "Russia"], "India"),
                ("What is the distance of a marathon?", ["42.195 km", "42.2 km", "40 km", "45 km"], "42.195 km"),
                ("Who holds the record for most Olympic gold medals?", ["Michael Phelps", "Usain Bolt", "Carl Lewis", "Mark Spitz"], "Michael Phelps")
            ]
        }
        return all_questions.get(self.category, all_questions["Math"])
    
    def display_question(self):
        if self.question_index < len(self.questions):
            self.time_left = self.difficulty
            question, options, _ = self.questions[self.question_index]
            self.question_label.config(text=question)
            self.next_button.config(state=tk.DISABLED)
            
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, bg="SystemButtonFace", state=tk.NORMAL)
        else:
            self.show_result()
    
    def check_answer(self, choice):
        _, options, correct_answer = self.questions[self.question_index]
        selected_option = options[choice] if choice != -1 else None
        
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        
        if selected_option == correct_answer:
            self.option_buttons[choice].config(bg="#FFD700")
            self.score += 1
        else:
            if choice != -1:
                self.option_buttons[choice].config(bg="#FF4C4C")
            correct_index = options.index(correct_answer)
            self.option_buttons[correct_index].config(bg="#FFD700")
        
        self.next_button.config(state=tk.NORMAL)
    
    def use_lifeline(self, lifeline):
        if self.lifelines[lifeline]:
            if lifeline == "50/50":
                _, options, correct_answer = self.questions[self.question_index]
                incorrect_options = [opt for opt in options if opt != correct_answer]
                random.shuffle(incorrect_options)
                for btn in self.option_buttons:
                    if btn.cget("text") in incorrect_options[:2]:
                        btn.config(state=tk.DISABLED)
            elif lifeline == "Extra Time":
                self.time_left += 5
            elif lifeline == "Skip":
                self.next_question()
            self.lifelines[lifeline] = False
            self.lifeline_buttons[lifeline].config(state=tk.DISABLED)
    
    def next_question(self):
        self.question_index += 1
        self.display_question()
    
    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"{self.username}, your score: {self.score}/{len(self.questions)}")
        self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
