import os
import yaml
import textwrap

num = 100

# Load questions from a YAML file
def load_questions():
    with open("difference.yaml", 'r') as file:
        return yaml.safe_load(file)

questions = load_questions()


def run_quiz(questions):
    for question in questions:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        # Wrapping text at 'num' characters
        wrapped_question = textwrap.fill(question["Question"], width=num)
        print("\n")
        print("\033[1;36m" + wrapped_question + "\033[0m")  # Cyan color for question
        print("\n")

        # Iterating over keys A, B, C, D, E... and printing corresponding options
        for key in ['A', 'B', 'C', 'D', 'E']:
            if key in question:
                # Convert the value to string if it's not already
                option_value = str(question[key])
                # Wrapping option text and coloring the key differently
                option_text = textwrap.fill(option_value, width=num - len(key) - 2)
                print("\033[1;33m" + key + ":\033[0m " + option_text, "\n")  # Yellow color for keyS

        input()
        wrapped_answer = textwrap.fill(f"Answer: {question['Answer']}", width=num)
        print("\033[1;32m" + wrapped_answer + "\033[0m")  # Green color for answer
        wrapped_explanation = textwrap.fill(f"Explanation: {question['Explanation']}", width=num)
        print("\033[1;34m" + wrapped_explanation + "\033[0m")  # Blue color
        input()


# Run the quiz
run_quiz(questions)

# Note: The script won't run in this notebook environment as it requires interaction. 
# You should run this script in a local Python environment.

