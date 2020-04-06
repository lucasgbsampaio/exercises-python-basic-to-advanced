"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points
"""

def winner(stuart, kevin):
    if stuart > kevin:
        return f'Stuart {stuart}'
    elif kevin > stuart:
        return f'Kevin {kevin}'
    else:
        return 'Draw'

def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    string = string.upper()
    for index in range(len(string)):
        if string[index] in vowels:
            kevin = kevin + (len(string) - index)
        else:
            stuart = stuart + (len(string) - index)
    print(winner(stuart, kevin))

if __name__ == '__main__':
    s = input()
    minion_game(s)