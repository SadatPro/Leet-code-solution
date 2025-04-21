

differences = [1, -3, 4]
lower = 1
upper = 6
def numberOfArrays(differences,lower,upper):

    curr = min_sum = max_sum = 0
    for diff in differences:
        curr += diff
        min_sum = min(curr,min_sum)
        max_sum = max(curr, max_sum)

    lower_x = lower - min_sum
    upper_x = upper - max_sum

    return   upper_x - lower_x + 1






print(numberOfArrays(differences, lower, upper))  # Output: 2
