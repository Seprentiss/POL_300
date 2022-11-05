# Finish the code to join together the numbers 0-9 into a string
def for_loop():
    string_to_print = ""
    # Fix the for loop. What goes inside parentheses after range
    for i in range(10):
        string_to_print += str(i)

    return string_to_print


# Finish the code to sum all numbers from 0-n
def while_loop():
    run_num = 0
    int_to_print = 0

    # Fill in what goes after the <
    while run_num < 10:
        int_to_print += run_num
        run_num += 1

    return int_to_print


def sum_evens_sub_odds():
    test_list = [1, 2, 3, 4, 5, 6]
    sum = 0

    for num in test_list:

        if num % 2 == 0:
            sum += num
        if num % 2 == 1:
            sum -= num

    return sum



# DO NOT CHANGE BELOW THIS LINE. TESTING YOUR OUTOUT

print(for_loop())  # 0123456789
print(while_loop())  # 45
print(sum_evens_sub_odds())  # 3