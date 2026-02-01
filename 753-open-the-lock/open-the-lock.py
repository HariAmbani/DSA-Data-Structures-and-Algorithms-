from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)

        if "0000" in dead or target in dead:
            return -1
        if target == "0000":
            return 0

        def children(lock):
            res = []
            for i in range(4):
                digit = int(lock[i])

                res.append(lock[:i] + str((digit + 1) % 10) + lock[i+1:])
                res.append(lock[:i] + str((digit - 1) % 10) + lock[i+1:])

            return res

        front = {"0000" : 0}
        back = {target : 0}

        q1 = deque(["0000"])
        q2 = deque([target])

        while q1 and q2:
            # in multidimensional bfs always go with minium length queue
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                front, back = back, front
            
            for i in range(len(q1)):
                lock = q1.popleft()
                step = front[lock]

                for child in children(lock):
                    if child in dead:
                        continue
                    
                    if child in front:
                        continue
                    
                    if child in back:
                        return step+1+back[child]
                    
                    front[child] = step + 1
                    q1.append(child)

        return -1
