class Solution:
    NAME = "Empty Solution"
    DESCRIPTION = """\
    Empty Description
    """

    def __init__(self, problem):
        self.problem = problem
        self.n = None

    def update_locations(self, locations):
        self.n = int(len(locations) ** 0.5)

    def update_trucks(self, trucks):
        pass

    def make_commands(self):
        return []
