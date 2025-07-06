foods=[]
prices=[]
total=0

while True:
    food=input("enter a food to buy or press q to quit: ")
    if food.lower =='q':
        break
    else:
        price=float(input(f"enter the price of the (food):R"))
        foods.append(food)
        price.append(price)

        print("--- YOUR CART ---")

        for price in food:
            print(food)

        for price in prices:
           print(prices)

    total += price
    print(f"your total is:R(total) ")

