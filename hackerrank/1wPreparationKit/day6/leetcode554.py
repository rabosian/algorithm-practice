
def leastBricks(wall):

    crossDict = {}
    for row in wall:
        edge = 0
        for i in range(len(row)-1):
            edge += row[i]
            if edge in crossDict:
                crossDict[edge] += 1
            else:
                crossDict[edge] = 1
    
    return len(wall) if not crossDict else len(wall)-max(crossDict.values())
    

wall = [[10000],[10000],[10000]]
print(leastBricks(wall))
