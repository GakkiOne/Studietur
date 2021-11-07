import pandas as pd
import matplotlib.pyplot as plt

def sorting(index):
    studietur = pd.read_csv('DailyStep.csv')
    allvalues = studietur[studietur.columns[0]].tolist()
    dailysteps = []
    for c in range(len(allvalues)):
        data = allvalues[c].split(";")
        dailysteps.append(data[index])
    return dailysteps

def values_to_int(listOfString):
    listOfInts = []
    if type(listOfString[0]) == str:
        for i in listOfString:
            listOfInts.append(int(i))
    return listOfInts

def values_to_float(listOfString):
    listOfFloat = []
    if type(listOfString[0]) == str:
        for i in listOfString:
            listOfFloat.append(float(i))
    return listOfFloat

def date_split(date):
    days = []
    for i in range(len(date)):
        days.append(date[i][5:10])
    return days

def plot(data,label):
    plt.plot(date, data)
    plt.xlabel("Date")
    plt.ylabel(label)
    plt.show()

steps = values_to_int(sorting(1))
date = date_split(sorting(0))
calories = values_to_int(sorting(4))
floors = values_to_int(sorting(5))
distance = values_to_float(sorting(3))

plot(steps,"steps")
plot(calories,"Kcal")
plot(floors,"floors")
plot(distance,"distance")

