import os
import yaml

# Load questions from a YAML file
def load_questions():
    with open("difference.yaml", 'r') as file:
        return yaml.safe_load(file)

questions = load_questions()

def run_quiz(questions):
    for question in questions:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        #print(question["Question"])
        print("\033[1;36m" + question["Question"] + "\033[0m")  # Cyan color for question
        print("\n")
        # Iterating over keys A, B, C, D, E... and printing corresponding options
        for key in ['A', 'B', 'C', 'D', 'E']:
            if key in question:
                print(f"{key}: {question[key]}")
        
        input()
        print("\033[1;32m" + f"Answer: {question['Answer']}" + "\033[0m")  # Green color for answer
        print("\033[1;34m" + f"Explanation: {question['Explanation']}" + "\033[0m")  # Blue color
        input()

# Run the quiz
run_quiz(questions)

# Note: The script won't run in this notebook environment as it requires interaction. 
# You should run this script in a local Python environment.

