import random
win_num=random.randint(1,10)
user_input= int(input("plz guess a number  "))
attemt=0
while True:
    attemt +=1
    if win_num > user_input:
        print("sorry number is too low   ")
        user_input=int(input("guess again  "))
    elif win_num < user_input:
        print("sorry number is too high  ")
        user_input=int(input("guess again   "))
    elif win_num == user_input:
        print("you win   ",)
        print(f"you won in{attemt}step")
        break