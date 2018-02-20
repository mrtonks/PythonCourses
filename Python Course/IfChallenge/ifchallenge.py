# Write down a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (the must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.
name = input("What's your name? ")
age = int(input("What's your age, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {0}.".format(name))
else:
    print("Sorry, but you can't enter to the holiday, {0}.".format(name))