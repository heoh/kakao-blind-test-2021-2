from common.constant import BASE_URL, X_AUTH_TOKEN
from common.api import Session, Command, Status


def main():
    session = Session(BASE_URL, X_AUTH_TOKEN).start(problem=1)
    while session.status == Status.READY:
        locations = session.get_locations()
        trucks = session.get_trucks()
        session.simulate([
            {'truck_id': 0, 'command': [Command.NOTHING]},
        ])
        print(f"{session.time}: {session.failed_requests_count}")
    print(session.get_score())


if __name__ == '__main__':
    main()
