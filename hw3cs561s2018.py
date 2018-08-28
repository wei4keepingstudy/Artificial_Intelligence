import copy

#for up&down
#l, r is the absolute position of our action(direction)
#l is always the leftpart of grid, r is always the right part of grid
#for left&right
#l is always below part, r is always up part
def check(i, j, action):
	still = 0
	#111111
	if action == 'walkup' or action == 'walkdown':
		if j - 1 > 0 and (i, j - 1) not in wallCellPosition:
			l = (1 - pwalk) * 0.5
		else:
			l = 0
			still += (1 - pwalk) * 0.5
		if j + 1 < columns + 1 and (i, j + 1) not in wallCellPosition:
			r = (1 - pwalk) * 0.5
		else:
			r = 0
			still += (1 - pwalk) * 0.5
		if action == 'walkup':
			if i + 1 < rows + 1 and (i + 1, j) not in wallCellPosition:
				direction = pwalk 
			else:
				direction = 0
				still += pwalk
		else:
			if i - 1 > 0 and (i - 1, j) not in wallCellPosition:
				direction = pwalk 
			else:
				direction = 0
				still += pwalk
	#222222222
	if action == 'runup' or action == 'rundown':
		if j - 2 > 0 and (i, j - 2) not in wallCellPosition and (i, j - 1) not in wallCellPosition:
			l = (1 - prun) * 0.5
		else:
			l = 0
			still += (1 - prun) * 0.5
		if j + 2 < columns + 1 and (i, j + 2) not in wallCellPosition and (i, j + 1) not in wallCellPosition:
			r = (1 - prun) * 0.5
		else:
			r = 0
			still += (1 - prun) * 0.5
		if action == 'runup':
			if i + 2 < rows + 1 and (i + 2, j) not in wallCellPosition and (i + 1, j) not in wallCellPosition:
				direction = prun 
			else:
				direction = 0
				still += prun
		else:
			if i - 2 > 0 and (i - 2, j) not in wallCellPosition and (i - 1, j) not in wallCellPosition:
				direction = prun 
			else:
				direction = 0
				still += prun
	#3333333
	if action == 'walkleft' or action == 'walkright':
		if i - 1 > 0 and (i - 1, j) not in wallCellPosition:
			l = (1 - pwalk) * 0.5
		else:
			l = 0
			still += (1 - pwalk) * 0.5
		if i + 1 < rows + 1 and (i + 1, j) not in wallCellPosition:
			r = (1 - pwalk) * 0.5
		else:
			r = 0
			still += (1 - pwalk) * 0.5
		if action == 'walkright':
			if j + 1 < columns + 1 and (i, j + 1) not in wallCellPosition:
				direction = pwalk 
			else:
				direction = 0
				still += pwalk
		else:
			if j - 1 > 0 and (i, j - 1) not in wallCellPosition:
				direction = pwalk 
			else:
				direction = 0
				still += pwalk
	#4444444
	if action == 'runleft' or action == 'runright':
		if i - 2 > 0 and (i - 2, j) not in wallCellPosition and (i - 1, j) not in wallCellPosition:
			l = (1 - prun) * 0.5
		else:
			l = 0
			still += (1 - prun) * 0.5
		if i + 2 < rows + 1 and (i + 2, j) not in wallCellPosition and (i + 1, j) not in wallCellPosition:
			r = (1 - prun) * 0.5
		else:
			r = 0
			still += (1 - prun) * 0.5
		if action == 'runright':
			if j + 2 < columns + 1 and (i, j + 2) not in wallCellPosition and (j + 1) not in wallCellPosition:
				direction = prun 
			else:
				direction = 0
				still += prun
		else:
			if j - 2 > 0 and (i, j - 2) not in wallCellPosition and (j - 1) not in wallCellPosition:
				direction = prun 
			else:
				direction = 0
				still += prun
	return l, r, direction, still



