import datetime

import osrs
import osrs.move
from osrs.item_ids import ItemIDs
from slayer import transport_functions
from combat import slayer_killer
from slayer.utils import bank

varrock_tele_widget_id = '218,23'
fally_tele_widget_id = '218,29'
trollheim_tele_widget_id = '218,54'


supplies = [
    ItemIDs.SUPER_ATTACK4.value,
    ItemIDs.SUPER_ATTACK4.value,
    ItemIDs.SUPER_STRENGTH4.value,
    ItemIDs.SUPER_STRENGTH4.value,
    ItemIDs.RUNE_POUCH.value,
    ItemIDs.SUPER_RESTORE4.value,
    {
        'id': ItemIDs.NATURE_RUNE.value,
        'quantity': 'All'
    },
    ItemIDs.KARAMJA_GLOVES_4.value,
    {
        'id': ItemIDs.MONKFISH.value,
        'quantity': 'X',
        'amount': '9'
    },
    {
        'id': ItemIDs.PRAYER_POTION4.value,
        'quantity': '10'
    },
]

equipment = [
    {'id': ItemIDs.DRAGON_DEFENDER.value, 'consume': 'Wield'},
    {'id': ItemIDs.ZAMORAK_CLOAK.value, 'consume': 'Wear'},
    {'id': ItemIDs.SLAYER_HELMET_I.value, 'consume': 'Wear'},
    {'id': ItemIDs.ARMADYL_BRACERS.value, 'consume': 'Wear'},
    {'id': ItemIDs.BRIMSTONE_RING.value, 'consume': 'Wear'},
    {'id': ItemIDs.DRAGON_BOOTS.value, 'consume': 'Wear'},
    {'id': ItemIDs.BANDOS_CHESTPLATE.value, 'consume': 'Wear'},
    {'id': ItemIDs.BANDOS_TASSETS.value, 'consume': 'Wear'},
    {'id': ItemIDs.AMULET_OF_FURY.value, 'consume': 'Wear'},
    {'id': ItemIDs.OSMUMTENS_FANG.value, 'consume': 'Wield'},
    {'id': ItemIDs.HOLY_BLESSING.value, 'consume': 'Equip'},
]

banking_config_equipment = {
    'dump_inv': True,
    'dump_equipment': True,
    'search': [{'query': 'slayer', 'items': equipment}]
}

banking_config_supplies = {
    'dump_inv': True,
    'dump_equipment': False,
    'search': [{'query': 'slayer', 'items': supplies}]
}

pot_config = slayer_killer.PotConfig(super_atk=True, super_str=True)


def pre_log():
    osrs.clock.random_sleep(11, 12)


def main():
    qh = osrs.queryHelper.QueryHelper()
    qh.set_inventory()
    task_started = False
    while True:
        bank(qh, task_started, equipment, supplies)
        osrs.game.tele_home()
        osrs.game.click_restore_pool()
        osrs.clock.sleep_one_tick()
        osrs.game.cast_spell(trollheim_tele_widget_id)
        transport_functions.godwars_main_room()
        task_started = True
        while True:
            qh.query_backend()
            if qh.get_inventory(ItemIDs.SUPER_RESTORE4.value):
                osrs.move.fast_click(qh.get_inventory(ItemIDs.SUPER_RESTORE4.value))
            else:
                break
        success = slayer_killer.main('spiritual mage', pot_config.asdict(), 35, prayers=['protect_mage'], ignore_interacting=True, pre_hop=pre_log)
        osrs.player.turn_off_all_prayers()
        osrs.game.cast_spell(varrock_tele_widget_id)
        if success:
            return True
