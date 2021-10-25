filename = "../csvs/hurling_finalists.csv"

countiesList = []
winsList = []
lastWinList = []
finalLossesList = []
lastLosingFinalList = []
finalWinRatioList = []

try:
    with open(filename) as file:
        headers = file.readline()

        while (line := file.readline().rstrip()):
            county, wins, lastWin, finalLosses, lastLosingFinal, finalWinRatio = line.split(",")
            countiesList.append(county)
            winsList.append(int(wins))
            lastWinList.append(lastWin)
            finalLossesList.append(int(finalLosses))
            lastLosingFinalList.append(lastLosingFinal)
            finalWinRatioList.append(float(finalWinRatio.rstrip("%")))

            

    print(len(countiesList))
    print(sum(winsList))
    print(f"{sum(winsList)/ len(countiesList):.1f}")
    print(countiesList[lastWinList.index("2021")])
    print(countiesList[winsList.index(max(winsList))])
    print(countiesList[finalWinRatioList.index(max(finalWinRatioList))])


except FileNotFoundError as e:
    print(f"Error {filename} not found, {e}")   

