from mapping_elements import Node, read_datafile, Graph, Station, Owner, Cat
import random

NON_EXISTANT_STATION_IDS = [189]


def main():
    tubemap = Graph()
    tubemap.readnodefile('tfl_stations.csv')
    tubemap.readconnections('tfl_connections.csv')
    populate_map(tubemap, 400)
    for i in xrange(0,10001):
        move_random_owner(tubemap)


def move_random_owner(tubemap):
    stationcount = len(tubemap.nodes)
    random_node = tubemap.nodes[get_random_station_id(stationcount)]
    try:
        random_owner = random.choice(list(random_node.occupiers.owners))
        new_location = random_owner.move(random_node.connections)
        if new_location is not None:
            random_node.occupiers.remove_owner(random_owner)
            tubemap.nodes[new_location].occupiers.addowner(random_owner)
            # print '{} moved from {} to {}'.format(random_owner,random_node.id, new_location)
    except IndexError:
        pass
        # can't move if empty


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
    main()