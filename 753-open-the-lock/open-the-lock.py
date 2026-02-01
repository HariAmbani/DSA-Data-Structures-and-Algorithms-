from collections import deque

class Solution(object):
    def openLock(self, deadends, target):

        dead = set(deadends)

        if "0000" in dead:
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

        front = {"0000": 0}
        back = {target: 0}

        q1 = deque(["0000"])
        q2 = deque([target])

        while q1 and q2:

            # always expand smaller queue
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                front, back = back, front

            for _ in range(len(q1)):
                lock = q1.popleft()
                step = front[lock]

                for nxt in children(lock):

                    if nxt in dead:
                        continue

                    if nxt in front:
                        continue

                    # 🔥 meeting point
                    if nxt in back:
                        return step + 1 + back[nxt]

                    front[nxt] = step + 1
                    q1.append(nxt)

        return -1
