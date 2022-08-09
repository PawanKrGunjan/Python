def minion_game(word):
    player1=0
    player2=0
    str_len = len(word)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 +=(str_len)-i
        else:
            player2 += (str_len)-i
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
    # The Minion Game in Python - Hacker Rank Solution END

if __name__ == '__main__':
    s = input()
    minion_game(s)
