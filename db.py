#Databas connection module


#make MongoDB connections here
# TO DO

ppgList = []
temperatureList = []

def insertIntoDB(xList, flag):
    #write code to insert the elements one by one.
    if flag == 1:
        del ppgList[:]
    elif flag == 2:
        del temperatureList[:]
    

def checkLists():
    if len(ppgList) >= 100:
        insertIntoDB(ppgList, 1)
    elif len(temperatureList) >= 100:
        insertIntoDB(temperatureList, 2)

def putIntoList(x):
    if "*C" in x:
        temperatureList.append(x[:-2])
    else:
        ppg.append(x)
    checkLists()