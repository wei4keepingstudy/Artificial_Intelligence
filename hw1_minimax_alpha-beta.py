## 1 2 3 4 5 6 7 8
#h
#g
#f
#e
#d
#c
#b
#a
#C3-D4
import copy
global next_move, nodes_count, max_player, min_player
class StepState:
	"""docstring for stepState"""
	def __init__(self, name, board, parent = None):
		self.name = name
		self.board = board
		self.parent = parent
		self.value = None

def moveOne(oldboard, player, x1, y1, x2, y2):
	board = copy.deepcopy(oldboard)
	
	if player == 'S':
		if abs(x2 - x1) == 1:
			if x2 == 0 and board[x2][y2] != '0':
				board[x2][y2] = board[x2][y2][0] + str(int(board[x2][y2][1]) + 1)
				board[x1][y1] = '0'
			elif x2 != 0 or board[x2][y2] == '0':
				board[x2][y2] = board[x1][y1]
				board[x1][y1] = '0'
		elif abs(x1 - x2) == 2:
			if x2 == 0 and board[x2][y2] != '0':
				board[x2][y2] = board[x2][y2][0] + str(int(board[x2][y2][1]) + 1)
				board[x1][y1] = '0'
				board[(x1 + x2)/2][(y1 + y2)/2] = '0'
			elif x2 != 0 or board[x2][y2] == '0':
				board[x2][y2] = board[x1][y1]
				board[x1][y1] = '0'
				board[(x1 + x2)/2][(y1 + y2)/2] = '0'
		
	elif player == 'C':
		if abs(x2 - x1) == 1:
			if x2 == 7 and board[x2][y2] != '0':
				board[x2][y2] = board[x2][y2][0] + str(int(board[x2][y2][1]) + 1)
				board[x1][y1] = '0'
			elif x2 != 7 or board[x2][y2] == '0':
				board[x2][y2] = board[x1][y1]
				board[x1][y1] = '0'
		elif abs(x1 - x2) == 2:
			if x2 == 7 and board[x2][y2] != '0':
				board[x2][y2] = board[x2][y2][0] + str(int(board[x2][y2][1]) + 1)
				board[x1][y1] = '0'
				board[(x1 + x2)/2][(y1 + y2)/2] = '0'
			elif x2 != 7 or board[x2][y2] == '0':
				board[x2][y2] = board[x1][y1]
				board[x1][y1] = '0'
				board[(x1 + x2)/2][(y1 + y2)/2] = '0'
	return board
	
	
def actions(stepstate, player):
	action = []
	board = stepstate.board
	if player == 'S':
		p_num = 1
	else:
		p_num = -1
	for i, row in enumerate(board):
		for j, state in enumerate(row):

			if state == '0':
				continue
			if state != '0' and state[0] == player:
				if  0 <= i - p_num <= 7 and 0 <= j - 1 <= 7 and board[i - p_num][j-1] == '0':
					action.append(StepState((i, j, i - p_num, j-1), moveOne(board, player,i, j, i - p_num, j-1), stepstate.name))

				elif 0 <= i-p_num <= 7 and 0 <= j - 1 <= 7:
					if board[i - p_num][j-1][0] != player:

						if 0 <= i - p_num*2 <= 7 and 0 <= j - 2 <= 7 and board[i - p_num * 2][j-2] == '0':
							action.append(StepState((i, j, i - p_num*2, j-2), moveOne(board, player,i, j, i - p_num*2, j-2), stepstate.name))
						

						elif (i - p_num*2 == 7 or i - p_num*2 == 0) and board[i - p_num * 2][j-2] != '0' and board[i - p_num * 2][j-2][0] == player:
							action.append(StepState((i, j, i - p_num*2, j-2), moveOne(board, player,i, j, i - p_num*2, j-2), stepstate.name))

					elif (i - p_num == 0 or i - p_num == 7) and board[i - p_num][j-1][0] == player:
						action.append(StepState((i, j, i - p_num, j-1), moveOne(board, player, i, j, i-p_num, j-1),stepstate.name))

				if 0 <= i - p_num <= 7 and 0 <= j + 1 <= 7 and board[i - p_num][j+1] == '0':
					action.append(StepState((i, j, i - p_num, j+1), moveOne(board, player,i, j, i - p_num, j+1), stepstate.name))

				elif 0 <= i-p_num <= 7 and 0 <= j + 1 <= 7:
					if board[i - p_num][j+1][0] != player:
						#print i - p_num*2,board[i - p_num * 2][j+2],board[i - p_num * 2][j-2][0]
						if 0 <= i - p_num*2 <= 7 and 0 <= j + 2 <= 7 and board[i - p_num * 2][j+2] == '0':
							action.append(StepState((i, j, i - p_num*2, j+2), moveOne(board, player,i, j, i - p_num*2, j+2), stepstate.name))
						elif (i - p_num*2 == 7 or i - p_num*2 == 0) and board[i - p_num * 2][j+2] != '0' and board[i - p_num * 2][j+2][0] == player:
							action.append(StepState((i, j, i - p_num*2, j+2), moveOne(board, player,i, j, i - p_num*2, j+2), stepstate.name))


					elif (i - p_num == 0 or i - p_num == 7) and board[i - p_num][j+1][0] == player:
						action.append(StepState((i, j, i - p_num, j+1), moveOne(board, player, i, j, i-p_num, j+1),stepstate.name))

	if not action:
		action.append(StepState('pass', board, stepstate.name))
	#print action[0].name,  action
	return action 




