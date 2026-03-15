class Fancy(object):

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def append(self, val):
        val = (val - self.add) % self.MOD
        val = (val * pow(self.mul, self.MOD-2, self.MOD)) % self.MOD
        self.seq.append(val)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD