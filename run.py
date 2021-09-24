import textwrap
from common.constant import BASE_URL, X_AUTH_TOKEN, LOG_DIR
from common.api import Session, Status
from common.log import set_log_filename_auto, override_print_globally
from solution.random_solution import RandomSolution


def main():
    set_log_filename_auto(LOG_DIR)
    override_print_globally()

    solution = RandomSolution(problem=1)
    session = Session(BASE_URL, X_AUTH_TOKEN).start(problem=solution.problem)

    print(solution.NAME)
    print()
    print(textwrap.dedent(solution.DESCRIPTION))

    print("== Start ==")
    solution.start()
    print()

    while session.status == Status.READY:
        print(f"== Time: {session.time} ==")
        print(f"failed_requests_count: {session.failed_requests_count}")
        print(f"distance: {session.distance}")

        solution.update_locations(session.get_locations())
        solution.update_trucks(session.get_trucks())
        session.simulate(solution.make_commands())

        print()

    print("== End ==")
    print(f"failed_requests_count: {session.failed_requests_count}")
    print(f"distance: {session.distance}")
    print(f"SCORE: {session.get_score()}")
    print("========")
    print()


if __name__ == '__main__':
    main()
