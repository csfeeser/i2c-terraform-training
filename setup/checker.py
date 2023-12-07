import yaml

# Read a YAML file and return the data
def read_yaml(file_name):
    with open(file_name, 'r') as file:
        return yaml.safe_load(file)

# Write data to a YAML file
def write_yaml(file_name, data):
    with open(file_name, 'w') as file:
        yaml.dump(data, file)

# Read the quiz and total YAML files
quiz_data = read_yaml('quiz.yaml')
total_data = read_yaml('total.yaml')

# Extract questions from quiz.yaml
quiz_questions = {item['Question'] for item in quiz_data}

# Find questions in total.yaml not in quiz.yaml
difference_data = [item for item in total_data if item['Question'] not in quiz_questions]

# Write the difference to difference.yaml
write_yaml('difference.yaml', difference_data)

