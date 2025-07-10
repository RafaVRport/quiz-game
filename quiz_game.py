import json

def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for idx, choice in enumerate(q["choices"], 1):
            print(f"{idx}. {choice}")
        answer = input("Your answer (1-4): ")
        if q["choices"][int(answer)-1

