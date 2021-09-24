from common.api import Command
from common.util import (
    location_to_point, point_to_location,
    array_to_matrix, print_matrix,
    parse_locations,
)


class Truck:
    def __init__(self, truck_id):
        self.id = truck_id
        self.location = 0
        self.size = 0
        self.capacity = 20
        self.max_turn = 10

    def update(self, data):
        self.location = data['location_id']
        self.size = data['loaded_bikes_count']

    def can_move_up(self, n):
        x, y = location_to_point(n, self.location)
        return y + 1 < n

    def can_move_right(self, n):
        x, y = location_to_point(n, self.location)
        return x + 1 < n

    def can_move_down(self, n):
        x, y = location_to_point(n, self.location)
        return y - 1 >= 0

    def can_move_left(self, n):
        x, y = location_to_point(n, self.location)
        return x - 1 >= 0

    def do_nothing(self):
        return Command.NOTHING

    def move_up(self, n):
        if not self.can_move_up(n):
            return self.do_nothing()

        x, y = location_to_point(n, self.location)
        y += 1
        self.location = point_to_location(n, (x, y))

        return Command.MOVE_UP

    def move_right(self, n):
        if not self.can_move_right(n):
            return self.do_nothing()

        x, y = location_to_point(n, self.location)
        x += 1
        self.location = point_to_location(n, (x, y))

        return Command.MOVE_RIGHT

    def move_down(self, n):
        if not self.can_move_down(n):
            return self.do_nothing()

        x, y = location_to_point(n, self.location)
        y -= 1
        self.location = point_to_location(n, (x, y))

        return Command.MOVE_DOWN

    def move_left(self, n):
        if not self.can_move_left(n):
            return self.do_nothing()

        x, y = location_to_point(n, self.location)
        x -= 1
        self.location = point_to_location(n, (x, y))

        return Command.MOVE_LEFT

    def unload(self):
        self.size -= 1
        return Command.UNLOAD

    def load(self):
        self.size += 1
        return Command.LOAD

    def is_full(self):
        return self.size >= self.capacity

    def is_empty(self):
        return self.size <= 0
