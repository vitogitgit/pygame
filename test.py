# -*- coding: utf-8 -*-

if __name__ == '__main__':
	score_list , name_list = [] , []
	with open ('Leaderboard.txt' , 'r') as f:
		txt_lines = f.readlines()
		for line in txt_lines:
			line = line.split('-%-')
			score_list.append(int(line[1][:-1]))
			name_list.append(line[0])
	print score_list
	print name_list
	userScore = input('score:')
	updateList = False
	for i in score_list:
		if userScore > i: updateList = True
	if updateList:
		userName = raw_input('your name:')
		print type(userName)
		score_list.pop()
		name_list.pop()
		score_list.append(userScore)
		score_list.sort(reverse=True)
		for i , eachScore in enumerate(score_list):
			if eachScore == userScore: userIndex = i
		name_list.insert(userIndex , userName)
		print score_list
		print name_list
		with open ('Leaderboard.txt' , 'w') as f:
			for i in range(5):
				f.write(name_list[i]+'-%-'+str(score_list[i])+'\n')
	

'''
cd /Users/littlevito/Desktop/test_automation/pythonGOGO/pygame/hitAircraft
python test.py
'''