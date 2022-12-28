import random

n = int(input("Enter seed: "))
random.seed(n)

alphabets = []
p = ''
q = ''

# Appends the list with all the alphabets

for i in range(65, 91):
    alphabets.append(chr(i))

# Randomly samples alphabets into a string and then puts them inside p

p_trial = random.sample(alphabets, 26)
for j in range(0, 26):
    p += p_trial[j]

# Randomly samples alphabets into a string and then puts them inside q

q_trial = random.sample(alphabets, 26)
for k in range(0, 26):
    q += q_trial[k]

# Randomly samples the numbers into pi and qi

pi = random.sample(range(0, 26), 10)
qi = random.sample(range(0, 26), 10)

print("Player P: {} {}".format(p, pi))
print("Player Q: {} {}".format(q, qi))

# Function that calculates the difference between each corresponding letter and calculates the score

def alpha_battle(p, pi, q, qi):
    p_list = list(p)
    q_list = list(q)
    ascii_P = []
    ascii_Q = []
    score_p = 0
    score_q = 0

    for i in range(0, 10):
        p_list[qi[i]] = 'tbd'
        q_list[pi[i]] = 'tbd'
    
    for j in range(25, -1, -1):
        if p_list[j] == 'tbd':
            del p_list[j]
        if q_list[j] == 'tbd':
            del q_list[j]
    
    for k in range(0, 16):
        ascii_P.append(ord(p_list[k]))
        ascii_Q.append(ord(q_list[k]))
    
    for l in range(0, 16):
        if ascii_P[l] > ascii_Q[l]:
            score_p += ascii_P[l] - ascii_Q[l]
        elif ascii_P[l] == ascii_Q[l]:
            continue
        else:
            score_q += ascii_Q[l] - ascii_P[l]

    result = dict(P = score_p, Q = score_q)
    print("Score: {}".format(result))
    if score_p > score_q:
        print("Player P wins!")
    elif score_p < score_q:
        print("Player Q wins!")
    else:
        print("Draw game!")

alpha_battle(p, pi, q, qi)