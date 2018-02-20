import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] =  "a sweet, orange, citrus fruit"
    fruit['apple'] =  "good for making soda"
    fruit['lemon'] =  "a sour, lemon citrus fruit"
    fruit['grape'] =  "a small, sweet fruit growing in bunches"
    fruit['lime'] =  "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])