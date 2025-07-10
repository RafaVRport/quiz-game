# quiz-game
Python Quiz Game project
# Python Quiz Game

A simple command-line quiz game in Python. Users answer multiple-choice questions, receive feedback, and see their final score.

## Features
- Loads questions from a JSON file
- Randomizes question order
- Immediate feedback after each question
- Final score summary

## How to Run

1. Make sure you have Python installed.
2. Clone this repository and navigate to its folder.
3. Run the game:

    ```bash
    python quiz_game.py
    ```

4. Answer the questions by entering the number of your chosen option.

## Customizing Questions

Edit the `questions.json` file to add, remove, or modify quiz questions.  
Each question should have:
- `"question"`: The question text
- `"choices"`: A list of possible answers
- `"answer"`: The number (1-indexed) of the correct choice

## Example
