from questions import Question


question_prompts = [
    Question("1) What color are brinjalS? \n (a) Red/purple \n (b) Green \n (c) Yellow \n\n", "a"),
    Question("2) Ram stands for? \n (a) God \n (b) Peace \n (c) Random access memory \n\n", "c"),
    Question("3) Who is the Prime Minister of India?? \n (a) Meloni \n (b) Modi \n (c) Rahul Pappu \n\n", "b"),
    Question("4) What is the use of Excel Sheet? \n (a) data killing \n (b) Data controling \n (c) Data Entry/ Data Managing \n\n", "c"),
    Question("5) What is the capital of france? \n (a) Paris \n (b) London \n (c) Virginia \n\n", "a")
]

questions = [
    question_prompts[0],
    question_prompts[1],
    question_prompts[2],
    question_prompts[3],
    question_prompts[4]
]



def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt).strip().lower()
        if answer == q.answer.lower():
            score += 1.3
            print("This was correct! Let's move to the next question.")
        else:
            print("This was wrong! Try again")

    print(f"Your score is {score}/{len(questions)}")
    

if __name__ == "__main__":
    run_test(questions)