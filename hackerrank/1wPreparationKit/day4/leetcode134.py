# Gas station
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start, totalGas, currentGas = 0, 0, 0
    for i in range(len(gas)):
        totalGas += gas[i] - cost[i]
        currentGas += gas[i] - cost[i]
        if currentGas < 0:
            currentGas = 0
            start = i + 1
    return start if totalGas >= 0 else -1


gas = [2,3,4]
cost = [3,4,1]
print(canCompleteCircuit(gas, cost))