import random

user_seed = int(input("Enter seed: "))
random.seed(user_seed)

# prize_values holds the amount of money in a list for its respective question number
prize_values = [0, 1000, 2000, 3000, 4000, 8000, 10000, 20000, 30000, 40000, 60000, 80000, 150000, 250000, 500000, 1000000]
amount_earned = 0                   # Initializing the toltal amount of money earned to 0
lifeline_used = False               # Initializing the flag for lifeline being used to False

for question_number in range(1, 16):
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    op_list = ["+", "-", "*", "/"]
    op = random.choice(op_list)

    options = ["A", "B", "C", "D"]
    c = random.choice(options)
    r = ''

    soln = int(eval(str(x) + op + str(y)))

    if question_number == 5 or question_number == 10:
        print("Question {} (${}#):".format(question_number, prize_values[question_number]))
        print("{} {} {} = ?".format(x, op, y))
    else:
        print("Question {} (${}):".format(question_number, prize_values[question_number]))
        print("{} {} {} = ?".format(x, op, y))

    for choice in options:
        print("{}. ".format(choice), end = '')
        if choice == c:
            print("{}  ".format(soln), end = '')
            correct = choice
        else:
            r = random.randint(1, 100) 
            while r == soln:
                r = random.randint(1, 100)   
            print("{}  ".format(r), end = '')
    
    if lifeline_used or question_number == 15:
        print("F. Withdraw", end = '')
    else:
        print("E. Jump  F. Withdraw", end = '')
    print('')

    user_ans = input("Final answer: ").upper()

    if user_ans == correct:
        print("Right!")
        if question_number > 5 and question_number < 10:
            amount_earned = 8000
        elif question_number > 10 and question_number < 15:
            amount_earned = 60000
        elif question_number == 15:
            print("Game over!")
            print("You got $1000000!")
            print("Congrats! You are a millionaire!")
        else:
            amount_earned = prize_values[question_number]
    elif user_ans == "E":
        lifeline_used = True
        if question_number == 5:
            amount_earned = 0
        elif question_number == 10:
            amount_earned = 8000
    elif user_ans == "F":
        if question_number == 6 or question_number == 11:
            amount_earned = 0
        elif lifeline_used:
            amount_earned = prize_values[question_number - 2]
        else:
            amount_earned = prize_values[question_number - 1]
        print("Game over!")
        print("You got ${}!".format(amount_earned))
        break
    else:
        print("Wrong!")
        print("Game over!")
        print("You got ${}!".format(amount_earned))
        break
