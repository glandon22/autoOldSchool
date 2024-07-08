import cooks_assistant
import transport_functions
import util_functions
import sheep_shearer
import imp_catcher
import osrs
import witchs_potion
from prayer import gilded_v2
import romeo_and_juliet
import vampire_slayer
import dorics_quest
import goblin_diplomacy
import witchs_house
import druidic_ritual
import rune_mysteries
import natural_history_quiz
import waterfall_quest
from agility import gnome_v2
import grand_tree
import tree_gnome_village
import monks_friend

'''cooks_assistant.main()
transport_functions.bank_in_lumby()
util_functions.get_quest_items([
    {
        'id': [
            osrs.item_ids.ItemIDs.BALL_OF_WOOL.value
        ],
        'quantity': 'All'
    },
    osrs.item_ids.ItemIDs.AMULET_OF_GLORY6.value,
    {
        'id': osrs.item_ids.ItemIDs.COINS_995.value,
        'quantity': 'X',
        'amount': '100k'
    },
    osrs.item_ids.ItemIDs.RED_BEAD.value,
    osrs.item_ids.ItemIDs.YELLOW_BEAD.value,
    osrs.item_ids.ItemIDs.WHITE_BEAD.value,
    osrs.item_ids.ItemIDs.BLACK_BEAD.value,
])
transport_functions.bank_to_lumby_ground()
transport_functions.walk_to_sheep_shearer()
sheep_shearer.main()
transport_functions.leave_farmer_freds_house()
transport_functions.walk_to_wizards_tower()
imp_catcher.main()
transport_functions.glory_to_draynor()
util_functions.get_quest_items([
    {
        'id': [
            osrs.item_ids.ItemIDs.DRAGON_BONES.value
        ],
        'quantity': 'All',
        'noted': True
    },
    osrs.item_ids.ItemIDs.IRON_SCIMITAR.value,
    {
        'id': osrs.item_ids.ItemIDs.COINS_995.value,
        'quantity': 'X',
        'amount': '100k'
    },
    osrs.item_ids.ItemIDs.EYE_OF_NEWT.value,
    osrs.item_ids.ItemIDs.BURNT_MEAT.value,
    osrs.item_ids.ItemIDs.ONION.value
])
witchs_potion.main()
transport_functions.leave_hettys_house()
util_functions.hop_to(330)
gilded_v2.main()
util_functions.hop_to(337)
util_functions.get_quest_items([
    osrs.item_ids.ItemIDs.STAFF_OF_AIR.value,
    osrs.item_ids.ItemIDs.GARLIC.value,
    osrs.item_ids.ItemIDs.HAMMER.value,
    osrs.item_ids.ItemIDs.CADAVA_BERRIES.value,
    osrs.item_ids.ItemIDs.BEER.value,
    {
        'id': osrs.item_ids.ItemIDs.MIND_RUNE.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.EARTH_RUNE.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY6.value,
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY5.value,
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY4.value,
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY3.value,
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY2.value,
            osrs.item_ids.ItemIDs.AMULET_OF_GLORY1.value,
        ],
        'quantity': '1'
    },
])
util_functions.equip_air_staff_and_earth_strike()
vampire_slayer.main()
util_functions.tab_to_varrock()
romeo_and_juliet.main()
transport_functions.walk_to_ge()
util_functions.get_quest_items([])
osrs.bank.ge_handler([
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.GOBLIN_MAIL.value), 'quantity': 3},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.BLUE_DYE.value), 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.ORANGE_DYE.value), 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.CLAY.value), 'quantity': 6},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.IRON_ORE.value), 'quantity': 2},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.FALADOR_TELEPORT.value), 'quantity': 10},
    {'id': osrs.item_ids.ItemIDs(osrs.item_ids.ItemIDs.COPPER_ORE.value), 'quantity': 4},
])
util_functions.get_quest_items([
    {
        'id': osrs.item_ids.ItemIDs.GOBLIN_MAIL.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.CLAY.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.IRON_ORE.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.FALADOR_TELEPORT.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.COPPER_ORE.value,
        'quantity': 'All'
    },
    osrs.item_ids.ItemIDs.BLUE_DYE.value,
    osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
    osrs.item_ids.ItemIDs.ORANGE_DYE.value,
])
transport_functions.tab_to_fally()
dorics_quest.main()
transport_functions.leave_dorics()
transport_functions.walk_to_loc(2947, 2962, 3500, 3510, 2956, 3503)
goblin_diplomacy.main()
util_functions.tab_to_varrock()
transport_functions.walk_to_ge()
osrs.bank.ge_handler([
    {'id_override': 'prayer potion(4)', 'quantity': 3},
    {'id': osrs.item_ids.ItemIDs.CHEESE.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.RAW_CHICKEN.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.RAW_BEEF.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.RAW_RAT_MEAT.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.RAW_BEAR_MEAT.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.LEATHER_GLOVES.value, 'quantity': 1},
])
quest_items = [
    {
        'id': osrs.item_ids.ItemIDs.MIND_RUNE.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.EARTH_RUNE.value,
        'quantity': 'All'
    },
    {
        'id': osrs.item_ids.ItemIDs.PRAYER_POTION4.value,
        'quantity': 'All'
    },
    osrs.item_ids.ItemIDs.CHEESE.value,
    osrs.item_ids.ItemIDs.LEATHER_GLOVES.value,
    osrs.item_ids.ItemIDs.FALADOR_TELEPORT.value,
    osrs.item_ids.ItemIDs.FALADOR_TELEPORT.value,
    osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
    osrs.item_ids.ItemIDs.STAFF_OF_AIR.value,
    osrs.item_ids.ItemIDs.RAW_CHICKEN.value,
    osrs.item_ids.ItemIDs.RAW_BEEF.value,
    osrs.item_ids.ItemIDs.RAW_RAT_MEAT.value,
    osrs.item_ids.ItemIDs.RAW_BEAR_MEAT.value,
]
osrs.bank.banking_handler({
    'dump_inv': True,
    'dump_equipment': True,
    'search': [{'query': '', 'items': quest_items}]
})
transport_functions.tab_to_fally()
transport_functions.walk_to_loc(2940, 2948, 3449, 3454, 2948, 3451)
transport_functions.fally_to_tav_gate()
witchs_house.main()
transport_functions.walk_to_loc(2911, 2915, 3484, 3488, 2913, 3486)
druidic_ritual.main()
util_functions.tab_to_varrock()
transport_functions.walk_to_ge()
osrs.bank.ge_handler([
    {'id_override': 'necklace of passage(5)', 'quantity': 5},
    {'id': osrs.item_ids.ItemIDs.LUMBRIDGE_TELEPORT.value, 'quantity': 10},
])
quest_items = [
    {
        'id': osrs.item_ids.ItemIDs.LUMBRIDGE_TELEPORT.value,
        'quantity': 'All'
    },
    osrs.item_ids.ItemIDs.NECKLACE_OF_PASSAGE5.value,
    osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
    osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
]
osrs.bank.banking_handler({
    'dump_inv': True,
    'dump_equipment': True,
    'search': [{'query': '', 'items': quest_items}]
})
transport_functions.tab_to_lumby()
transport_functions.walk_to_loc(3208, 3214, 3209, 3211, 3210, 3210)
transport_functions.talk_to_lumby_duke()
rune_mysteries.main()
util_functions.tab_to_varrock()
transport_functions.walk_to_loc(3247, 3251, 3447, 3450, 3248, 3448)
util_functions.walk_through_door(24428, 'y', 4800, True, door_type='game', timeout=3)
natural_history_quiz.main()
util_functions.walk_through_door(24427, 'y', 4800, False, door_type='game', timeout=3)
transport_functions.walk_to_ge()
# buy items for waterfall, gnome stronghold, biohazard, tree gnome village, and monks friend quest
osrs.bank.ge_handler([
    # Waterfall quest
    {'id': osrs.item_ids.ItemIDs.WATER_RUNE.value, 'quantity': 10},
    {'id': osrs.item_ids.ItemIDs.AIR_RUNE.value, 'quantity': 10},
    {'id': osrs.item_ids.ItemIDs.ROPE.value, 'quantity': 10},
    {'id_override': 'Games necklace(8)', 'quantity': 3},
    {'id_override': 'Skills necklace(6)', 'quantity': 1},
    {'id_override': 'Ring of dueling(8)', 'quantity': 1},
    # grand tree
    {'id': osrs.item_ids.ItemIDs.FIRE_RUNE.value, 'quantity': 1000},
    {'id': osrs.item_ids.ItemIDs.KHAZARD_TELEPORT.value, 'quantity': 2},
    # plague city
    {'id': osrs.item_ids.ItemIDs.DWELLBERRIES.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.SPADE.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.CHOCOLATE_DUST.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.SNAPE_GRASS.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.BUCKET_OF_MILK.value, 'quantity': 1},
    {'id': osrs.item_ids.ItemIDs.BUCKET_OF_WATER.value, 'quantity': 4},
    # monks friend and tree gnome vilalge
    {'id': osrs.item_ids.ItemIDs.LOGS.value, 'quantity': 7},
    {'id': osrs.item_ids.ItemIDs.JUG_OF_WATER.value, 'quantity': 1},
    {'id_override': 'prayer potion(4)', 'quantity': 3},
])
quest_items = [
    osrs.item_ids.ItemIDs.GAMES_NECKLACE8.value,
    osrs.item_ids.ItemIDs.RING_OF_DUELING8.value,
    osrs.item_ids.ItemIDs.PRAYER_POTION4.value,
    osrs.item_ids.ItemIDs.VARROCK_TELEPORT.value,
    osrs.item_ids.ItemIDs.ROPE.value,
]
osrs.bank.banking_handler({
    'dump_inv': True,
    'dump_equipment': True,
    'search': [{'query': '', 'items': quest_items}]
})
transport_functions.walk_to_loc(3253, 3258, 3476, 3480, 3255, 3478)
util_functions.recharge_prayer_at_alter()
transport_functions.games_neck_to_barb()
transport_functions.walk_to_loc(2528, 2530, 3494, 3497, 2529, 3495)
waterfall_quest.main()
transport_functions.necklace_of_passage_tele_outpost()
transport_functions.walk_to_loc(2458, 2462, 3379, 3382, 2460, 3381)
util_functions.help_femi()
transport_functions.walk_to_loc(2473, 2476, 3436, 3440, 2474, 3438)
gnome_v2.main(25)
osrs.move.go_to_loc(2465, 3489)
grand_tree.main()
osrs.move.interact_with_object(17385, 'y', 5000, False, timeout=6, right_click_option='Climb-up')
osrs.move.interact_with_object(16683, 'z', 1, True, timeout=4)
osrs.move.go_to_loc(2449, 3483, 1)
quest_items = [
    osrs.item_ids.ItemIDs.STAFF_OF_AIR.value,
    osrs.item_ids.ItemIDs.JUG_OF_WATER.value,
    {
        'id': [
            osrs.item_ids.ItemIDs.MIND_RUNE.value,
        ],
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.FIRE_RUNE.value,
        ],
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.PRAYER_POTION4.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION3.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION2.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION1.value,
        ],
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.PRAYER_POTION4.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION3.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION2.value,
            osrs.item_ids.ItemIDs.PRAYER_POTION1.value,
        ],
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.LOGS.value,
        ],
        'quantity': 'All'
    },
    {
        'id': [
            osrs.item_ids.ItemIDs.RING_OF_DUELING8.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING7.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING6.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING5.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING4.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING3.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING2.value,
            osrs.item_ids.ItemIDs.RING_OF_DUELING1.value,
        ],
        'quantity': '1'
    },
]
osrs.bank.banking_handler({
    'dump_inv': True,
    'dump_equipment': True,
    'search': [{'query': '', 'items': quest_items}]
})
transport_functions.dueling_to_c_wars()
transport_functions.walk_out_of_c_wars()
osrs.move.go_to_loc(2520, 3158)
osrs.move.interact_with_object(2186, 'y', 3161, True, obj_type='wall', timeout=5, right_click_option='Squeeze-through')
osrs.move.go_to_loc(2536, 3166)
tree_gnome_village.main()
osrs.move.go_to_loc(2517, 3163)
osrs.move.interact_with_object(2186, 'y', 3160, False, obj_type='wall', timeout=5,
                               right_click_option='Squeeze-through')
util_functions.talk_to_npc('elkoy')
util_functions.dialogue_handler([])
osrs.move.go_to_loc(2606, 3220)
monks_friend.main()'''

# prob need to go back to varrock and buy shit to do plague city, possibly biohazard, sea slug, knights sword, fishing contest,
# a quest for some thiving xp, farming xp, and dnetering the abyss mini quest