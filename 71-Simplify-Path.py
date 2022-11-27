class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        newPaths = list()
        for p in paths:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if len(newPaths) > 0:
                    newPaths.pop()
            else:
                newPaths.append(p)
        return "/" + "/".join(newPaths)
