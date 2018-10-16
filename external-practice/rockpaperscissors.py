def rockpaperscissors():
    import random
    ropasc = ["R","P","S"]
    ropasc2 = ["ROCK","PAPER","SCISSORS"]
    numwins = input("How many wins to declare victory?  ")
    
    while True:
        try: 
            numwins = int(numwins)
            break
        except(TypeError,ValueError):
            numwins = input("NOT AN INTEGER! TRY AGAIN!  ")
       
    wins = 0
    losses = 0

    while wins < numwins and losses < numwins:
        rand = random.randint(0,2)
        npc = ropasc[rand]
        player = input("r for Rock, p for paper, or s for scissors?  ")
        player = player.upper()
        print("COMPUTER: ",ropasc2[rand])
        while player not in ropasc:
            player = input("NOPE! Enter r for rock, p for paper, or s for scissors!  ")
            player = player.upper() 
        if player == npc:
            print(" ")
            print("DRAW!")
        elif player == ropasc[0] and npc == ropasc[2]:
            wins += 1
            print(" ")
            print(ropasc2[0]," beats ",ropasc2[2])
            print("You win! PLAYER: ",wins, "| COMPUTER: ",losses)
        elif player == ropasc[1] and npc == ropasc[0]:                                         
            wins += 1
            print(" ")
            print(ropasc2[1]," covers ",ropasc2[0])
            print("You win! PLAYER: ",wins, "| COMPUTER: ",losses)
        elif player == ropasc[2] and npc == ropasc[1]:                                         
            wins += 1
            print(" ")
            print(ropasc2[2]," cut ",ropasc2[1])
            print("You win! PLAYER: ",wins, "| COMPUTER: ",losses)
        elif npc == ropasc[0] and player == ropasc[2]:
            losses += 1
            print(" ")
            print(ropasc2[0]," beats ",ropasc2[2])
            print("Aww too bad! PLAYER: ",wins, "| COMPUTER: ",losses)
        elif npc == ropasc[1] and player == ropasc[0]:                                         
            losses += 1
            print(" ")
            print(ropasc2[1]," covers ",ropasc2[0])
            print("Aww too bad! PLAYER: ",wins, "| COMPUTER: ",losses)
        elif npc == ropasc[2] and player == ropasc[1]:                                         
            losses += 1
            print(" ")
            print(ropasc2[2]," cut ",ropasc2[1])
            print("Aww too bad! PLAYER: ",wins, "| COMPUTER: ",losses)
  
rockpaperscissors()
