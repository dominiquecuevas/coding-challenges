class PersonNode():

    def __init__(self, na,e, adjacent=None):

        if adjacent is None:
            # set of nodes next to current node
            adjacent = set()

        assert isinstance(adjacent, set)

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        return "<PersonNode: "