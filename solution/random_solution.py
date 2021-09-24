import inspect
import random
from common.constant import DEBUG
from common.util import (
    location_to_point, point_to_location,
    array_to_matrix, print_matrix,
    parse_locations,
)
from truck.truck import Truck
from .solution import Solution


rand = random.Random(1234)


class RandomSolution(Solution):
    NAME = "RandomSolution"
    DESCRIPTION = """\
    트럭은 무작위 방향으로 움직이며,
    현재 위치의 자전거 수가 일정 수 이하면 보충하고,
    현재 위치의 자전거 수가 일정 수 이상이면 수거함
    """

    def __init__(self, problem):
        super().__init__(problem)

        self.bike_arr = None
        self.trucks = None
        if problem == 1:
            self.min_bikes = 2
            self.max_bikes = 2
        elif problem == 2:
            self.min_bikes = 2
            self.max_bikes = 2

    def start(self):
        super().start()

        print("[parameters]")
        print(f"problem: {self.problem}")
        print(inspect.getsource(self.__init__))

    def update_locations(self, locations):
        super().update_locations(locations)

        self.bike_arr = parse_locations(locations)
        if DEBUG:
            print_matrix(array_to_matrix(self.bike_arr))

    def update_trucks(self, trucks):
        super().update_trucks(trucks)

        if not self.trucks:
            self.init_trucks(trucks)

        for data in trucks:
            truck = self.trucks[data['id']]
            truck.update(data)

    def init_trucks(self, trucks):
        self.trucks = []
        for i in range(len(trucks)):
            self.trucks.append(RandomTruck(i, self.min_bikes, self.max_bikes))

    def make_commands(self):
        commands = [{'truck_id': i, 'command': []}
                    for i in range(len(self.trucks))]
        for turn in range(10):
            for truck in self.trucks:
                command = truck.do_action(turn, self.n, self.bike_arr)
                commands[truck.id]['command'].append(command)
        return commands


class RandomTruck(Truck):
    def __init__(self, truck_id, min_bikes, max_bikes):
        super().__init__(truck_id)

        self.min_bikes = min_bikes
        self.max_bikes = max_bikes

    def do_action(self, turn, n, bike_arr):
        if bike_arr[self.location] < self.min_bikes and not self.is_empty():
            bike_arr[self.location] += 1
            print(f"Truck({self.id}): unload {self.location}")
            return self.unload()
        if bike_arr[self.location] > self.max_bikes and not self.is_full():
            bike_arr[self.location] -= 1
            print(f"Truck({self.id}): load {self.location}")
            return self.load()

        r = rand.randint(0, 3)
        if r == 0:
            return self.move_up(n)
        if r == 1:
            return self.move_right(n)
        if r == 2:
            return self.move_down(n)
        if r == 3:
            return self.move_left(n)
