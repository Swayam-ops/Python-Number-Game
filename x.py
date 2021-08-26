import random

def compare_number(number, user_guess):
    Positive_marks = [0, 0, 0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
           Positive_marks[i] += 1
    return Positive_marks


if __name__ == "__main__":
    playing = True
    number = str(random.randint(1000, 10000))
    guesses = 0

    print("Let's Play A Game")
    print("PYTHON will Generate A 4 Digit Number, And You Have To Guess The Numbers One Digit At A Time.")
    print("For Every Number I The Wrong Place, You Get 's -1. For Every Number In The Right Place, You Get 's +4.")
    print("The Game Will End When You Get 20 marks.")
    print("Type Exit! if you get frustrated")

while playing:
    user_guess = input("Guess the NUMBER: ")
    if user_guess.lower() == "exit":
        break
    positivenegative_count = compare_number(number, user_guess)
    guesses += 1
    correct = sum(positivenegative_count)
    wrong = len(number) - correct
    print(f"You Have {correct} +4, And {wrong} -1.")

    if correct == 4:
        playing = False
        print(f"You Win The Game After {guesses} Guess(es)!. The Number Was {number}.")
        break
    else:
        print(f"Your Guess Isn't Quite Right, Try Again!.")
        if correct >= 1:
            print(str([user_guess[i] for i, x in enumerate(positivenegative_count) if x == 1]) + " was correct!")