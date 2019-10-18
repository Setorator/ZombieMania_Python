from os import path
from glob import glob

# TODO: merge this to Map class?
def extract_all_maps():
    my_path = path.dirname(path.abspath(__file__))
    map_paths = glob(path.join(my_path, "..\\..\\res\\maps\\*"))

    maps = []
    for map_path in map_paths:
        maps.append(extract_map(map_path))

    return maps


def extract_map(map_path):
    with open(map_path, "r") as file:
        lines = file.readlines()
        res = []
        for line in lines:
            res.append(list(line.strip()))

    return res


def main():
    print("Starting Map Builder")
    maps = extract_all_maps()

    print(maps[0][0])
    for map in maps:
        print("MapSize: {},{}".format(len(map), len(map[0])))


if __name__ == '__main__':
    main()
