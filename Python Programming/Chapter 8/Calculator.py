#Calculator Sample Program
#Python version of a calculator program

#The variable round tells whether to loop or not
#if variable rounds is equal to 1, it means to loop
#any other answer means don't loop
round = 1

#this variable holds the user's choice in the menu:

choice = 0

while round == 1:
    #print what options you have
    print "Welcome to the Calculator"

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Substraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit Calculator"
    print " "

    choice = raw_input("Choose your option: ").rstrip()
    
    if choice == '1':
        a = int(raw_input("First number: "))
        b = int(raw_input("Second number: "))
        sum = a + b
        print a, " + ", b, " = ", sum
    elif choice == '2':
        c = int(raw_input("First number: "))
        d = int(raw_input("Second number: "))
        diff = c - d
        print c, " - ", d, " = ", diff
    elif choice == '3':
        e = int(raw_input("First number: "))
        f = int(raw_input("Second number: "))
        prod = e * f
        print e, " * ", f, " = ", prod
    elif choice == '4':
        g = float(raw_input("First number: "))
        h = float(raw_input("Second number: "))
        quot = g / h
        print g, " / ", h, " = ", quot
    elif choice == '5':
        round = 0
    
print "Thank you for using the calculator!"