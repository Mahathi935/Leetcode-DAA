def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, total, path):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                path.append(candidates[i])
                backtrack(i+1, total + candidates[i], path)
                path.pop()
                prev = candidates[i]

        backtrack(0, 0, [])
        return res