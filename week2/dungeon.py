from hero import Hero
from orc import Orc
from fight import Fight


class Dungeon:

    def __init__(self, map_path):
        map_file = open(map_path, 'r')
        self.map = map_file.read().splitlines()
        map_file.close()
        # self.map becomes [[],[],...]
        self.map = [list(x) for x in self.map]
        self.players = {}

    def print_map(self):
        printing_map = '\n'.join([''.join(x) for x in self.map])
        print(printing_map)
        return printing_map

    def spawn(self, player_name, entity):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'S':
                    if type(entity) is Hero:
                        self.map[i][j] = 'H'
                        self.players[player_name] = [entity, (i, j)]
                        return True
                    elif type(entity) is Orc:
                        self.map[i][j] = 'O'
                        self.players[player_name] = [entity, (i, j)]
                        return True
                    else:
                        break
        return False

        def move(self, player_name, direction):
            if player_name in self.players:
                position = self.players[player_name][1]  # (i. j)
                new_position = ()  # ((i,j), (i, j),...)

                if direction == 'up' and position[0] - 1 >= 0:
                    new_position = (position[0] - 1, position[1])
                elif direction == 'down' and position[0] + 1 < len(self.map):
                    new_position = (position[0] + 1, position[1])
                elif direction == 'left' and position[1] - 1 >= 0:
                    new_position = (position[0], position[1] - 1)
                elif direction == 'right' and position[1] + 1 < len(self.map[position[0]]):
                    new_position = (position[0], position[1] + 1)
                else:
                    return False

                oponent = 'O' if type(self.players[player_name][0]) is Hero else 'H'

            if self.map[new_position[0]][new_position[1]] == '.':
                self.map[new_position[0]][new_position[1]] = self.map[
                    position[0]][position[1]]
                self.map[position[0]][position[1]] = '.'
                self.players[player_name][1] = new_position
                return True

            elif self.map[new_position[0]][new_position[1]] == oponent:
                for oponent_name in self.players:

                    if self.players[oponent_name][1] == new_position:
                        fight = Fight(self.players[player_name][0], self.players[oponent_name][0])

                        if not fight is None:
                            fight_outcome = fight.simulate_fight()
                            print(fight_outcome[0])

                            if fight_outcome[1] == 'H':
                                self.players.pop(oponent_name)
                                self.players[player_name][1] = new_position
                                self.map[new_position[0]][new_position[1]] = self.map[position[0]][position[1]]
                                self.map[position[0]][position[1]] = '.'

                            elif fight_outcome[1] == 'O':
                                self.players.pop(player_name)
                                self.map[position[0]][position[1]] = '.'

                            return fight_outcome[1]
            else:
                return False


# map = Dungeon("map.txt")
# map.spawn("player_1", Hero("Bron", 100, "DragonSlayer"))
# map.print_map()
# map.spawn("player_1", Orc("Orcy", 150, 1.5))
# map.print_map()

# print(map.players)
