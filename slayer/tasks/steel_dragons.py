# 2134,9305,0
import datetime

import osrs
from osrs.item_ids import ItemIDs
from slayer import transport_functions
from combat import slayer_killer
from slayer.utils import bank
varrock_tele_widget_id = '218,23'


equipment = [
    {'id': ItemIDs.DRAGONFIRE_SHIELD.value, 'consume': 'Wield'},
    {'id': ItemIDs.FIRE_CAPE.value, 'consume': 'Wear'},
    {'id': ItemIDs.SLAYER_HELMET_I.value, 'consume': 'Wear'},
    {'id': ItemIDs.BARROWS_GLOVES.value, 'consume': 'Wear'},
    {'id': ItemIDs.BRIMSTONE_RING.value, 'consume': 'Wear'},
    {'id': ItemIDs.DRAGON_BOOTS.value, 'consume': 'Wear'},
    {'id': ItemIDs.BANDOS_CHESTPLATE.value, 'consume': 'Wear'},
    {'id': ItemIDs.BANDOS_TASSETS.value, 'consume': 'Wear'},
    {'id': ItemIDs.AMULET_OF_FURY.value, 'consume': 'Wear'},
    {'id': ItemIDs.DRAGON_HUNTER_LANCE.value},
    {'id': ItemIDs.HOLY_BLESSING.value, 'consume': 'Equip'},
    {'id': ItemIDs.DRAMEN_STAFF.value, 'consume': 'Wield'},
]

supplies = [
    ItemIDs.SUPER_ATTACK4.value,
    ItemIDs.SUPER_ATTACK4.value,
    ItemIDs.SUPER_STRENGTH4.value,
    ItemIDs.SUPER_STRENGTH4.value,
    ItemIDs.PRAYER_POTION4.value,
    ItemIDs.PRAYER_POTION4.value,
    ItemIDs.PRAYER_POTION4.value,
    ItemIDs.PRAYER_POTION4.value,
    ItemIDs.EXTENDED_ANTIFIRE4.value,
    ItemIDs.RUNE_POUCH.value,
    ItemIDs.KARAMJA_GLOVES_4.value,
    {
        'id': ItemIDs.MONKFISH.value,
        'quantity': '5'
    },
    {
        'id': ItemIDs.NATURE_RUNE.value,
        'quantity': 'All'
    }
]

pot_config = slayer_killer.PotConfig(super_combat=True, antifire=True)


def pre_log():
    safe_tile = {
        'x': 2677,
        'y': 9427,
        'z': 0
    }
    safe_tile_string = f'{safe_tile["x"]},{safe_tile["y"]},{safe_tile["z"]}'
    qh = osrs.queryHelper.QueryHelper()
    qh.set_tiles({safe_tile_string})
    qh.set_player_world_location()
    last_off_tile = datetime.datetime.now()
    while True:
        qh.query_backend()
        if qh.get_player_world_location('x') != safe_tile["x"] \
                or qh.get_player_world_location('y') != safe_tile["y"]:
            last_off_tile = datetime.datetime.now()

        if qh.get_player_world_location('x') == safe_tile["x"] \
                and qh.get_player_world_location('y') == safe_tile["y"]:
            if (datetime.datetime.now() - last_off_tile).total_seconds() > 11:
                return
            if (datetime.datetime.now() - last_off_tile).total_seconds() > 3:
                osrs.player.turn_off_all_prayers()
        elif qh.get_tiles(safe_tile_string):
            osrs.move.fast_click(qh.get_tiles(safe_tile_string))
        else:
            osrs.move.follow_path(qh.get_player_world_location(), safe_tile)


def main():
    qh = osrs.queryHelper.QueryHelper()
    qh.set_inventory()
    task_started = False
    while True:
        qh.query_backend()
        bank(qh, task_started, equipment, supplies)
        osrs.game.tele_home()
        osrs.game.click_restore_pool()
        osrs.game.tele_home_fairy_ring('ckr')
        transport_functions.brimhaven_dungeon_steels()
        qh.query_backend()
        osrs.move.click(qh.get_inventory(ItemIDs.DRAGON_HUNTER_LANCE.value))
        task_started = True
        success = slayer_killer.main('steel dragon', pot_config.asdict(), 35, prayers=['protect_melee'], hop=True, pre_hop=pre_log)
        qh.query_backend()
        osrs.player.turn_off_all_prayers()
        osrs.game.cast_spell(varrock_tele_widget_id)
        if success:
            return True
