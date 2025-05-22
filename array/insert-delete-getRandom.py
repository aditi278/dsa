import random
class RandomizedSet:

    def __init__(self):
        self.randSet = {}

    def insert(self, val: int) -> bool:
        try:
            x = self.randSet[val]
            return False
        except:
            self.randSet[val] = True
            return True

    def remove(self, val: int) -> bool:
        try:
            del self.randSet[val]
            return True
        except:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randSet.keys()))