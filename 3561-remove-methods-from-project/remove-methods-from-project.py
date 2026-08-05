from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, l: List[List[int]]) -> List[int]:
        s = {}
        p = {}
        v = {}

        for i in range(n):
            s[i] = []
            v[i] = False

        for u, z in l:
            s[u].append(z)

        q = deque()
        q.append(k)
        v[k] = True

        while q:
            i = q.popleft()

            for j in s[i]:
                if v[j] == False:
                    v[j] = True
                    p[j] = i
                    q.append(j)

        for u, z in l:
            if v[u] == False and v[z] == True:
                return list(range(n))

        fl = []
        for i in v:
            if v[i] == False:
                fl.append(i)

        fl.sort()
        return fl
            

        



        
        
            

