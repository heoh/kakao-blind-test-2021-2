from __future__ import annotations
from typing import List, Dict
import requests


class Session:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token
        self.auth_key = None
        self.problem = None
        self.time = None
        self.distance = 0.
        self.status = None
        self.failed_requests_count = 0

    def start(self, problem: int) -> Session:
        r = requests.post(
            url=f'{self.base_url}/start',
            headers={
                'X-Auth-Token': self.token,
                'Content-Type': 'application/json',
            },
            json={
                'problem': problem,
            },
        )
        r.raise_for_status()
        response = r.json()

        self.auth_key = response['auth_key']
        self.problem = response['problem']
        self.time = response['time']
        self.status = Status.READY
        self.failed_requests_count = 0

        return self

    def get_locations(self) -> List[Dict]:
        r = requests.get(
            url=f'{self.base_url}/locations',
            headers={
                'Authorization': self.auth_key,
                'Content-Type': 'application/json',
            },
        )
        r.raise_for_status()
        response = r.json()
        return response['locations']

    def get_trucks(self) -> List[Dict]:
        r = requests.get(
            url=f'{self.base_url}/trucks',
            headers={
                'Authorization': self.auth_key,
                'Content-Type': 'application/json',
            },
        )
        r.raise_for_status()
        response = r.json()
        return response['trucks']

    def simulate(self, commands: List[Dict]) -> int:
        r = requests.put(
            url=f'{self.base_url}/simulate',
            headers={
                'Authorization': self.auth_key,
                'Content-Type': 'application/json',
            },
            json={
                'commands': commands,
            },
        )
        r.raise_for_status()
        response = r.json()

        self.status = response['status']
        self.time = response['time']
        self.distance = float(response['distance'])
        self.failed_requests_count = int(float(response['failed_requests_count']))

        return self

    def get_score(self) -> float:
        r = requests.get(
            url=f'{self.base_url}/score',
            headers={
                'Authorization': self.auth_key,
                'Content-Type': 'application/json',
            },
        )
        response = r.json()
        return response['score']


class Command:
    NOTHING = 0
    MOVE_UP = 1
    MOVE_RIGHT = 2
    MOVE_DOWN = 3
    MOVE_LEFT = 4
    LOAD = 5
    UNLOAD = 6


class Status:
    READY = 'ready'
    FINISHED = 'finished'
    IN_PROGRESS = 'in_progress'
