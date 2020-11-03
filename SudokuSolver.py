
#creat sudoku board
sudokuBorad = [
	[6,0,0,1,0,0,0,0,2],
	[8,0,1,0,9,0,0,0,0],
	[0,7,5,0,8,4,0,0,0],
	[4,3,0,0,2,0,5,6,1],
	[5,1,8,7,0,0,4,0,9],
	[0,9,6,4,1,0,3,0,0],
	[0,0,0,0,7,0,0,0,0],
	[0,6,0,0,3,1,0,5,0],
	[7,0,2,5,4,0,6,0,3],
	]



#choices
#delcared a list with all the possible numbers in sudoku
possibleNumbers = [1,2,3,4,5,6,7,8,9]
counter = 0
#constrains 
def checkBoard():
	for nums in sudokuBorad:
		counter =+ 1
		print("break")
		print (counter)
		if counter < 2:
			for num2 in nums:
				print(num2)

checkBoard()
#does it break the row 
#does it break the colunm
#does it break the sub-grid 

#goal is to fill in all 0s 
# pre decalred sudokuBorad
