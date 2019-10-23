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
        if(player_info is None):
            continue
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
    if(xp_info is None):
        print("None")
        return None
    if prt == True:
        print("Match ID is",match_id, "Total Xp is:",info_player['total_xp'])
        for i in xp_info.keys():
            if i == '0':
                print('Unspecified:', xp_info[i],end="    \t")
            if i == '1':
                print('HeroKill:', xp_info[i],end="    \t")
            if i == '2':
                print('CreepKill:', xp_info[i],end="    \t")
            if i == '3':
                print('RoshanKill:', xp_info[i],end="    \t")
        print()
    return xp_info

def get_totoal_xp(player_id,match_id,prt=False):
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
        xp_info = get_xp_info_player_match(player_id,m_id,prt)
        if(xp_info is None):
            continue
        xp_info_recent_matches.append(xp_info)

    return xp_info_recent_matches


def get_gold_info_player_match(player_id,match_id, prt=False):
    """
    get the gold information of one player in one match
    :param player_id:
    :param match_id:
    :return:
    """
    info_player = get_player_info_match_id(player_id,match_id)

    gold_info =info_player['gold_reasons']
    if(gold_info is None):
        print("None")
        return None
    if prt == True:
        print("Match ID is",match_id, "Total GOLD is:",info_player['total_gold'])
        count =0
        l = len(gold_info)
        for i in gold_info.keys():
            if i == '0':
                print('Unspecified:', gold_info[i],end="    \t")
            if i == '1':
                print('DeathLost:', gold_info[i], end="    \t")
            if i == '2':
                print('Buyback:', gold_info[i], end="    \t")
            if i == '3':
                print('PurchaseConsumable:', gold_info[i], end="    \t")
            if i == '4':
                print('PurchaseItem:', gold_info[i], end="    \t")
            if i == '5':
                print('AbandonedRedistribute:', gold_info[i], end="    \t")
            if i == '6':
                print('SellItem:', gold_info[i], end="    \t")
            if i == '7':
                print('AbilityCost:', gold_info[i], end="    \t")
            if i == '8':
                print('CheatCommand:', gold_info[i], end="    \t")
            if i == '9':
                print('SelectionPenalty:', gold_info[i], end="    \t")
            if i == '10':
                print('GameTick:', gold_info[i], end="    \t")
            if i == '11':
                print('Building:', gold_info[i], end="    \t")
            if i == '12':
                print('Herokill:', gold_info[i], end="    \t")
            if i == '13':
                print('CreepKill:', gold_info[i], end="    \t")
            if i == '14':
                print('RoshanKill:', gold_info[i], end="    \t")
            if i == '15':
                print('CourierKill:', gold_info[i], end="    \t")
            if i == '16':
                print('SharedGold:', gold_info[i], end="    \t")
            count += 1
            if (count % 4==0 and count != l):
                print()
        print()
    return gold_info

def get_totoal_gold(player_id,match_id,prt=False):
    info_player = get_player_info_match_id(player_id,match_id)
    if prt == True:
        print("Total GOLD:",info_player['total_gold'])
    return info_player['total_gold']


def get_gold_info_player_recent_matches(player_id,prt=False):
    """
    get the gold information of ONE player for recent matches

    :param player_id:
    :return:list of xp information for recent matches
    """
    gold_info_recent_matches =[]
    matches_recent_id = get_recent_matches_id(player_id)

    for m_id in matches_recent_id:
        gold_info = get_gold_info_player_match(player_id,m_id,prt)
        if(gold_info is None):
            continue
        gold_info_recent_matches.append(gold_info)

    return gold_info_recent_matches

def get_kills_info_player_match(player_id,match_id,prt=False):
    """
    get ONE player in ONE match's kills information
    :param player_id:
    :param match_id:
    :param prt:
    :return: list of kill information
    """
    info = get_player_info_match_id(player_id,match_id)
    info_kills = {}
    if('hero_kills' not in info.keys()):
        if prt is True:
            print("None")
        return None
    info_kills.update({'hero_kills': info['hero_kills'] } )
    info_kills.update({'lane_kills':info['lane_kills']})
    info_kills.update({'neutral_kills':info['neutral_kills']})
    info_kills.update({'ancient_kills':info['ancient_kills']})
    info_kills.update({'tower_kills':info['tower_kills']})
    info_kills.update({'roshan_kills':info['roshan_kills']})
    info_kills.update({'observer_kills':info['observer_kills']})
    info_kills.update({'courier_kills':info['courier_kills']})
    info_kills.update({'observer_kills':info['observer_kills']})
    info_kills.update({'sentry_kills':info['sentry_kills']})
    info_kills.update({'necronomicon_kills':info['necronomicon_kills']})
    if(prt is True):
        print(info_kills)
    return info_kills

def get_kills_info_player_recent_matches(player_id,prt = False):
    """
    get kills information for recent matches
    :param player_id:
    :param prt:
    :return: list of kills information dictionary
    """
    info_kills =[]
    match_id_list = get_recent_matches_id(player_id)
    for m_id in match_id_list:
        info_kills.append(get_kills_info_player_match(player_id,m_id,prt))

    return  info_kills

# '''Match_id = 5025106005
# Player_id = 143593296

# -----------------------------------------------------------
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd.lower() == 'mmr':
        player_id = int(sys.argv[2])
        query_mmr(player_id)
    if cmd.lower() =="mmrall":
        query_mmr(143593296)
        query_mmr(157092389)
        query_mmr(185399450)
        query_mmr(126049611)

    # get information about experience
    if cmd.lower() == 'xp':
        player_id = int(sys.argv[2])
        prt = False
        l = len(sys.argv)
        if (l == 3):
            get_xp_info_player_recent_matches(player_id)
        if(l==4):
            if (sys.argv[3].lower() == "true"or sys.argv[3].lower() == "t"):
                prt = True
                get_xp_info_player_recent_matches(player_id,prt)
            else:
                match_id = int(sys.argv[3])
                get_xp_info_player_match(player_id,match_id,prt)
        if(l==5):
            prt = True
            match_id = int(sys.argv[3])
            get_xp_info_player_match(player_id, match_id, prt)

    # for query information about gold
    if cmd.lower() == 'gold':
        player_id = int(sys.argv[2])
        prt = False
        l = len(sys.argv)
        if (l == 3):
            get_gold_info_player_recent_matches(player_id)
        if(l==4):
            if (sys.argv[3].lower() == "true"or sys.argv[3].lower() == "t"):
                prt = True
                get_gold_info_player_recent_matches(player_id,prt)
            else:
                match_id = int(sys.argv[3])
                get_gold_info_player_match(player_id,match_id,prt)
        if(l==5):
            prt = True
            match_id = int(sys.argv[3])
            get_gold_info_player_match(player_id, match_id, prt)

    # get kills information
    if cmd.lower() == 'kills' or cmd.lower() == 'kill':
        player_id = int(sys.argv[2])
        prt = False
        l = len(sys.argv)
        if (l == 3):
            get_kills_info_player_recent_matches(player_id)
        if(l==4):
            if (sys.argv[3].lower() == "true"or sys.argv[3].lower() == "t"):
                prt = True
                get_kills_info_player_recent_matches(player_id,prt)
            else:
                match_id = int(sys.argv[3])
                get_kills_info_player_match(player_id,match_id,prt)
        if(l==5):
            prt = True
            match_id = int(sys.argv[3])
            get_kills_info_player_match(player_id, match_id, prt)

