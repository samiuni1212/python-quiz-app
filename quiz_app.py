import tkinter as tk
from tkinter import messagebox

# Define the quiz questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 1  # Position in the options array (index starts from 1)
    },
    {
        "topic": "Lists",
        "question": "What will be the result of this Python code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "IndexError"],
        "answer": 2  # "2" is the correct answer (second option)
    },
    {
        "topic": "Strings",
        "question": "What will this code output?",
        "code": "print('Hello' + ' ' + 'World')",
        "options": ["HelloWorld", "Hello World", "Hello+World", "Error"],
        "answer": 2  # "Hello World" is the correct answer
    },
    {
        "topic": "Conditionals",
        "question": "What will be the output of this code?",
        "code": "x = 10\nif x > 5:\n    print('Greater')\nelse:\n    print('Smaller')",
        "options": ["Greater", "Smaller", "None", "Error"],
        "answer": 1  # "Greater" is the correct answer
    },
    {
        "topic": "Functions",
        "question": "What will this function return?",
        "code": "def add(a, b):\n    return a + b\n\nprint(add(2, 3))",
        "options": ["23", "5", "None", "Error"],
        "answer": 2  # "5" is the correct answer
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator App")
        
        self.current_question = None
        
        # Input field for topic
        self.topic_label = tk.Label(root, text="Enter Python topic:")
        self.topic_label.pack(pady=5)
        
        self.topic_entry = tk.Entry(root)
        self.topic_entry.pack(pady=5)
        
        # Button to generate question
        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack(pady=10)
        
        # Display the question, code, and options
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=5)
        
        self.code_label = tk.Label(root, text="", wraplength=400)
        self.code_label.pack(pady=5)
        
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=5)
        
        self.feedback_label = tk.Label(root, text="", wraplength=400)
        self.feedback_label.pack(pady=10)
        
        # Submit button
        self.submit_button = tk.Button(root, text="Submit", state=tk.DISABLED, command=self.submit_answer)
        self.submit_button.pack(pady=10)

    def generate_question(self):
        # Get the entered topic
        topic = self.topic_entry.get().strip()

        # Search for questions with the entered topic
        for question in questions:
            if question["topic"].lower() == topic.lower():
                self.current_question = question
                break
        else:
            self.current_question = None

        # If a question is found, display it
        if self.current_question:
            self.display_question()
        else:
            messagebox.showerror("Error", f"No question found for topic: {topic}")
        
    def display_question(self):
        # Display the question and code
        self.question_label.config(text=f"Topic: {self.current_question['topic']}\n{self.current_question['question']}")
        self.code_label.config(text=f"Code:\n{self.current_question['code']}")
        
        # Remove any previous options (in case topic is changed)
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Display the options
        self.selected_option = tk.IntVar()
        for idx, option in enumerate(self.current_question["options"], start=1):
            rb = tk.Radiobutton(self.options_frame, text=option, variable=self.selected_option, value=idx)
            rb.pack(anchor="w")
        
        # Enable the Submit button
        self.submit_button.config(state=tk.NORMAL)
        
        # Clear the feedback label
        self.feedback_label.config(text="")
        
    def submit_answer(self):
        # Get the selected answer
        selected_answer = self.selected_option.get()

        # Check if the answer is correct
        if selected_answer == self.current_question["answer"]:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")

        # Disable the Submit button
        self.submit_button.config(state=tk.DISABLED)

# Create the Tkinter window
root = tk.Tk()

# Create the quiz app
quiz_app = QuizApp(root)

# Start the Tkinter event loop
root.mainloop()
