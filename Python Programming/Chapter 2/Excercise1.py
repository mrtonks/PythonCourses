#This program will compute the total meal cost plus tip

food = 55.50
tax = 6.75/100
tip = 15.0/100

food = food + food * tax
total_cost = food + food * tip

print("%.2f" % total_cost)