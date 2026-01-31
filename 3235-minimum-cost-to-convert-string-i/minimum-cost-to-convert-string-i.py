class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):

        INF = 10**18

        dis = [[INF]*26 for _ in range(26)]

        for i in range(26):
            dis[i][i] = 0

        for i in range(len(original)):
            u = ord(original[i]) - 97
            v = ord(changed[i]) - 97
            if cost[i] < dis[u][v]:
                dis[u][v] = cost[i]

        for k in range(26):
            dk = dis[k]
            for i in range(26):
                dik = dis[i][k]
                if dik == INF:
                    continue
                row_i = dis[i]
                for j in range(26):
                    val = dik + dk[j]
                    if val < row_i[j]:
                        row_i[j] = val

        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            c = dis[ord(s)-97][ord(t)-97]
            if c == INF:
                return -1
            ans += c

        return ans
