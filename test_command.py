import opendota2py
import sys
import json

from opendota2py import Player
from opendota2py import Match
from opendota2py import Hero

sys.path.append('..')
sys.path.append('.')


def query_mmr(player_id):
    """
	query mmr with player_id
	:param id:
	:return:
	"""
    player = Player(player_id)
    print(f"{player.personaname} - {player.mmr_estimate} mmr")
    return player.mmr_estimate

def get_personaname(player_id):
    player = Player(player_id)
    return player.personaname

def get_recent_matches_id(player_id):
    """
	get recent matches ID list with player_id
	:param id:
	:return: matches_id_list
	"""
    gamer = Player(player_id)
    matches = gamer.recent_matches
    matches_id_list = []
    for i in matches:
        matches_id_list.append(i.match_id)
    return matches_id_list


def get_players_info_match_id(match_id):
    """
	get  players information of a single match with match id
	:param match_id:
	:return: all info of this match
	"""
    match = Match(match_id)
    return match.players

# error need to be modify
def get_player_info_match_id(player_id, match_id):
    '''
    get a player's information with match id
    :param player_id:
    :param match_id:
    :return:
    '''
    players_info = get_players_info_match_id(match_id)
    for player_info in players_info:
        if player_info['account_id'] == player_id:
            return player_info
        else:
            continue
    print("No such a player in match:", match_id)
    return None


# no specific game mode, need to set more options
def get_player_info_recent_matches(player_id):
    """
	get one player information from his or her recent matches
	no specific game mode
	:param player_id:
	:return: player informations of several recent matches
	"""
    matches_recent_id = get_recent_matches_id(player_id)
    player_info_recent_matches = []
    for mtch_id in matches_recent_id:
        player_info_recent_matches.append(get_player_info_match_id(player_id,mtch_id))
    return player_info_recent_matches


def get_xp_info_player_match(player_id,match_id, prt=False):
    """
    get the experience information of one player in one match
    '0':Unspecified; '1':HeroKill; '2':CreepKill; '3': RoshanKill
    :param player_id:
    :param match_id:
    :return:
    """
    info_player = get_player_info_match_id(player_id,match_id)
    xp_info =info_player['xp_reasons']
    if prt == True:
        for i in info_player.keys():
            if i == '0':
                print('Unspecified:', xp_info[i])
            if i == '1':
                print('HeroKill:', xp_info[i])
            if i == '2':
                print('CreepKill:', xp_info[i])
            if i == '3':
                print('RoshanKill:', xp_info[i])
    return xp_info

def get_totoal_xp(player_id,match_id,prt=False):
    player = Player(player_id)
    info_player = get_player_info_match_id(player_id,match_id)
    if prt == True:
        print("Total XP:",info_player['total_xp'])
    return info_player['total_xp']


def get_xp_info_player_recent_matches(player_id,prt=False):
    """
    get the xp information of ONE player for recent matches
    '0':Unspecified; '1':HeroKill; '2':CreepKill; '3': RoshanKill
    :param player_id:
    :return:list of xp information for recent matches
    """
    xp_info_recent_matches =[]
    matches_recent_id = get_recent_matches_id(player_id)
    for m_id in matches_recent_id:
        xp_info_recent_matches.append(get_xp_info_player_match(player_id,m_id,prt))
    return  xp_info_recent_matches


def get_totoal_gold(player_id,match_id,prt=False):
    player = Player(player_id)
    info_player = get_player_info_match_id(player_id,match_id)
    if prt==True:
        print("Total Gold:",info_player['total_gold'])
    return info_player['total_gold']

# '''Match_id = 5018080036
# Player_id = 143593296
#
# matches_recent_id = find_recent_match(Player_id)
# print(matches_recent_id)
# info_recent_matches_player = get_info_recent_matches_player(Player_id)
# # print(info_recent_matches_player)
#
# count =0
# for info in info_recent_matches_player:
# 	# print('info',info)
# 	# print('info_gold_reasons',info['gold_reasons'])
# 	# print('type of info gold',type(info['gold_reasons']))
# 	if info['gold_reasons'] is None:
# 		continue
# 	else:
# 		keys = info['gold_reasons'].keys()
# 		if '0' in keys:
# 			print(info['gold_reasons']['0'])
# 			count +=info['gold_reasons']['0']
# 		else:
# 			print('No 9')
#
#
#
# # m = Match(5018080036)
# # for i in m.players:
# 	# print(i)
# 	# print('\n')
# 	# print(i['account_id'])
# 	# query_mmr(i['account_id'])
# 	# print('\n')
# # p = m.players
# # p0 = p[0]
# # print(p0['account_id'])
# # print(p0.keys())
# # print(p0['gold_reasons'])
# # match = Match(5016567818)
#
#
# # id = 321174338
# # p = Player(143593296)
# # print(p.recent_matches[0])
# # print(p.rankings)

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd.lower() == 'mmr':
        player_id = int(sys.argv[2])
        query_mmr(player_id)

    if cmd.lower() == 'farm':
        player_id = int(sys.argv[2])
        matches_recent_id = get_recent_matches_id(player_id)
        info_player_recent_matches = get_player_info_recent_matches(player_id)
        sum_of_ten_matches = 0
        count = 0
        for info in info_player_recent_matches:
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
        print('Average property of past', count, 'matches: ' + str(int(ave_of_ten_matches)))

    if cmd.lower() == 'xp':
        if len(sys.argv)==3:
            player_id = int(sys.argv[2])
            prt = False
            get_xp_info_player_recent_matches(player_id,prt)
        if len(sys.argv)==4:
            player_id = int(sys.argv[2])
            if(sys.argv[3] and sys.argv[3]=='True'):
                prt = True
                get_xp_info_player_recent_matches(player_id,prt)
            else:
                match_id = int(sys.argv[3])
                get_xp_info_player_match(player_id,match_id)

