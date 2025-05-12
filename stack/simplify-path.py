class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = []
        for x in path.split('/'):
            if x == '..':
                if len(new_path) > 0:
                    new_path.pop()
            elif x != '' and x != '.':
                new_path.append(x)
        return '/'+'/'.join(new_path)
 