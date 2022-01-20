import os
import sys
import time
"""Bohdan Simulator
made by Tre"""
calories=0
print("You are Bohdan. You wake up and get out of bed.")
#Section1
time.sleep(1)
print("What would you like to do?")
option1=int(input("You can eat(1) or listen to sea shanties(2)."))
if option1==1:
    print("You eat a delicious mejackmeal.")
    calories+=10
elif option1==2:
    print("You listen to sea shanties.")
else:
    print("That is not a valid option!")
#Section2
time.sleep(1)
print("What would you like to do now?")
option2=int(input("You can eat(1) or take a nap(2)."))
if option2==1:
    print("You eat another delicious mejackmeal.")
    calories+=10
elif option2==2:
    print("You take a quick nap and wake up well rested.")
else:
    print("That is not a valid option!")
#Section3
time.sleep(1)
print("What would you like to do this time?")
option3=int(input("You can eat(1) or go on dysania(2)."))
if option3==1:
    print("You eat a third delicous mejackmeal.")
    calories+=10
elif option3==2:
    print("You go on dysania and have a fun time.")
else:
    print("That is not a valid option!")
#End
time.sleep(1)
if calories>=30:
    ending="glutton"
elif 0<calories<30:
    ending="normal"
elif calories==0:
    ending="good"
time.sleep(1)
print("You got the "+str(ending)+" ending!")
if ending=="glutton":
    print("You ate too much and exploded.")
elif ending=="normal":
    print("Just a normal day in the life of bohdan.")
elif ending=="good":
    print("You did not eat too much and lost some weight.")
input("Press ENTER to exit")