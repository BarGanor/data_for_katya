import pandas as pd
import xlrd

pd.set_option('display.expand_frame_repr', False)

df = pd.read_excel("/Users/YG/PycharmProjects/data_for_katya/Multiple_Lines.xlsx")
df = df[df.check_doubles == 0]
df = df.drop(["check_doubles"], axis=1)

grouped = df.groupby(df.Reg_Num)


def checkIfDup(df):
    if all([df['year_rdate'], df['month_rdate'], df['round_num'], df['RoundType']]):
        return True
    else:
        return False


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

