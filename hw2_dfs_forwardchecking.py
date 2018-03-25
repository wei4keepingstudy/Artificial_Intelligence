import math
def check_full(visited):
	if potsNumSum == len(visited):
		return True
	return False

def dfs(cur, res, visited):
	if check_full(visited):
		return True
	for i in range(len(cur)):
		if cur[i]:
			flag = False
			team = cur[i][0]
			for j in range(group_num):
				#print a[x][y][0], res[x][0]
				if all(team[0] != p[0] for p in res[j]) and (all(team[-1] != q[-1] for q in res[j]) or (sum(w[-1] == 'f' for w in res[j] ) < 2 and team[-1] =='f')):
					res[j].append(team)
					cur[i].remove(team)
					visited.add(team)
					flag = True
					#print res, i, j, visited
					#if check_full(visited):
					#	print "?????"
					#	return True 
					#else:
					#	if y != len(res[x])-1:
					#		if dfs(cur, res, x, y+1, visited):
					#			return True
					#	elif x != len(res)-1:
					#		if dfs(cur, res, x+1, 0, visited):
					#			return True
					#	if i == 0:
					#		return False
					if dfs(cur, res, visited):
						return True
					if i == 0:
						return False
	
					res[j].remove(team)
					cur[i].insert(0,team)
					visited.remove(team)
					flag = False
		
				
			if not flag:
				return False
	







if __name__ == '__main__':
	fileInput = open("input.txt", "r")
	fileOutput = open("output.txt", "w")
	if not fileInput:
		fileOutput.write('No') 

	group_num = int(fileInput.readline().strip())
	pot_num = int(fileInput.readline().strip())

	pots = [] #pot
	for i in range(pot_num):
		line = fileInput.readline().strip()
		line = line.split(',')
		line = [str(i) + x for x in line]
		pots.append(line)


	ifSolution = True
	cur = [[]for _ in range(len(pots))]
	confederations = []
	afc = []
	caf = []
	concacaf = []
	conmebol = []
	ofc = []
	uefa = []
	for i in range(6):
		line = fileInput.readline().strip().replace(':', ',')
		line = line.split(',')
		if line[0] == 'AFC':
			if line[1] != 'None':
				afc = line[1:]
		elif line[0] == 'CAF':
			if line[1] != 'None':
				caf = line[1:]
		elif line[0] == 'CONCACAF':
			if line[1] != 'None':
				concacaf = line[1:]
		elif line[0] == 'CONMEBOL':
			if line[1] != 'None':
				conmebol = line[1:]
		elif line[0] == 'OFC':
			if line[1] != 'None':
				ofc = line[1:]
		elif line[0] == 'UEFA':
			if line[1] != 'None':
				uefa = line[1:]

	for i in range(len(pots)):
		for j in range(len(pots[i])):
			if pots[i][j][1:] in afc:
				cur[i].append(pots[i][j] + 'a')
			elif pots[i][j][1:] in caf:
				cur[i].append(pots[i][j] + 'b')
			elif pots[i][j][1:] in concacaf:
				cur[i].append(pots[i][j] + 'c')
			elif pots[i][j][1:] in conmebol:
				cur[i].append(pots[i][j] + 'd')
			elif pots[i][j][1:] in ofc:
				cur[i].append(pots[i][j] + 'e')
			elif pots[i][j][1:] in uefa:
				cur[i].append(pots[i][j] + 'f')
	confederations.append(afc)
	confederations.append(caf)
	confederations.append(concacaf)
	confederations.append(conmebol)
	confederations.append(ofc)
	confederations.append(uefa)

	#pigeon cage rule
	potsNum = map(len, pots)
	confederationsNum = map(len, confederations)
	if any(group_num < x for x in potsNum) or any(group_num < x for x in confederationsNum[:-1]) or (2 * group_num < confederationsNum[-1]):
		ifSolution = False

	res = []
	total = group_num
	potsNumSum = sum(potsNum)
	#print cur
	if ifSolution:
		#while total >0:
		#	maxNuminGroup = math.ceil(float(potsNumSum) / total)
		#	res.append([0 for _ in range(int(maxNuminGroup))])
		#	total -= 1
		#	potsNumSum -= maxNuminGroup

		#res = [[0 for _ in range(int(maxNuminGroup))] for _ in range(group_num-1)]
		#res.append([0 for _ in range(sum(potsNum)- int(maxNuminGroup)*(group_num-1))])
		res = [[] for _ in range(group_num)]
		#print res
		#visited = [[0 for _ in range(len(pots[i]))] for i in range(len(pots))]
		visited = set()
		dfs(cur, res, visited)
		fileOutput.write('Yes' + '\n')
		ans = [[y[1:-1] for y in x ] for x in res]
		for line in ans:
			if line:
				fileOutput.write(','.join(line) + '\n')
			else:
				fileOutput.write('None'+ '\n')

	else:
		fileOutput.write('No')


	fileInput.close()
	fileOutput.close()



	
