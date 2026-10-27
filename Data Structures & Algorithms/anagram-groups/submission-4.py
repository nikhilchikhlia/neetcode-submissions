class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        finalArray = []
        data = defaultdict(list)
        for string in strs:
            data["".join(sorted(string))].append(string)
            sortedString = "".join(sorted(string))
        return list(data.values())
