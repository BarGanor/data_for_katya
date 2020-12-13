import pandas as pd
import xlrd
import openpyxl


########    Separate between multiple and single lines   #####
def getOneLiners(path):
    df = pd.read_excel(path)
    df = df.drop(columns='Unnamed: 0')

    listOfDF = []

    grouped = df.groupby(df.CompanyFullName)

    for name, group in grouped:
        if group.shape[0] == 1:
            listOfDF.append(group)

    noOneLineDF = pd.concat(listOfDF)

    return noOneLineDF


def getMultipleLiners(path):
    df = pd.read_excel(path)
    df = df.drop(columns='Unnamed: 0')

    listOfDF = []

    grouped = df.groupby(df.CompanyFullName)

    for name, group in grouped:
        if group.shape[0] > 1:
            listOfDF.append(group)

    noOneLineDF = pd.concat(listOfDF)

    return noOneLineDF


def checkIfDup(df):
    if all([df['year_rdate'], df['month_rdate'], df['round_num'], df['RoundType']]):
        return True
    else:
        return False


def checkDups(df):
    grouped = df.groupby(df.Reg_Num)
    for group in grouped:
        temp = None
        for row in range(len(group[1])):
            try:
                if checkIfDup(group[1].iloc[row] == temp):
                    print(row)
                    print(group)
            except:
                print("except")

            temp = group[1].iloc[row]


def concatAllDFs(oneLine, multipleLines, mainSheet):
    check_for_nan = pd.DataFrame(mainSheet['Reg_Num'].isnull())

    noCompanyID = []
    for row in range(len(check_for_nan)):
        if check_for_nan.iloc[row]['Reg_Num'] == True:
            noCompanyID.append(mainSheet.iloc[row])

    noCompanyID = pd.DataFrame(noCompanyID).drop(["check_doubles"], axis=1)
    print(noCompanyID.shape)
    noCompanyID.to_excel("NoCompanyID.xlsx")
    finishedDF = oneLine.append(multipleLines).append(noCompanyID).reset_index()

    finishedDF = finishedDF.drop(["index", "check_doubles", "Unnamed: 0"], axis=1)
    finishedDF = finishedDF.drop_duplicates()
    return finishedDF


def dfToExcel(df, fileName):
    df.to_excel(fileName)


#   Main sheet
mainSheetPath = "/Users/YG/Desktop/משרד האוצר/firstsheet.xlsx"
mainSheetDF = pd.read_excel(mainSheetPath)

#   Single line
singleLine = getOneLiners(mainSheetPath)
singleLine.to_excel("Single_Lines.xlsx")

#   Multiple lines
multipleLines = getMultipleLiners(mainSheetPath)
singleLine.to_excel("Multiple_Lines.xlsx")

#   Check for duplicates
multipleLines = multipleLines[multipleLines.check_doubles == 0]
multipleLines = multipleLines.drop(["check_doubles"], axis=1)
checkDups(multipleLines)  # Print all suspected duplicates

#   Concat all data-frames
concatinatedDF = concatAllDFs(singleLine, multipleLines, mainSheetDF)


