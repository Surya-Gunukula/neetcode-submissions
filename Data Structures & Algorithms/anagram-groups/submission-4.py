class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputList = []
        input_map = defaultdict(list)

        for input_str in strs:
            sorted_str = ''.join(sorted(input_str))
            input_map[sorted_str].append(input_str)

        for value in input_map.values():
            outputList.append(value)
        
        return outputList


            
            
