class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        #             north   east   south   west
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        cur_dir = 0
        x, y = 0, 0
        xd, yd = directions[0][0], directions[0][1]

        obstacles_set = set(map(tuple, obstacles))

        further_point = 0

        for i in commands:
            if i == -1:
                cur_dir = (cur_dir+1)%4
                xd = directions[cur_dir][0]
                yd = directions[cur_dir][1]
            elif i == -2:
                cur_dir = (cur_dir-1)%4
                xd = directions[cur_dir][0]
                yd = directions[cur_dir][1]
            else:
                for j in range(i):
                    new_x = x+xd
                    new_y = y+yd
                    if (new_x, new_y) not in obstacles_set:
                        x, y = new_x, new_y
                        new_length = (x*x) + (y*y)
                        further_point = max(further_point, new_length)
                    else:
                        break
            
        return further_point


        