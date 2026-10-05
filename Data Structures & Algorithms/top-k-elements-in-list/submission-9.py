class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        val = sorted(list(hashmap.values()))

        res = []
        while k > 0:
            for i in hashmap:
                if hashmap[i] == val[-1]:
                    res.append(i)
                    val.pop()
                    hashmap.pop(i)
                    break
            k = k - 1
        
        return res
