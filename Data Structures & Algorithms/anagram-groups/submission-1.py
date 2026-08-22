class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = [list(i) for i in strs]
        copy = list(map(lambda a: sorted(a) ,copy))
        copy = list(map(lambda a: ''.join(a) ,copy))
        d= {}
        for i in range(len(copy)):
            if copy[i] in d:
                d[copy[i]].append(strs[i])
            else:
                d[copy[i]] = [strs[i]]
        return list([i for i in d.values()])