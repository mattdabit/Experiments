import xlsxwriter
import os
from feedback import *
def createFile(subj, trial_type, player_times, std, m, r_std, r_m):
	os.chdir('/home/matt/Documents/Drummer Experiment/Data')
	workbk = xlsxwriter.Workbook(('%s.xlsx')%subj)
	worksheet = workbk.add_worksheet()
	worksheet.write(0, 0, "Subject")
	worksheet.write(0, 1, 'Trial')
	worksheet.write(0, 2, 'Trial Block')
	worksheet.write(0, 3, 'Trial by Block')
	worksheet.write(0, 4, "Trial Type")
	worksheet.write(0, 5, "Player Times")
	worksheet.write(0, 6, "Frequency of Tapping")
	worksheet.write(0, 7, "STDEV")
	worksheet.write(0, 8, "MEAN")
	worksheet.write(0, 9, "Rounded Frequency of Tapping")
	worksheet.write(0, 10, "Rounded STDEV")
	worksheet.write(0, 11, "Rounded MEAN")

	#Subj name
	col = 0
	row = 1
	while row <501:
		worksheet.write(row, col, subj)
		row+=1

	#Trial Number
	row = 1
	col +=1
	while row < 501:
		worksheet.write(row, col, row)
		row+=1

	#Trial block
	row = 1
	col +=1
	i = 1
	while row < 501:
		for x in range(25):
			worksheet.write(row, col, i)
			row+=1
		i+=1
	#Trial block
	row = 1
	col +=1
	i = 1
	while row < 501:
		i = 1
		for x in range(25):
			worksheet.write(row, col, i)
			row+=1
			i+=1


	#Trial Type
	row = 1
	col += 1
	for item in trial_type:
		for i in range(250): 
			worksheet.write(row, col, item)
			row+=1
		row = 251

	#Player times
	row = 1
	col+=1
	for i in range(len(player_times)):
		worksheet.write(row, col, player_times[i])
		row+=1

	#freq of tapping
	col+=1
	row = 2
	diff = rate(player_times)
	for i in range(len(diff)):
		if diff[i] > 5000:
			worksheet.write(row, col, "")
			row+=1
		else:
			worksheet.write(row, col, diff[i])
			row+=1

	#standard deviation
	col+=1
	row = 1
	for item in std:
		worksheet.write(row, col, int(item))
		row+=25

	#Mean
	col+=1
	row = 1
	for item in m:
		worksheet.write(row, col, int(item))
		row+=25

	#Rounded Delta of player times
	r_diff = round_rate(player_times)

	col+=1
	row =2
	for i in range(len(r_diff)):
		if r_diff[i] > 5000:
			worksheet.write(row, col, "")
			row+=1
		else:
			worksheet.write(row, col, r_diff[i])
			row+=1

	#rounded std
	col+=1
	row = 1
	for item in r_std:
		worksheet.write(row, col, int(item))
		row+=25

	#rounded mean
	col+=1
	row = 1
	for item in r_m:
		worksheet.write(row, col, int(item))
		row+=25

	workbk.close()