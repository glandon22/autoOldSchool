import osrs
from osrs.item_ids import ItemIDs
from slayer import transport_functions
from combat import slayer_killer
from slayer.tasks import gear

varrock_tele_widget_id = '218,23'
supplies = [
        {
            'id': ItemIDs.COINS_995.value,
            'quantity': 'X',
            'amount': '200'
        },
        ItemIDs.SUPER_COMBAT_POTION4.value,
        ItemIDs.SUPER_COMBAT_POTION4.value,
        ItemIDs.SUPER_COMBAT_POTION4.value,
        ItemIDs.RUNE_POUCH.value,
        {
            'id': [
                ItemIDs.SLAYER_RING_1.value,
                ItemIDs.SLAYER_RING_2.value,
                ItemIDs.SLAYER_RING_3.value,
                ItemIDs.SLAYER_RING_4.value,
                ItemIDs.SLAYER_RING_5.value,
                ItemIDs.SLAYER_RING_6.value,
                ItemIDs.SLAYER_RING_7.value,
                ItemIDs.SLAYER_RING_8.value,
            ],
            'quantity': '1'
        },
        ItemIDs.DRAMEN_STAFF.value,
        {
            'id': ItemIDs.MONKFISH.value,
            'quantity': 'All'
        },
    ]
equipment = [
        ItemIDs.ABYSSAL_WHIP.value,
        ItemIDs.RUNE_DEFENDER.value,
        ItemIDs.COMBAT_BRACELET.value,
        ItemIDs.OBSIDIAN_CAPE.value,
        ItemIDs.SLAYER_HELMET.value,
        ItemIDs.BRIMSTONE_RING.value,
        ItemIDs.DRAGON_BOOTS.value,
        ItemIDs.BANDOS_CHESTPLATE.value,
        ItemIDs.BANDOS_TASSETS.value,
        ItemIDs.AMULET_OF_FURY.value,
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

pot_config = slayer_killer.PotConfig(super_combat=True)


def main():
    qh = osrs.queryHelper.QueryHelper()
    qh.set_inventory()
    task_started = False
    while True:
        qh.query_backend()
        print('starting function')
        if not task_started:
            success = osrs.bank.banking_handler(banking_config_equipment)
            if not success:
                print('failed to withdraw equipment.')
                return False
            osrs.clock.sleep_one_tick()
            qh.query_backend()
            for item in qh.get_inventory():
                osrs.move.click(item)
            qh.query_backend()
        success = osrs.bank.banking_handler(banking_config_supplies)
        if not success:
            print('failed to withdraw supplies.')
            return False
        while True:
            qh.query_backend()
            if qh.get_inventory(ItemIDs.DRAMEN_STAFF.value):
                osrs.move.click(qh.get_inventory(ItemIDs.DRAMEN_STAFF.value))
                break
        osrs.game.tele_home()
        osrs.clock.random_sleep(2, 2.1)
        osrs.game.tele_home_fairy_ring('biq')
        transport_functions.smoke_dungeon()
        qh.query_backend()
        while True:
            qh.query_backend()
            if qh.get_inventory(ItemIDs.ABYSSAL_WHIP.value):
                osrs.move.click(qh.get_inventory(ItemIDs.ABYSSAL_WHIP.value))
                break
        task_started = True
        finished = slayer_killer.main('dust devil', pot_config.asdict(), 35)
        osrs.game.cast_spell(varrock_tele_widget_id)
        if finished:
            return

'''
run from fairy ring biq to 3309,3105,0
find npc id 17 and click need 200 gp for this carpet ride smh
click optino 3 to polli
in polli when coords 334 x 3366 :  2994 y 3012
click esc key
run to 3310,2959,0
find obj 6279 on tile 3310,2962,0
i dungeon when y greater than 9k
end func
'''