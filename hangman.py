from random import randint
 
def find_indices(word, c):
	l = len(word)
	n = list()
	for i in range(0,l):
		if(c == word[i]):
			n.append(i)
	return n

def play_round(word, gaali, chances_remaining):
	final = ''
	l = len(word)
	final_list = list('_') * l
	hangman = "HANGMAN"
	score = 0
	count = 0
	print ' '.join(final_list)
	while(chances_remaining > 0 and l > 0):
		a = raw_input("\nenter character: ")
		if(a in word and not(a in final)):
			score += 1
			index_list = find_indices(word, a)
			list_len = len(index_list)
			for i in range(0, list_len):
				final_list[index_list[i]] = a
				l -= 1
			final = ' '.join(final_list)
			print final + '\tscore: ', str(score) + '\tcharacters remaining: ' + str(l)
		elif(a in final):
			print gaali[randint(0,3)]
			chances_remaining -= 1
			count += 2
			print hangman[0:count] + '\tscore: ' + str(score)  + '\tchances remaining: ', chances_remaining
		else:
			chances_remaining -= 1
			count += 2
			print hangman[0:count] + '\tscore: ' + str(score) + '\tchances remaining: ', chances_remaining
	data = [chances_remaining, l, score]
	return data
 
def hangman():
	quit = 'no'
	gaali = ['\nchut! kitni baar likhega', '\ngaand maar li jayegi, phir likha toh', '\ndobara likhna mana hai', '\nmaa chuda, chakke']
	dict_file = open('dict.txt', 'r').read().split('\n')
	user_file = open('user_file.txt', 'a')
	name = raw_input("enter name: ")
	level = raw_input("enter difficulty level[e: easy, m: medium, h: hard]: ")
	d_level = {'e': [3, 5, 3, 'easy'], 'm': [6, 8, 4, 'medium'], 'h': [9, 15, 4, 'hard']} #[start length, end length, chances, level]
	user_file.write("user: " + name + "\tlevel: " + d_level[level][3] + "\n")
	print "\nlet's start the game, "  + name + "!!"
	score_list = [0, 0, 0] #[max_score, total_score, round_count]
	
	while(quit == 'no'):
		flag = 0
		score_list[2] += 1
		print '\nRound: ' + str(score_list[2])
		while(flag == 0):
			word = dict_file[randint(0, len(dict_file)-1)]
			word_len = len(word)
			if(word_len <= d_level[level][1] and word_len >= d_level[level][0]):
				flag = 1
		data = play_round(word, gaali, d_level[level][2])
		if(data[0] > 0 and data[1] == 0):
			print '\n\n***************\nYAY! YOU WIN :D\n***************\n\n'
		if(data[0] == 0):
			print '\nthe correct word is: ' + word
		if(data[2] > score_list[0]):
			score_list[0] = data[2]
		score_list[1] += data[2]
		user_file.write('score: ' + str(data[2]) + '\tmax_score: ' + str(score_list[0]) + '\n')
		quit = raw_input("\nwant to quit (yes/no): ")

	user_file.write("total score in this session: " + str(score_list[1]) + "\n\n")
	user_file.close()

if __name__ == "__main__":
	hangman()

