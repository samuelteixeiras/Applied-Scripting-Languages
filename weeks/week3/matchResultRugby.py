# Program to get match result
# Student ID: 00291713 

homeTeamName = input("Name of the home team: ")
homeTeamScore = int(input("Home team score: "))
homeTeamTries = int(input("Number of tries scored by the home team: "))

awayTeamName = input("Name of the away team: ")
awayTeamScore = int(input("Away team score: "))
awayTeamTries = int(input("Number of tries scored by the away team: "))


homeTeamPoints = 0
awayTeamPoints = 0
if homeTeamScore > awayTeamScore:
    homeTeamPoints +=4 
    if (homeTeamScore - awayTeamScore <= 7):
        awayTeamPoints +=1
elif awayTeamScore > homeTeamScore:
    awayTeamPoints +=4 
    if (awayTeamScore - homeTeamScore  <= 7):
        homeTeamPoints +=1
else:
    homeTeamPoints +=2 
    awayTeamPoints +=2 

if homeTeamTries >= 4:
    homeTeamPoints +=1 

if awayTeamTries >= 4:
    awayTeamPoints +=1 

print(f"{homeTeamName} awarded {homeTeamPoints} championship points")
print(f"{awayTeamName} awarded {awayTeamPoints} championship points")
