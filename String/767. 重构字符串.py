class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import heapq
        pq = [(-S.count(s), s) for s in set(S)]
        heapq.heapify(pq)
        for c, x in pq:
            if -c > (len(S) + 1) / 2:
                return ""
        out = []
        while (len(pq) >= 2):
            c1, v1 = heapq.heappop(pq)
            c2, v2 = heapq.heappop(pq)
            out.extend([v1, v2])
            if c1 + 1: heapq.heappush(pq, (c1 + 1, v1))
            if c2 + 1: heapq.heappush(pq, (c2 + 1, v2))

        return "".join(out) + (pq[0][1] if pq else "")