# Quiz Game in Python

questions = [
    {
        "question": "What is the capital city of Koshi Province?",
        "options": ["A. Itahari", "B. Dharan", "C. Biratnagar", "D. Damak"],
        "answer": "C"
    },
    {
        "question": "Which is not an object oriented programming language?",
        "options": ["A. Python", "B. Java", "C. C++", "D. C"],
        "answer": "D"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "B"
    },
    {
        "question": "Which is the second highest mountain in the world?",
        "options": ["A. Makalu", "B. K2", "C. Manaslu", "D. Kangchenjunga"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Au", "B. Ag", "C. Gd", "D. Go"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
]

score = 0

print("Welcome to the Quiz Game!")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    userAnswer = input("Please enter your answer (A, B, C, or D): ").upper()

    if userAnswer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")
    
print(f"Your final score is {score} out of {len(questions)}.")
print("Thank you for playing the Quiz Game!")

