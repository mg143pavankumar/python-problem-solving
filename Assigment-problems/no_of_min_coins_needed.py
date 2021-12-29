def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # finding number of fives required for rupees_to_make
    five = int(rupees_to_make/5)
    one_needed = rupees_to_make % 5

    five_needed = five if five <= no_of_five else no_of_five

    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five

    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(
        five_needed, one_needed))) if one_needed <= no_of_one else (print(-1))


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28, 8, 5)
