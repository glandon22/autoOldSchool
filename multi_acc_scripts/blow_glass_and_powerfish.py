import datetime

import keyboard

from crafting import blow_glass, complete_inv_on_login
from fishing import catch_fish
from osrs_utils import general_utils

acc_configs = [
    {
        'port': '56799',
        'password': 'pass_70',
        'post_login_steps': complete_inv_on_login('56799')
    },
    {
        'port': '56800',
        'password': 'pass_71',
        'post_login_steps': None
    }
]


def main():
    start_time = datetime.datetime.now()
    general_utils.random_sleep(10, 15)
    while True:
        start_time = general_utils.multi_break_manager(start_time, 53, 58, 423, 551, acc_configs)
        blow_glass(general_utils.get_skill_data('crafting', acc_configs[0]['port']))
        general_utils.random_sleep(0.5, 0.6)
        keyboard.send('alt + tab')
        general_utils.random_sleep(0.5, 0.6)
        catch_fish('2', '56800')
        general_utils.random_sleep(0.5, 0.6)
        keyboard.send('alt + tab')
        general_utils.random_sleep(0.5, 0.6)


main()