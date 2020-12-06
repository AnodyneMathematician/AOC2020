import csv
CurrentList = []
CurrentList2 = []
CurrentList3 = []
QuestionsAnswered = 0
QuestionsAnswered2 = 0
with open("InputAdventofCodeDay6 2020.csv",  newline='')as csvfile:
    inpt = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in inpt:
        if row == []:
            QuestionsAnswered += len(CurrentList)
            CurrentList = []
            QuestionsAnswered2 += len(CurrentList2)
            CurrentList2 = []
        else:
            row = list(row[0])
            if CurrentList == []:
                for i in range(len(row)):
                    CurrentList2.append(row[i])
            else:
                CurrentList3 = []
                for i in range(len(CurrentList2)):
                    if CurrentList2[i] in row:
                        CurrentList3.append(CurrentList2[i])
                CurrentList2 = CurrentList3
            for i in range(len(row)):
                if row[i] not in CurrentList:
                    CurrentList.append(row[i])
        
print("Pt 1;",QuestionsAnswered + len(CurrentList))
print("Pt 2;",QuestionsAnswered2 + len(CurrentList2))

