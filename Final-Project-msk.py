# Mathew Kelne
# Final Project

print("You are about to be asked a series of questions!")
print("This code will guess your age based on the answers you provide.")
print("Please answer the questions 1-5, one being disagree, and 5 being agree.")
print("Be honest, and have fun with it :)")

print("Age Guesser")

#Question 1
userResponce1 = int(input("Classic Rock is the best music! "))
desiredAnswer1 = 5
ageGuessed1 = 5 - abs(userResponce1 - desiredAnswer1)
print("Next Question ")

#Question 2
userResponce2 = int(input("I grew up with Call of Duty! "))
desiredAnswer2 = 1
ageGuessed2 = 5 - abs(userResponce2 - desiredAnswer2)
print("Next Question ")

#Question 3
userResponce3 = int(input("Pokemon was my childhood! "))
desiredAnswer3 = 1
ageGuessed3 = 5 - abs(userResponce3 - desiredAnswer3)
print("Next Question ")

#Question 4
userResponce4 = int(input("Do you drive a newer car? "))
desiredAnswer4 = 5
ageGuessed4 = 5 - abs(userResponce4 - desiredAnswer4)
print("Next Question ")

#Question 5 
userResponce5 = int(input("Do you text people regularly? "))
desiredAnswer5 = 1
ageGuessed5 = 5 - abs(userResponce5 - desiredAnswer5)
print("The results are in! ")

ageScore = (ageGuessed1 + ageGuessed2 + ageGuessed3 + ageGuessed4 + ageGuessed5) * 10
print("Age Score " + str(ageScore))

if totalCompatibility >= 200:
    print("Wow! You are old! Probably at 45 or older")

if totalCompatibility >= 150 and totalCompatibility < 200:
    print("Time to stop celebrating birthdays! You're between 30-45! ")

if totalCompatibility < 150:
print("You've still got it! You're either in your teens, or 20s! " )

