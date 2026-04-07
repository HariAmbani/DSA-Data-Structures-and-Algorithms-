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
        cur_pos = [0,0]

        obstacles_set = set()
        for i,j in obstacles:
            obstacles_set.add((i,j))

        further_point = 0

        for i in commands:
            if i == -1:
                cur_dir = (cur_dir+1)%4
            elif i == -2:
                cur_dir = (cur_dir-1)%4
            else:
                for j in range(i):
                    new_x = cur_pos[0]+directions[cur_dir][0]
                    new_y = cur_pos[1]+directions[cur_dir][1]
                    if (new_x, new_y) not in obstacles_set:
                        cur_pos[0], cur_pos[1] = new_x, new_y
                        new_length = (cur_pos[0]*cur_pos[0]) + (cur_pos[1]*cur_pos[1])
                        if new_length > further_point:
                            further_point = new_length
                    else:
                        break
            
        return further_point


        