hello#snake and ladder
import random
N=0
while (N<100):


        n=input("enter 'r' to roll a dice")
        if(n=='r'):
            r=random.randint(1,6)
            N=N+r
            print("your random number ",r)
            print("your in position",N)
            if N>100:
               print("ur position is greater than 100 please try again")
               N=N-r
            elif N==100:
              print("U won")
        
        elif N==8:
            N=37
           
            print("you just climed a ladder and you are in position",N)
        elif N==11:
            N=2
        
            print("ooh,you got bitten by a snake and you are in position",N)
        elif N==13:
            N=34
           
            print("you just got on a ladder and you are in position",N)
        elif N==25:
            N=4
          
            print("oh no a snake bite you and you are in position",N)
        elif N==38:
            N=9
         
            print("a snake bite you and now your position is",N)
        elif N==40:
            N=68
          
            print("on the ladder and you climed to",N)
        elif N==52:
            N=81
           
            print("got on a ladder and now you are in",N)
        elif N==65:
            N=46
           
            print("got bite by a snake and your going down to",N)
        elif N==76:
            N=97
           
            print("you just climed a ladder and now your position is",N)
        elif N==89:
            N=70
            
            print("got bite by a snake and you are now going down to",N)
        elif N==93:
            N=64
        
            N==100
            print("unfortunately got bite by a snake and now you r going down to",N)
        elif N==100:
            print("congratulations you have won the game")

