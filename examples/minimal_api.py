class Orientation:
    def flip(self, s):
        return -s

class Chain:
    def __init__(self, states):
        self.states = states

    def valid(self):
        return all(self.states)

class Resonance:
    def align(self, t1, t2):
        return t1 == t2

def pipeline(signal):
    orientation = Orientation()
    chain = Chain([signal])
    resonance = Resonance()

    s1 = orientation.flip(signal)
    s2 = orientation.flip(s1)

    if not chain.valid():
        return None

    if not resonance.align(s1, s2):
        return None

    return "E"  # Emergence
