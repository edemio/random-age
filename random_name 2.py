from random import randint
import matplotlib.pyplot as plt
import numpy as np

random_int1 = 0
random_int2 = 0
run = 0
e_total_guesses = 0
s_total_guesses = 0
e_guesses_in_one_run = 0
s_guesses_in_one_run = 0
e_guess_list = []
s_guess_list = []
rounds = []
e_smaller = 0
s_smaller = 0
while run <= 99:
    while random_int1 + random_int2 != 19:
        random_int1 = 0 + randint(0, 13)
        random_int2 = 0 + randint(0, 13)
        if random_int1 + random_int2 == 19:
            print(random_int1 + random_int2)
            print('wow that is edems age')
            e_guess_list.append(e_guesses_in_one_run)
        else:
            print(random_int1 + random_int2)
            print('try again')
            e_total_guesses += 1
            e_guesses_in_one_run += 1
    while random_int1 + random_int2 != 21:
        random_int1 = 0 + randint(2, 13)
        random_int2 = 0 + randint(2, 13)
        if random_int1 + random_int2 == 21:
            print(random_int1 + random_int2)
            print('wow that is setors age')
            s_guess_list.append(s_guesses_in_one_run)
        else:
            print(random_int1 + random_int2)
            print('try again')
            s_total_guesses += 1
            s_guesses_in_one_run += 1
    run += 1
    rounds.append(run)
    if e_guesses_in_one_run < s_guesses_in_one_run:
        e_smaller += 1
    else:
        s_smaller += 1
    e_guesses_in_one_run = 0
    s_guesses_in_one_run = 0
    print()
    print(f'edem has less guesses in {e_smaller} / {run} cases')
    print(f'setor has less guesses in {s_smaller} / {run} cases')
print()
print(f'list for edem guesses = {e_guess_list}')
print(f'average tries edem = {sum(e_guess_list) / len(e_guess_list)}')
print()
print(f'list for setor guesses = {s_guess_list}')
print(f'average tries setor = {sum(s_guess_list) / len(s_guess_list)}')
print(((np.array(e_guess_list) - np.array(s_guess_list)) >= 0).sum())
plt.plot(rounds, e_guess_list, s_guess_list)
plt.show()
total_guesses = e_total_guesses + s_total_guesses
print(f'in {run} rounds a total amount of {total_guesses} were made. '
      f'That are on average {total_guesses / run} guesses per round!')
