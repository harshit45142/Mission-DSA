import heapq

def runningMedian(a):
    maxh = []
    minh = []
    ans = []
    for aa in a:
        if len(maxh) == 0 or aa <= -maxh[0]:
            heapq.heappush(maxh, -aa)
        else:
            heapq.heappush(minh, aa)

        if len(maxh) > len(minh) + 1:
            heapq.heappush(minh, -heapq.heappop(maxh))
        elif len(minh) > len(maxh):
            heapq.heappush(maxh, -heapq.heappop(minh))

        if len(maxh) > len(minh):
            m = -maxh[0]
        else:
            m = (-maxh[0] + minh[0]) / 2
        ans.append(format(m, ".1f"))
    return ans
