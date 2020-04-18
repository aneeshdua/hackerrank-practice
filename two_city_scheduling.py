class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res=0
        N = len(costs)
        diff = [c[0] - c[1] for c in costs]
        indices =  sorted(range(0,N), key=lambda k:diff[k])
        for i in range(int(N/2)):
            res += costs[indices[i]][0]
            res += costs[indices[N-i-1]][1]
        return res    
