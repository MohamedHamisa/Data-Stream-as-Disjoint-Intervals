class SummaryRanges:
    def __init__(self):
        self.stack = deque()
        
    def dfs(self, nums):
        return list(zip(sorted(set([n for n in nums if n-1 not in nums])),
                        sorted(set([n for n in nums if n+1 not in nums]))))

    def addNum(self, val):
        self.stack.append(val)

    def getIntervals(self):
        return self.dfs(self.stack)






