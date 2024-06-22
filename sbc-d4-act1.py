#modules in order to generate random integers
from random import randint
#player's input choices whether kulob(fold) or hayang(unfold)
p1 = input("Kulob Hayang? ")
#this line is a conditional statement that if a player has inputted a choice neither both kulob or hayang, it prints kulob or hayang ra oy or it just basically doesn't continue to the game
if p1 not in ["kulob", "hayang"]:
    print("kulob or hayang ra oy")
#then this line states that if the player has inputted kulob or hayang, the two cpu's randomizes their pick whether kulob or hayang
#both lines c2 and c3 variables has assigned value 0 to kulob and 1 to hayang
#notice the 0,1. this means that it randomizes numbers form 0 to 1 which are assigned values for kulob and hayang   
else:
    c2 = "kulob" if randint(0, 1) == 0 else "hayang"
    c3 = "kulob" if randint(0, 1) == 0 else "hayang"
#now this next two lines prints both cpu 2 and cpu 3's picks which can be kulob or hayang
    print(f"Computer 2 = {c2}")
    print(f"Computer 3 = {c3}")
#this is now the logic how the winner can be decided
#now the first condition states that if the player, cpu 2 and cpu 3 equates each other or example they all have picked kulob, then it prints tabla or draw
    if p1 == c2 == c3:
        print("Tabla!")
#this next condition states that if the player one picked the different one or he picked kulob then both cpu's have picked hayang, then the player has won         
    elif p1 != c2 and p1 != c3:     
        print("Player ang daog!")
#this condition states that if the cpu 2 picked the different one from player and cpu 3, then cpu 2 has won        
    elif c2 != p1 and c2 != c3:
        print("CPU 2 ang daog!")
#then the last condition, else if the cpu 3 picked different, then cpu 3 has won        
    else:
        print("CPU 3 ang daog!")
#note that the logic of how the winner is decided relied on the fact who is the one who picked the different choice whether kulob or hayang