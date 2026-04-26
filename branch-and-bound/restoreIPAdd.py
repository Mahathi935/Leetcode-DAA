def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return
            
            if len(path) == 4:
                return
            
            for i in range(1, 4):
                if start+i > len(s):
                    break
                part = s[start:start+i]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                
                path.append(part)
                backtrack(start+i, path)
                path.pop()

        backtrack(0, [])
        return res