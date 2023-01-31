import datetime

import keyboard

from herblore import make_pots
from osrs_utils import general_utils

'''
{
    'port': '56799',
    'password': 'pass_70',
    'post_login_steps': None
}
{
    'port': '56800',
    'password': 'pass_71',
    'post_login_steps': None
}
'''

acc_configs = [
    {
        'port': '56799',
        'password': 'pass_70',
        'post_login_steps': None
    }
]


def main():
    start_time = datetime.datetime.now()
    #general_utils.random_sleep(10, 15)
    while True:
        start_time = general_utils.multi_break_manager(start_time, 53, 58, 423, 551, acc_configs)
        make_pots(acc_configs[0]['port'])

main()