from mapping_elements import Node, read_datafile, Graph, Station, Owner, Cat, NoDestinationException
import random
import itertools
import argparse


NON_EXISTANT_STATION_IDS = [189]
MAX_MOVES_FOR_PLAYER = 4

def main(N):
    tubemap = Graph()
    populate_count = N
    tubemap.readnodefile('tfl_stations.csv')
    tubemap.readconnections('tfl_connections.csv')
    populate_map(tubemap, populate_count)
    while any_cats_missing(tubemap):
        move_random_player(tubemap,'owner',populate_count)
        move_random_player(tubemap,'cat',populate_count)
    print 'done'
#     results
    found_sum = get_sum_cats_found(tubemap)
    avg_cat_moves = get_average_number_cat_moves(tubemap)

    print """
    Total number of cats: {}
    Number of cats found: {}
    Average number of movements required to find a cat: {}
""".format(populate_count, found_sum, avg_cat_moves)

def any_cats_missing(tubemap):
    return any(
        [tubemap.nodes[node_id].occupiers.cats for node_id in tubemap.nodes]
    )

def get_average_number_cat_moves(tubemap):
    foundcats = [tubemap.nodes[node_id].occupiers.foundcats for node_id in tubemap.nodes]
    foundcats_moves = [i.moves for i in itertools.chain.from_iterable(foundcats)]
    avg_cat_moves = float(sum(foundcats_moves) / len(foundcats_moves)) if len(foundcats_moves) > 0 else 0
    return avg_cat_moves


def get_sum_cats_found(tubemap):
    found_sum = sum([1 for k in tubemap.nodes if tubemap.nodes[k].occupiers.open == False])
    return found_sum


def move_random_player(tubemap, player_type,populate_count):
    """
    :param tubemap: a Graph object
    :param player_type: string: 'owner'|'cat'
    :return: None
    """
    stationcount = len(tubemap.nodes)
    random_node = tubemap.nodes[get_random_station_id(stationcount)]
    try:
        random_player = random.choice(list(getattr(random_node.occupiers, '%ss' % player_type)))
        new_location = random_player.move(random_node.connections)
        remove_fn = getattr(random_node.occupiers, 'remove_%s' % player_type)
        remove_fn(random_player)
        add_fn = getattr(tubemap.nodes[new_location].occupiers, 'add%s' % player_type)
        random_player.moves += 1
        if random_player.moves < MAX_MOVES_FOR_PLAYER:
            add_fn(random_player)
        else:
            print 'this {} has moved {} times and is exhausted!'.format(player_type, MAX_MOVES_FOR_PLAYER)
    except (NoDestinationException, AttributeError, IndexError):
        pass


def populate_map(tubemap, player_count):
    stationcount = len(tubemap.nodes)
    for i in range(1, player_count):
        cat_origin, owner_origin = generate_origins(stationcount)
        tubemap.nodes[cat_origin].occupiers.addcat(Cat(id=i))
        tubemap.nodes[owner_origin].occupiers.addowner(Owner(id=i))


def generate_origins(stationcount):
    while True:
        owner_origin = get_random_station_id(stationcount)
        cat_origin = get_random_station_id(stationcount)
        if  cat_origin != owner_origin:
            return cat_origin, owner_origin


def get_random_station_id(stationcount):
    while True:
        randstation = random.randint(1, stationcount-1)
        if randstation not in NON_EXISTANT_STATION_IDS:
            return randstation


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='How many cats/owners?')
    parser.add_argument('N',
                        type=int,
                       help='an integer')

    args = parser.parse_args()
    N = args.N
    main(N)