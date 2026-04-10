class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            m = float('inf') #smallest length

            for interval in intervals:
                if q >= interval[0] and q <= interval[1]:
                    m = min(m, interval[1] - interval[0] + 1)
            
            if m == float('inf'):
                res.append(-1)
            else:
                res.append(m)
        
        return res
            


        