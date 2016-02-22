file = open('/Users/luciomelito/Documents/Python/Project Euler/Problem22Data.txt').read().split(",")

names = []

for line in file:
    names.append(line[1:-1])
 
names.sort()   

totalScore = 0
possibleLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(0, len(names)):
    score = 0
    for letter in names[i]:
        score += possibleLetters.index(letter) + 1
    score *= i+1
    totalScore += score
    
print totalScore