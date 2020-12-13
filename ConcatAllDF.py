import pandas as pd
import xlrd

pd.set_option('display.expand_frame_repr', False)

noOneLine = pd.read_excel("/Users/YG/PycharmProjects/data_for_katya/Multiple_Lines.xlsx")
oneLine = pd.read_excel("/Users/YG/PycharmProjects/data_for_katya/Single_Lines.xlsx")

mainSheet = pd.read_excel("/Users/YG/Desktop/משרד האוצר/firstsheet.xlsx")

check_for_nan = pd.DataFrame(mainSheet['Reg_Num'].isnull())

noCompanyID = []
for row in range(len(check_for_nan)):
    if check_for_nan.iloc[row]['Reg_Num'] == True:
        noCompanyID.append(mainSheet.iloc[row])

noCompanyID = pd.DataFrame(noCompanyID).drop(["check_doubles"], axis=1)
print(noCompanyID.shape)
noCompanyID.to_excel("NoCompanyID.xlsx")
finishedDF= oneLine.append(noOneLine).append(noCompanyID).reset_index()

finishedDF = finishedDF.drop(["index", "check_doubles", "Unnamed: 0"], axis=1)
finishedDF = finishedDF.drop_duplicates()
finishedDF.to_excel("No_Duplicates.xlsx")



