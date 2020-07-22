word = 'bottles'

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall")
    print(beer_num, word, "of beer")
    print("Take one down")
    print("Pass it around")

    if beer_num == 1:
        print("No more bottles of beers on the wall.")
    else:
        current_bottle = beer_num - 1

        if current_bottle == 1:
            word = 'bottle'
        print(current_bottle, word, "of beer on the wall")
    print()    
    

