class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_table = [[] for _ in range(len(nums) + 1)]
        for count, freq in counts.items():
            freq_table[freq].append(count)

        output_list = []

        for i in range(len(nums), 0, -1):
            for num in freq_table[i]:
                output_list.append(num)
                k -= 1
                if(k <= 0):
                    break
            if(k <= 0):
                break
        return output_list
            