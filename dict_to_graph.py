import opendota2py
import sys
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


from opendota2py import Player
from opendota2py import Match
from opendota2py import Hero

sys.path.append('..')
sys.path.append('.')


display_kills_type = ['hero_kills','lane_kills','neutral_kills','ancient_kills','tower_kills']
display_gold_type = ['Unspecified','AbilityCost','Building','Herokill','CreepKill']
display_xp_type = ['Unspecified','HeroKill','CreepKill','RoshanKill']
gold_type = ['Unspecified','DeathLost','Buyback','PurchaseConsumable','PurchaseItem','AbandonedRedistribute','SellItem','AbilityCost','CheatCommand','SelectionPenalty','GameTick','Building','Herokill','CreepKill','RoshanKill','CourierKill','SharedGold']
xp_type = ['Unspecified','HeroKill','CreepKill','RoshanKill']

def dict_correct_key(data_dict,type_array):
    new_dict = {}
    for key in data_dict.keys():
        new_dict[type_array[int(key)]]= data_dict[key]
    return new_dict


def dict_to_Pie(data_dict, type_array,i):

    data_show =[]
    data_type_show = []
    originkeys = data_dict.keys()
    for key in type_array:
        if key in originkeys:
            data_show.append(data_dict[key])
            data_type_show.append(key)
        else:
            continue

    # fig, ax = plt.subplots(figsize = (6,3), subplot_kw=dict(aspect = "equal"))
    plt.subplot(3,1,i)
    plt.legend(type_array,loc='best')

    # wedgeprops define the spare circle in graph
    wedges, textss = plt.pie(data_show,explode=False, labels = type_array,wedgeprops=dict(width = 0.5),startangle= -30)

    # explaination block properties
    bbox_pros = dict(boxstyle = "square,pad = 0.2", fc = 'w',ec = "k",lw = 0.72)
    kw =dict(arrowprops = dict(arrowstyle = "-"),bbox = bbox_pros, zorder = 0.9,va ="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2-p.theta1)/2.+p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(data_type_show[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),horizontalalignment=horizontalalignment, **kw)


def get_personaname(player_id):
    player = Player(player_id)
    return player.personaname

def get_player_info_match_id(player_id, match_id):
    '''
    get a player's information with match id
    :param player_id:
    :param match_id:
    :return:
    '''
    match = Match(match_id)
    players_info = match.players

    for player_info in players_info:
        if(player_info is None):
            continue
        if player_info['account_id'] == player_id:
            return player_info
        else:
            continue
    print("No such a player in match:", match_id)
    return None

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


def show_me_sth(player_id,match_id):
    info = get_player_info_match_id(player_id,match_id)
    Name = info['personaname']
    gold_info = info['gold_reasons']
    xp_info = info['xp_reasons']
    kills_info = get_kills_info_player_match(player_id,match_id)

    gold = dict_correct_key(gold_info,gold_type)
    xp = dict_correct_key(xp_info,xp_type)
    print(gold,'\n',xp)

    plt.figure(figsize=(9,10))
    plt.suptitle(Name,fontsize = 16)
    dict_to_Pie(gold,display_gold_type,1)
    dict_to_Pie(xp,display_xp_type,2)
    dict_to_Pie(kills_info,display_kills_type,3)

    plt.show()

show_me_sth(143593296,5034645671)
show_me_sth(185399450,5034645671)
show_me_sth(157092389,5034645671)
show_me_sth(126049611,5034645671)


# show_me_sth(139988781,5027930285)
# data = {'1':123,'2':2345,'3':2342,'4':444,'5':555}
# type_show =['1','3','5']
#143593296  5034274308
# dict_to_Pie(data,type_show)