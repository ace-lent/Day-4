#the random module in order for us to generate random choices
import random
#user's input of 3 numbers bet lottery in order. Also, automatically converts string format into integer in one line
bet = list(map(int, input("Place bet (3 numbers with spaces): ").split()))
#this line generates any kind of three digit numbers that's why the range is 3
result = [random.randint(1, 9) for i in range(3)]
#this line prints the generated three digit numbers which will be compared to the user's bet whether they won or not
print(f"The result is: {result}")

#this are the conditions or the logic behind how a player would win
#this first condition states that if the user's 3 digit number inputted equals to the generated digits, then in prints that the player has won
if bet == result:
    print("You win!")
#this second conditon states that if the user has equated two numbers from the randomized result, the user almost won    
elif bet[1:] == result[1:]:
    print("You almost won")
#this third condition states that if the user has equated only one number from the radomized result, then the user partially got it    
elif any(bet[i] == result[i] for i in range(3)):
    print("You partially got it")
#lastly, if the user's bet does not equals to any number generated, then the user loses    
else:
    print("You lost")
#note that the logic of how you can get an equal number to the generated random number should also resonates the placing of the number
#example: bet: 123 result: 321, you partially won because you only got the 2 right in the middle
#even when you got the other 2 digits right, it doesn't count because of the placing of each numbers is wrong

