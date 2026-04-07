class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 1  # 0=N, 1=E, 2=S, 3=W (starts East)
        self.dirs = ["North", "East", "South", "West"]
        self.cycle = 2 * (width + height - 2)
        self.moved = False  # important for edge case

    def step(self, num):
        if self.cycle == 0:
            return

        num %= self.cycle
        if num == 0:
            num = self.cycle  # important trick

        self.moved = True

        while num > 0:
            if self.dir == 0:  # North
                dist = self.h - 1 - self.y
                move = min(dist, num)
                self.y += move

            elif self.dir == 1:  # East
                dist = self.w - 1 - self.x
                move = min(dist, num)
                self.x += move

            elif self.dir == 2:  # South
                dist = self.y
                move = min(dist, num)
                self.y -= move

            else:  # West
                dist = self.x
                move = min(dist, num)
                self.x -= move

            num -= move

            if num > 0:
                self.dir = (self.dir - 1) % 4

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        # 🔥 CRITICAL EDGE CASE
        if self.x == 0 and self.y == 0 and self.moved:
            return "South"
        return self.dirs[self.dir]