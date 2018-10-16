def hangman(word):
    wrong = 0
    stages = ["", 
             "________        ", 
             "|               ",
             "|      |        ", 
             "|      0        ", 
             "|     /|\       ",  
             "|     / \       ", 
             "|               " ] 
    charlist = [] 
    rletters = list(word) 
    board = ["__"] * len(word) 
    win = False 
    print("Welcome to Hangman") 
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            charlist.append(char)
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        print("Guesses: ",charlist)
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))
import random
wordlist = \
["scintillating","reaction","proud","abusive","better","alert","hushed","flat","knot","silky","numerous","treat","late","shut","strap","caring","bewildered","lush","decorate","metal","handle","horrible","worry","trees","young","happen","pest","cushion","festive","race","possible","one","advise","birth","murder","dog","befitting","slope","wholesale","husky","industrious","natural","nerve","youthful","acoustics","political","bustling","habitual","concentrate","subsequent","elite","grin","bizarre","quiver","planes","x-ray","burst","education","extend","smash","judge","drum","cannon","marvelous","precious","scold","hurried","tap","heavy","kiss","spiteful","want","clean","step","adventurous","open","woebegone","oranges","umbrella","bedroom","cloistered","pastoral","lethal","smell","ray","edge","wrong","bright","form","nauseating","allow","dance","wool","shade","sponge","obtain","office","talk","abaft","naughty","unadvised","wakeful","inquisitive","colorful","quick","thick","boy","aquatic","amusing","magic","promise","malicious","hat","brawny","watch","quiet","mature","return","pretty","eight","tacky","earthquake","lonely","flashy","unused","fluttering","present","toothpaste","mom","aspiring","pocket","cub","worried","fixed","snotty","calculator","consider","dogs","familiar","elbow","uppity","decisive","terrific","determined","kettle","torpid","sound","wary","shelter","nonstop","object","trains","tub","cultured","unlock","mist","property","mint","energetic","oafish","flag","educated","shirt","hour","rule","punch","rose","waste","hall","degree","pumped","behave","icicle","actually","men","hot","pie","moaning","crown","huge","leg","spot","trade","shrug","giants","food","abrupt","rich","six","representative","part","hilarious","forgetful","healthy","door","onerous","quizzical","found","tedious","crawl"]
theword = random.randint(0,199)
hangman(wordlist[theword])