def calculate(l, r, direction, still, utility, action, i, j):
	part1, part2, part3, part4 = 0, 0, 0, 0
	if action == 'walkup' or action == 'walkdown':
		if l != 0:
			part1 = l * utility[rows - i][j - 2]
		if r != 0:
			part2 = r * utility[rows - i][j]
		if direction != 0 and action == 'walkup':
			part3 = direction * utility[rows - i - 1][j - 1]
		if direction != 0 and action == 'walkdown':
			part3 = direction * utility[rows - i + 1][j - 1]
		if still != 0:
			part4 = still * utility[rows - i][j - 1]

	if action == 'runup' or action == 'rundown':
		if l != 0:
			part1 = l * utility[rows - i][j - 3]
		if r != 0:
			part2 = r * utility[rows - i][j + 1]
		if direction != 0 and action == 'runup':
			part3 = direction * utility[rows - i - 2][j - 1]
		if direction != 0 and action == 'rundown':
			part3 = direction * utility[rows - i + 2][j - 1]
		if still != 0:
			part4 = still * utility[rows - i][j - 1]

	if action == 'walkleft' or action == 'walkright':
		if l != 0:
			part1 = l * utility[rows - i + 1][j - 1]
		if r != 0:
			part2 = r * utility[rows - i - 1][j - 1]
		if direction != 0 and action == 'walkleft':
			part3 = direction * utility[rows - i][j - 2]
		if direction != 0 and action == 'walkright':
			part3 = direction * utility[rows - i][j]
		if still != 0:
			part4 = still * utility[rows - i][j - 1]

	if action == 'runleft' or action == 'runright':
		if l != 0:
			part1 = l * utility[rows - i + 2][j - 1]
		if r != 0:
			part2 = r * utility[rows - i - 2][j - 1]
		if direction != 0 and action == 'runleft':
			part3 = direction * utility[rows - i][j - 3]
		if direction != 0 and action == 'runright':
			part3 = direction * utility[rows - i][j + 1]
		if still != 0:
			part4 = still * utility[rows - i][j - 1]
		
	return part1, part2, part3, part4

def policy(res, utility, cur):
	#print utility
	#cur = [[0 for _ in range(columns)] for _ in range(rows)]
	#print terminalPositionReward
	flag = 0
	while True:
		for i in range(rows, 0, -1):
			for j in range(1, columns + 1):
				#print (i, j)
				if (i, j) in wallCellPosition:
					res[rows - i][j - 1] = 'None'
					continue
				if (i, j) in terminalPositionReward:
					res[rows - i][j - 1] = 'Exit'
					continue

				l, r, direction, still = check(i, j, 'walkup')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'walkup', i, j)
				walkup = float(str(rwalk + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'walkdown')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'walkdown', i, j)
				walkdown = float(str(rwalk + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'walkleft')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'walkleft', i, j)
				walkleft = float(str(rwalk + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'walkright')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'walkright', i, j)
				walkright = float(str(rwalk + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'runup')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'runup', i, j)
				runup = float(str(rrun + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'rundown')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'rundown', i, j)
				rundown = float(str(rrun + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'runleft')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'runleft', i, j)
				runleft = float(str(rrun + discount * (part1 + part2 + part3 + part4)))

				l, r, direction, still = check(i, j, 'runright')
				part1, part2, part3, part4 = calculate(l, r, direction, still, cur, 'runright', i, j)
				runright = float(str(rrun + discount * (part1 + part2 + part3 + part4)))

				maxvalue = max(walkup, walkdown, walkleft, walkright, runup, rundown, runleft, runright)
				#if i == rows - 1 and j == 1:
				#	print maxvalue,runup, rundown
				#curans = [walkup, walkdown, walkleft, walkright, runup, rundown, runleft, runright]
				cur[rows - i][j - 1] = maxvalue
				
				#if curans.count(maxvalue) > 1:
				if maxvalue == walkup:
					res[rows - i][j - 1] = 'Walk Up'
				elif maxvalue == walkdown:
					res[rows - i][j - 1] = 'Walk Down'
				elif maxvalue == walkleft:
					res[rows - i][j - 1] = 'Walk Left'
				elif maxvalue == walkright:
					res[rows - i][j - 1] = 'Walk Right'
				elif maxvalue == runup:
					res[rows - i][j - 1] = 'Run Up'
				elif maxvalue == rundown:
					res[rows - i][j - 1] = 'Run Down'
				elif maxvalue == runleft:
					res[rows - i][j - 1] = 'Run Left'
				elif maxvalue == runright:
					res[rows - i][j - 1] = 'Run Right'
				#else:
				#	idx = curans.index(maxvalue)
				#	curference = {0:'Walk Up', 1:'Walk Down', 2:'Walk Left', 3:'Walk Right', 4:'Run Up', 5:'Run Down', 6:'Run Left', 7:'Run Right'}
				#	res[rows - i][j - 1] = curference[idx]
				#if i == rows - 1 and j == 1:
				#	print res[rows - i][j - 1]
				#	print cur[rows - i][j - 1]
				#	print cur[rows - i][j + 1]
				#	print cur[rows - i + 2][j - 1]
				#	print runup, rundown
				#	print cur


		#maxv = 0
		#for i in range(rows, 0, -1):
		#	for j in range(1, columns + 1):
		#		maxv = max(maxv,  utility[rows - i][j - 1] - cur[rows - i][j - 1])

		#if maxv <= 5* 10 ** (-8):
		#	return res
		#flag += 1

		#if flag == 2:
		#	break
		if cur == utility:
			return res
		print cur
		for x in utility:
			print x
		#print res
		print '============='

		utility = copy.deepcopy(cur)