def computeUtility(stepstate):
	res = 0
	#print stepstate.board
	for i, row in enumerate(stepstate.board):
		for j in row:
			if j != '0':
				if j[0] == 'S':
					res += values[7 - i] * int(j[1])
				else:
					res -= values[i] * int(j[1])

	if max_player == 'S':
		return res
	else:
		return res * (-1)

def terminal_test(stepstate, depth, player):
	global nodes_count
	#reach maxdepth
	#print max_depth
	if int(depth) == int(max_depth):
		return True

	#one player left
	star = 0
	cycle = 0
	#print stepstate.board[0] 
	a = stepstate.board
	for i , row in enumerate(a):
		for j in row:
			if j != '0' and j[0] == 'S':
				star += 1
			if j != '0' and j[0] == 'C':
				cycle += 1
	if not (cycle and star):
		return True

	#pass pass
	#print actions(stepstate, player)[0].name
	#if actions(stepstate, player)[0].name == 'pass' and stepstate.name == 'pass':
	#	return True
	#print stepstate.name,actionlist[0].name 
	if actionlist[0].name == 'pass' and stepstate.name == 'pass':
		nodes_count += 1
		return True
	return False


class mini(object):

	def minimax(self, stepstate):
		#print max_player
	    utility = self.max_value(stepstate, max_player, 0)
	    #print next_move.name
	
	    return next_move.name, computeUtility(next_move), utility, nodes_count
	
	
	def max_value(self, stepstate, player, depth):
		global next_move, nodes_count,actionlist
	
		actionlist = actions(stepstate, player)
		#print actionlist
		
		if terminal_test(stepstate, depth, player):
			stepstate.value = computeUtility(stepstate)
			return stepstate.value
	
	
	
		value = -2 ** 32 
		for action in actionlist:
			#print action.name
			nodes_count += 1
			res = self.min_value(action, min_player, depth + 1)
			#print action.name
			if res > value:
				if action.parent == 'root':
					next_move = action
					#print next_move.name
				value = res
		return value
		
	def min_value(self, stepstate, player, depth):
		global nodes_count, actionlist
		actionlist = actions(stepstate, player)
		if terminal_test(stepstate, depth, player):
			stepstate.value = computeUtility(stepstate)
			return stepstate.value
	
		value = 2 ** 32 -1
		for action in actionlist:
			#print action.name
			nodes_count += 1
			value = min(value, self.max_value(action, max_player,depth + 1))
	
		return value

class ab(object):
		
	def alphabeta(self, stepstate):
		#print max_player
	    utility = self.max_valueab(stepstate, max_player, 0, -2 ** 32, 2 ** 32 -1)
	    #print next_move.name
	
	    return next_move.name, computeUtility(next_move), utility, nodes_count
	
	def max_valueab(self, stepstate, player, depth, alpha, beta):
		global next_move, nodes_count,actionlist
	
		actionlist = actions(stepstate, player)
		#print actionlist
		
		if terminal_test(stepstate, depth, player):
			stepstate.value = computeUtility(stepstate)
			return stepstate.value
	
	
	
		value = -2 ** 32 
		for action in actionlist:
			#print action.name
			nodes_count += 1
			res = self.min_valueab(action, min_player, depth + 1, alpha, beta)
			#print action.name
			if res > value:
				if action.parent == 'root':
					next_move = action
					#print next_move.name
				value = res
	
			action.alpha = value
			if value >= beta:
			    return value
			alpha = max(alpha, value)
		return value
		
	def min_valueab(self, stepstate, player, depth, alpha, beta):
		global nodes_count, actionlist
		actionlist = actions(stepstate, player)
		if terminal_test(stepstate, depth, player):
			stepstate.value = computeUtility(stepstate)
			return stepstate.value
	
		value = 2 ** 32 -1
		for action in actionlist:
			#print action.name
			nodes_count += 1
			value = min(value, self.max_valueab(action, max_player,depth + 1, alpha, beta))
	
			action.beta = value
			if value <= alpha:
			    return value
			beta = min(alpha, value)
		return value
		
	
def main():
	global max_player, min_player,max_depth,values,next_move,nodes_count
	nodes_count = 1

	fileInput = open("input.txt", "r")
	fileOutput = open("output.txt", "w")
	if not fileInput:
		return None
	max_player = fileInput.readline().strip()
	algorithm = fileInput.readline().strip()
	max_depth = fileInput.readline().strip()
	board = []
	for i in range(8):
		line = fileInput.readline().strip()
		cur = line.split(',')
		board.append(cur)
	values = fileInput.readline().strip()
	values = map(int, values.split(','))
	next_move = None
	if max_player == 'Star':
		max_player = 'S'
		min_player = 'C'
	else:
		min_player = 'S'
		max_player = 'C'
	next_mo = ''
	if algorithm == 'MINIMAX':
		solution = mini()
		next_m, next_value, final_value, nodes_count = solution.minimax(StepState('root', board))
	else:
		solution = ab()
		next_m, next_value, final_value, nodes_count = solution.alphabeta(StepState('root', board))
	
	dic = {0:'H', 1:'G', 2:'F', 3:'E', 4:'D', 5:'C', 6:'B', 7:'A'}
	if next_m != 'pass':
		next_mo = dic[next_m[0]] + str(next_m[1]+1) + '-' + dic[next_m[2]] + str(next_m[3]+1)
	else:
		next_mo = 'pass'

	fileOutput.write(next_mo + '\n' + str(next_value) + '\n' + str(final_value) + '\n' + str(nodes_count))

	fileInput.close()
	fileOutput.close()





if __name__ == '__main__':
	main()