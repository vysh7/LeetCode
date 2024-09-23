class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        i = 0
        for interval in intervals:
            if len(result)==0:
                result.append(interval)
            else:
                if result[i][1]> interval[1]:
                    continue
                elif result[i][1] >= interval[0]:
                    result[i][1] = interval[1]
                else:
                    result.append(interval)
                    i+=1
        return result       