# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:56:48 2021

@author: yac
"""

class Questions:
    def __init__(self, spørsmål, svar, valg):
        self.question = spørsmål
        self.answer = svar
        self.choice = valg
    
    def control(self, choice):
        if choice-1 == self.answer:
            return True
    
    def __str__(self):
       return (f"\n \n {self.question}\n \n {self.choice}")
        
    def correct(self):
        return f"det riktigie svaret er {self.choice[self.answer]}"
    
def Read_file():
    list_track = []
    with open("sporsmaalsfil.txt", "r", encoding= "UTF-8") as file:
        for line in file:
            line = line.replace("[","").replace("]","").split(":")
            
            question = line[0]
            answer = int(line[1])
            choice = line[2].strip("\n").split(",")
            
            
            track = Questions(question, answer, choice)
            
            list_track.append(track)
            
        return list_track
    
Score_player1 = 0
Score_player2 = 0

if __name__=="__main__":
    x = Read_file()
    counter = 0
    
    for i in x:
        print(i.question)
        choice_i = 1

        for que in i.choice:
            print(f"({choice_i}){que}")
            choice_i += 1
            
        choice_P1 = int(input("Player 1: "))
        choice_P2 = int(input("Player 2: "))
        
        print("\n"+i.correct())
        
        if i.control(choice_P1):
            Score_player1 += 1
            print(choice_P1)
            print("P1 riktig" + "\n")
        else:
            print("P1: hahaha")
        
        if i.control(choice_P2):
            Score_player2 += 1
            print(choice_P2)
            print("P2:  riktig")
        else:
            print("P2: haha")
    
        
print(f"Player 1: poeng{Score_player1}")
print(f"player 2: poeng{Score_player2}")
    
    
    
    
    
    