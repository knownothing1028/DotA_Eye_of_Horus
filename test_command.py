import opendota2py
import sys
import json

from opendota2py import Player
from opendota2py import Match
from opendota2py import Hero
sys.path.append('..')
sys.path.append('.')

def chaxun(id):
    player = Player(id)
    print(f"{player.personaname} - {player.mmr_estimate} mmr")

def find_recent_match(id):
    gamer = Player(id)
    matches = gamer.recent_matches
    match_id_list = []
    for i in matches:
        match_id_list.append(i.match_id)
    return match_id_list

def get_info_match_id(match_id):
    """
    single match
    :param match_id:
    :return: all info of this match
    """
    match = Match(match_id)
    return match.players

def get_info_player_match(player_id,match_id):
    """
    get specific player's info in this match
    :param player_id:
    :param match_id:
    :return:
    """
    match_all_players_info = get_info_match_id(match_id)
    for match_info in match_all_players_info:
        if match_info['account_id'] ==player_id:
            return match_info
        else:
            continue
    print("Error!")
    return None

def get_info_recent_matches_player(player_id):
    mtch_id_recent = find_recent_match(player_id)
    mtchs_info_player =[]
    for m_id in mtch_id_recent:
        mtch_info_player = get_info_player_match(player_id,m_id)
        mtchs_info_player.append(mtch_info_player)
    return mtchs_info_player

'''Match_id = 5018080036
Player_id = 143593296

matches_recent_id = find_recent_match(Player_id)
print(matches_recent_id)
info_recent_matches_player = get_info_recent_matches_player(Player_id)
# print(info_recent_matches_player)

count =0
for info in info_recent_matches_player:
    # print('info',info)
    # print('info_gold_reasons',info['gold_reasons'])
    # print('type of info gold',type(info['gold_reasons']))
    if info['gold_reasons'] is None:
        continue
    else:
        keys = info['gold_reasons'].keys()
        if '0' in keys:
            print(info['gold_reasons']['0'])
            count +=info['gold_reasons']['0']
        else:
            print('No 9')

print(count)'''

# m = Match(5018080036)
# for i in m.players:
    # print(i)
    # print('\n')
    # print(i['account_id'])
    # chaxun(i['account_id'])
    # print('\n')
# p = m.players
# p0 = p[0]
# print(p0['account_id'])
# print(p0.keys())
# print(p0['gold_reasons'])
# match = Match(5016567818)


'''
id = 321174338
match_recent = find_recent_match(id)
for mtch_id in match_recent:
    mtch = get_info_match_id(mtch_id)
    play_info = mtch.players
    '''

# p = Player(143593296)
# print(p.recent_matches[0])
# print(p.rankings)

if __name__ == '__main__':
	cmd = sys.argv[1]
	if cmd.lower() == 'mmr':
		Player_id = int(sys.argv[2])
		chaxun(Player_id)
    
	if cmd.lower() == 'farm':
		Player_id = int(sys.argv[2])
		matches_recent_id = find_recent_match(Player_id)
		info_recent_matches_player = get_info_recent_matches_player(Player_id)
		sum_of_ten_matches = 0
		count = 0
		for info in info_recent_matches_player:
			total_prop = 0
			if info['gold_reasons'] is None:
				continue
			else:
				keys = info['gold_reasons'].keys()
				for key in keys:
					total_prop += info['gold_reasons'][key]
				print('Match ID: ' + str(info['match_id']))
				print('total_property: ' + str(total_prop))
				print(' ')
				sum_of_ten_matches += total_prop
				count += 1
		ave_of_ten_matches = sum_of_ten_matches / count
		print('Average property of past 10 matches: ' + str(int(ave_of_ten_matches)))