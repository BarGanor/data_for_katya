import pandas as pd
import openpyxl
import xlrd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

path = '/Users/YG/PycharmProjects/data_for_katya/No_Duplicates.xlsx'

df = pd.read_excel(path)


def setEmptySeries(series, year):
    missingYearSeries = series
    missingYearSeries.at['year_rdate'] = year
    missingYearSeries.at['month_rdate'] = float('NaN')
    missingYearSeries.at['round_num'] = float('NaN')
    missingYearSeries.at['RoundType'] = float('NaN')
    missingYearSeries.at['round amount'] = float('NaN')
    missingYearSeries.at['stage_num'] = float('NaN')
    missingYearSeries.at['OtherInvestors'] = float('NaN')
    missingYearSeries.at['ForeignInvestors'] = float('NaN')
    missingYearSeries.at['IsraeliVCInvestors'] = float('NaN')
    return missingYearSeries


counter = 0

groupedByName = df.groupby('CompanyFullName')
print('initial' + str(df.shape))

for group in groupedByName:
    yearsInGroup = []
    for row in range(len(group[1])):
        temp = group[1].iloc[row]
        yearsInGroup.append(temp['year_rdate'])

    for year in range(2003, 2020):
        if year not in yearsInGroup:
            df = df.append(setEmptySeries(group[1].iloc[0], year), ignore_index=True)

    print(group[1].iloc[0]['CompanyFullName'])
    counter += 1

    if counter == 10:
        break

print(df.shape)

newGrouped = df.groupby('CompanyFullName')
for group in newGrouped:
    print(group[1].sort_values('year_rdate'))

######### Use the excel files you fixed (those who are inside)
