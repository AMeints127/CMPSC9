from lab04 import *
def test_example():
	maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze, 4, 4) == True
	assert maze == [
['+', '+', '+', '+', 'G', '+'],
['+', 8, '+', 11, 12, '+'],
['+', 7, 9, 10, '+', '+'],
['+', 6, '+', '+', 2, '+'],
['+', 5, 4, 3, 1, '+'],
['+', '+', '+', '+', '+', '+'] ]
	maze = [
['+','+','+','+','+','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze, 4, 4) == False
	maze = [
['+','G','+','+','+','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ','+',' ','+'],
['+','+','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze, 4, 1) == True
	assert maze == [
['+','G','+','+','+','+'],
['+','10','9','8','7','+'],
['+',' ',' ','+','6','+'],
['+','+','+','+','5','+'],
['+','1','2','3','4','+'],
['+','+','+','+','+','+'] ]
	maze = []
	assert solveMaze(maze, 4, 4) == False
	assert maze == []

	


	
