from common.constant import DEBUG
from common.util import (
    array_to_matrix, print_matrix,
    parse_locations,
)
from .solution import Solution


class DoNothingSolution(Solution):
    NAME = "DoNothingSolution"
    DESCRIPTION = """\
    아무 것도 하지 않고, 매트릭스 로그만 찍습니다.
    """

    def __init__(self, problem):
        super().__init__(problem)

    def start(self):
        super().start()

        print("[parameters]")
        print(f"problem: {self.problem}")

    def update_locations(self, locations):
        super().update_locations(locations)

        bike_arr = parse_locations(locations)
        if DEBUG:
            print_matrix(array_to_matrix(bike_arr))

    def update_trucks(self, trucks):
        super().update_trucks(trucks)

    def make_commands(self):
        return []
