def canCompleteCircuit(self, gas, cost):
        total = cur = start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if total >= 0 else -1