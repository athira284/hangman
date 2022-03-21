# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:58:51 2019

@author: Athira Mohanan
"""
import random
import sys
coll = ["python", "mountain", "spyder", "nature", "galaxy", "mobile", "table", "desktop",
 "linux", "monkey", "donkey", "secret", "alphabet"]
guessword = []
sw = random.choice(coll) 
length = len(sw)
alphabet = "abcdefghijklmnopqrstuvwxyz"
repeat = []
def reg():
    print("\nWelcome to hangman game!\n\nlets begin...............\n")
    while True:
        name = input("\nRegister your name\n").strip()
        if name =="":
            print("No!!! name cannot be empty")
        else:
            break
reg()
def strt():
    while True:
        ch = input("\nShall we start our game...?\n").upper()
        if ch == "YES" or ch == "Y":
            break
        elif ch == "NO" or ch == "N":
            sys.exit("\nThank you")
        else:
            print("\nReply as Yes or No")
            continue
strt()
def asgn():
    for chrtr in sw:
        guessword.append("-")
    print("\nthe word has", length, "characters\n")
    print("You can enter only 1 letter from a-z and you can make only 4 wrong attempts ......\n")
    print(guessword)
def prgm():
    atempt = 1
    while atempt < 5:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet: 
            print("Enter a letter from a-z alphabet")
        elif guess in repeat: 
            print("\nYou have already guessed that letter!")
        elif guess=="":
            print("\nNo space is accepted")
        else: 
            repeat.append(guess)
            if guess in sw:
                print("\nYou guessed correctly!")
                for x in range(0, length): 
                    if sw[x] == guess:
                        guessword[x] = guess
                        print(guessword)
                if not '-' in guessword:
                    print("\nCongrats....    :)   .....You won!")
                    break
            else:
                print("\nThe letter is not in the word. Try Again  !!!\n The number of attempts u made:\t",atempt)
                print(" \nThe number of attempts lft:\t",4-atempt)
                atempt += 1
            if atempt == 5:
                print("  \n Sorry, You lost :( The secret word was",sw)
asgn()
prgm()
guessword = []
sw = random.choice(coll) 
length = len(sw)
repeat = []
def conti():
    while True:
        ch = input("\ndo u want to continue...?\n").upper()
        if ch == "YES" or ch == "Y":
            asgn()
            prgm()
            break
        elif ch == "NO" or ch == "N":
            sys.exit("\nThank you")
        else:
            print("\nReply as Yes or No")
            continue
conti()
print("\nTHANK YOU     :) \nGAME OVER     :>")
