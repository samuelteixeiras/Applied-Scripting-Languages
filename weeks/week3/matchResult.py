# Program to get match result
# Student ID: 00291713 

homeTeamName = input("Home team name? ")
homeTeamScore = int(input("Home team score? "))
awayTeamName = input("Away team name? ")
awayTeamScore = int(input("Away team score? "))

if homeTeamScore > awayTeamScore:
    print(f"Winner is {homeTeamName}")
elif awayTeamScore > homeTeamScore:
    print(f"Winner is {awayTeamName}")
else:    
    print("Draw")