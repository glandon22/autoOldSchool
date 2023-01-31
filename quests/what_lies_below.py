# start the script after initiating chat with rat burgiss
import datetime

import keyboard
import pyautogui

from osrs_utils import general_utils

def first_dialogue():
    while True:
        q = {
            'chatOptions': True
        }
        data = general_utils.query_game_data(q)
        if 'chatOptions' in data and len(data['chatOptions']) >= 5:
            general_utils.random_sleep(1.6, 1.7)
            keyboard.send('3')
            general_utils.random_sleep(1, 1.1)
            break
        else:
            keyboard.send('space')
            general_utils.random_sleep(0.5, 0.6)
    while True:
        q = {
            'chatOptions': True
        }
        data = general_utils.query_game_data(q)
        if 'chatOptions' in data and len(data['chatOptions']) >= 3:
            general_utils.random_sleep(1.6, 1.7)
            keyboard.send('1')
            general_utils.random_sleep(1, 1.1)
            break
        else:
            keyboard.send('space')
            general_utils.random_sleep(0.5, 0.6)
    general_utils.random_sleep(2, 2.1)
    while True:
        q = {
            'widget': '231,6'
        }
        data = general_utils.query_game_data(q)
        if 'widget' in data and 'x' in data['widget']:
            keyboard.send('space')
            general_utils.random_sleep(0.5, 0.6)
        else:
            general_utils.random_sleep(1, 1.1)
            break
    while True:
        q = {
            'widget': '231,6'
        }
        npc = general_utils.query_game_data(q)
        q = {
            'widget': '217,6'
        }
        player = general_utils.query_game_data(q)
        if 'widget' in npc and 'x' in npc['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        elif 'widget' in player and 'x' in player['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        else:
            general_utils.random_sleep(1, 1.1)
            break


def go_to_bandits():
    inv = general_utils.get_inv()
    skills = general_utils.is_item_in_inventory(inv, 11105)
    general_utils.move_and_click(skills[0], skills[1], 7, 7, 'right')
    general_utils.random_sleep(0.5, 0.6)
    # right click menus always open in the same place relative to where they are opened from,
    # so to access desired entry i just go down from my current y position
    current_y_mouse_val = pyautogui.position()[1]
    general_utils.move_and_click(skills[0], current_y_mouse_val + 50, 15, 0)
    general_utils.random_sleep(1, 1.1)
    keyboard.send('4')
    general_utils.random_sleep(4, 4.1)
    general_utils.run_to_loc([
        '3136,3446,0',
        '3136,3453,0',
        '3136,3462,0',
        '3127,3470,0'
    ])
    general_utils.random_sleep(1,1.1)

#(datetime.datetime.now() - not_mining_timestamp).total_seconds() > 3
def kill_bandits():
    # rats paper 11008
    paper_collected = 0
    while True:
        # loop through and attack a monster
        started_fighting_timestamp = -1
        while True:
            npc_curr_target_id = 0
            monster_to_kill = 'Outlaw'
            q = {
                'interactingWith': True,
                'npcsToKill': [monster_to_kill],
                'skills': ['hitpoints'],
                'inv': True
            }
            data = general_utils.query_game_data(q)
            if 'interactingWith' in data and data['interactingWith'] == monster_to_kill:
                print('In combat, no action needed.')
                general_utils.random_sleep(0.5, 0.6)
                started_fighting_timestamp = datetime.datetime.now()
                break
            else:
                # sleep for a sec to find a new monster
                q = {
                    'npcsToKill': [monster_to_kill],
                }
                data = general_utils.query_game_data(q)
                closest = general_utils.find_closest_npc(data['npcs'], npc_curr_target_id)
                general_utils.move_and_click(closest['x'], closest['y'], 2, 2)
                npc_curr_target_id = closest['id']
                general_utils.random_sleep(3, 4)
        # find rats page on ground
        while True:
            items = general_utils.get_surrounding_ground_items(7, [11008])
            if '11008' in items:
                general_utils.move_and_click(items['11008'][0]['x'], items['11008'][0]['y'], 3, 3, 'right')
                q = {
                    'getMenuEntries': True
                }
                curr_pos = pyautogui.position()
                data = general_utils.query_game_data(q)
                if 'menuEntries' in data:
                    for i in range(len(data['menuEntries']['items'])):
                        if "paper" in data['menuEntries']['items'][i] and "Take" in data['menuEntries']['items'][i]:
                            additional_pixels = (len(data['menuEntries']['items']) - 1 - i) * 15 + 25
                            general_utils.move_and_click(curr_pos[0], curr_pos[1] + additional_pixels, 7, 1)
                            general_utils.random_sleep(2, 2.1)
                            break
                    break
        q = {
            'inv': True
        }
        data = general_utils.query_game_data(q)
        if 'inv' in data:
            paper_collected = 0
            for item in data['inv']:
                if item['id'] == 11008:
                    paper_collected += 1
            if paper_collected >= 5:
                return


def put_intel_in_folder():
    q = {
        'inv': True
    }
    data = general_utils.query_game_data(q)
    while True:
        if 'inv' in data:
            folder = general_utils.is_item_in_inventory(data['inv'], 11003)
            for item in data['inv']:
                if item['id'] == 11008:
                    general_utils.right_click_menu_select(item, 2)
                    general_utils.random_sleep(0.6, 0.7)
                    general_utils.move_and_click(folder[0], folder[1], 4, 4)
        return


def return_to_rat():
    q = {
        'inv': True
    }
    data = general_utils.query_game_data(q)
    while True:
        if 'inv' in data:
            cb_brace = general_utils.is_item_in_inventory_v2(data['inv'], 11118)
            general_utils.right_click_menu_select(cb_brace, 3)
            general_utils.random_sleep(1, 1.1)
            keyboard.send('2')
            general_utils.random_sleep(5, 5.1)
            general_utils.run_to_loc([
                '3201,3361,0',
                '3213,3359,0',
                '3220,3358,0',
                '3226,3350,0',
                '3227,3339,0',
                '3237,3336,0',
                '3245,3336,0',
                '3252,3332,0',
            ])
            general_utils.random_sleep(0.5, 0.6)
            general_utils.wait_until_stationary()
            general_utils.random_sleep(1, 1.1)
            break


def talk_to_rat():
    while True:
        q = {
            'npcsID': ['4158']
        }
        data = general_utils.query_game_data(q)
        if 'npcs' in data:
            for npc in data['npcs']:
                if npc['id'] == 4158:
                    general_utils.move_and_click(npc['x'], npc['y'], 3, 3)
                    general_utils.random_sleep(0.5, 0.6)
                    general_utils.wait_until_stationary()
                    general_utils.random_sleep(2, 2.1)
                    q = {
                        'widget': '217,6'
                    }
                    player = general_utils.query_game_data(q)
                    if 'widget' in player and 'x' in player['widget']:
                        return


def dialogue_rat():
    while True:
        q = {
            'widget': '231,6'
        }
        npc = general_utils.query_game_data(q)
        q = {
            'widget': '217,6'
        }
        player = general_utils.query_game_data(q)
        if 'widget' in npc and 'x' in npc['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        elif 'widget' in player and 'x' in player['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        else:
            general_utils.random_sleep(1, 1.1)
            break


def go_to_surok():
    q = {
        'inv': True
    }
    data = general_utils.query_game_data(q)
    while True:
        if 'inv' in data:
            tab = general_utils.is_item_in_inventory_v2(data['inv'], 8007)
            general_utils.move_and_click(tab['x'], tab['y'], 4, 4)
            general_utils.random_sleep(5, 5.1)
            general_utils.run_to_loc([
                '3212,3429,0',
                '3212,3437,0',
                '3212,3445,0',
                '3212,3452,0',
                '3212,3459,0',
                '3212,3467,0',
                '3208,3476,0',
                '3206,3482,0',
                '3210,3493,0'
            ])
            while True:
                q = {
                    'npcsID': ['4159']
                }
                data = general_utils.query_game_data(q)
                if 'npcs' in data:
                    for npc in data['npcs']:
                        if npc['id'] == 4159:
                            general_utils.move_and_click(npc['x'], npc['y'], 3, 3)
                            general_utils.random_sleep(0.5, 0.6)
                            general_utils.wait_until_stationary()
                            general_utils.random_sleep(2, 2.1)
                            q = {
                                'widget': '231,6'
                            }
                            player = general_utils.query_game_data(q)
                            if 'widget' in player and 'x' in player['widget']:
                                return


def handle_surok_answer():
    while True:
        q = {
            'widget': '231,6'
        }
        npc = general_utils.query_game_data(q)
        q = {
            'widget': '217,6',
            'chatOptions': True
        }
        player = general_utils.query_game_data(q)
        if 'widget' in npc and 'x' in npc['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        elif 'widget' in player and 'x' in player['widget']:
            keyboard.send('space')
            general_utils.random_sleep(1.5, 1.6)
        elif 'chatOptions' in player:
            for option in player['chatOptions']:
                if "Go on" in option:
                    keyboard.send('1')
                    general_utils.random_sleep(1, 1.1)
        else:
            general_utils.random_sleep(1, 1.1)
            break


def read_diary():
    q = {
        'inv': True
    }
    data = general_utils.query_game_data(q)
    diary = general_utils.is_item_in_inventory_v2(data['inv'], 11002)
    general_utils.move_and_click(diary['x'], diary['y'], 3, 3)
    general_utils.random_sleep(2, 2.1)
    for i in range(6):
        arrow = general_utils.get_widget('392,77')
        if arrow:
            general_utils.move_and_click(arrow['x'], arrow['y'], 3, 4)
            general_utils.random_sleep(1, 1.1)
        else:
            break
    keyboard.send('esc')


def main():
    first_dialogue()
    go_to_bandits()
    kill_bandits()
    put_intel_in_folder()
    return_to_rat()
    talk_to_rat()
    dialogue_rat()
    # if the door to the library is closed this will break, need to monitor and open door if needed
    go_to_surok()
    dialogue_rat()
    general_utils.random_sleep(4, 4.1)
    handle_surok_answer()
    read_diary()

