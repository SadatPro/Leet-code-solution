from itertools import count


def numRabbits(answers):
    answers_set = set(answers)
    total = 0

    for answer, freq in enumerate(answers):

        if answer  in answers_set:
            total += freq



    return total

# ✅ উদাহরণ:
answers = [1, 1, 2]
print("Minimum number of rabbits:", numRabbits(answers))
