class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        finalArray = []
        data = defaultdict(list)
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in data:
                data[sortedString].append(str(string))
            else:    
                data[sortedString] = [str(string)]
        for row in data.values():
            finalArray.append(row)
        return finalArray
