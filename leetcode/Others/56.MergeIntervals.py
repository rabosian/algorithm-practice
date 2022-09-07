def merge(intervals):
    if len(intervals) == 1:
        return intervals
    intervals.sort()
    result = [intervals[0]]
    for itv in intervals[1:]:
        cur = result.pop()
        if cur[1] >= itv[0]:
            result.append([min(cur[0],itv[0]),max(cur[1],itv[1])])
        else:
            result.append(cur)
            result.append(itv)
    return result


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))