def main():
	global rows, columns, wallCellPosition, terminalPositionReward, pwalk, prun, rwalk, rrun, discount, curference
	fileInput = open("input.txt", "r")
	fileOutput = open("output.txt", "w")
	if not fileInput:
		fileOutput.write('No') 

	gridsizeStr = fileInput.readline().strip()
	gridsize = gridsizeStr.split(',')
	rows = int(gridsize[0])
	columns = int(gridsize[1])

	wallCellNumber = fileInput.readline().strip()
	wallCellPosition = []
	for i in range(int(wallCellNumber)):
		wallpositionline = fileInput.readline().strip()
		wallposition = wallpositionline.split(',')
		x, y = int(wallposition[0]), int(wallposition[1])
		wallCellPosition.append((x, y))

	utility = [[0 for _ in range(columns)] for _ in range(rows)]
	cur = [[0 for _ in range(columns)] for _ in range(rows)]
	terminalNumber = fileInput.readline().strip()
	terminalPositionReward = {}
	for i in range(int(terminalNumber)):
		line = fileInput.readline().strip()
		linesplit = line.split(',')
		x, y = int(linesplit[0]), int(linesplit[1])
		position = (x, y)
		reward = float(linesplit[2])
		terminalPositionReward[position] = reward
		utility[rows - x][y - 1] = reward
		cur[rows - x][y - 1] = reward

	transitionModel = fileInput.readline().strip()
	transitionModelsplit = transitionModel.split(',')
	pwalk, prun = float(transitionModelsplit[0]), float(transitionModelsplit[1])

	rewards = fileInput.readline().strip()
	rewardsSplit = rewards.split(',')
	rwalk, rrun = float(rewardsSplit[0]), float(rewardsSplit[1])

	discount = float(fileInput.readline().strip())


	res = [['' for _ in range(columns)] for _ in range(rows)]
	#utility = [[0 for _ in range(columns)] for _ in range(rows)]
	#curference = {'walkup':7, 'walkdown':6, 'walkleft':5, 'walkright':4, 'runup':3, 'rundown':2, 'runleft':1, 'runright':0}
	#print utility
	result = policy(res, utility, cur)
	#print result
	for arr in result:
		line = ','.join(arr)
		fileOutput.write(line + '\n')

	fileInput.close()
	fileOutput.close()



if __name__ == '__main__':
	main()