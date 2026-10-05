class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in hashMap.items():
            freq[cnt].append(num)
        
        res = []
        # use range(len(freq)-1, 0, -1) instead of range(len(freq)-1, -1, -1) because freq[0] means there's no such number. the frequency is 0 
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res