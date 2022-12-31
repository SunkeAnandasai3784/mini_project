import random

# A list of questions with their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the largest ocean in the world?",
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the currency of Japan?",
        "answer": "Japanese yen"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "answer": "Mount Everest"
    }
]

# Shuffle the questions so that they appear in a random order
random.shuffle(questions)

# Initialize a score counter
score = 0

# Iterate over the questions and ask them to the user
for question in questions:
    # Ask the question and get the user's answer
    answer = input(question["question"] + " ")

    # Check if the answer is correct and update the score
    if answer.lower() == question["answer"].lower():
        score += 1

# Print the final score
print("You scored", score, "out of", len(questions))
