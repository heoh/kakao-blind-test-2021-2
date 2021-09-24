from common.constant import BASE_URL, X_AUTH_TOKEN, LOG_DIR
from common.api import Session, Command, Status
from common.util import (
    location_to_point, point_to_location,
    array_to_matrix, print_matrix,
    parse_locations,
)
from common.log import set_log_filename_auto, override_print_globally

DEBUG = True


class Solution:
    def __init__(self):
        self.n = None

    def update_locations(self, locations):
        self.n = int(len(locations) ** 0.5)
        bike_arr = parse_locations(locations)
        if DEBUG:
            print_matrix(array_to_matrix(bike_arr))

    def update_trucks(self, trucks):
        pass

    def make_commands(self):
        return []


def main():
    set_log_filename_auto(LOG_DIR)
    override_print_globally()

    solution = Solution()
    session = Session(BASE_URL, X_AUTH_TOKEN).start(problem=1)

    while session.status == Status.READY:
        solution.update_locations(session.get_locations())
        solution.update_trucks(session.get_trucks())
        session.simulate(solution.make_commands())
        print(f"{session.time}: {session.failed_requests_count}")
    print(f"SCORE: {session.get_score()}")


if __name__ == '__main__':
    main()
