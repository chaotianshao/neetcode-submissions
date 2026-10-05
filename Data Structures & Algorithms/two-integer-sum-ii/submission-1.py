class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(numbers)):
            if target - numbers[i] in hashmap:
                if i < hashmap[target - numbers[i]]:
                    return [i+1, hashmap[target - numbers[i]] + 1]
                else:
                    return [hashmap[target - numbers[i]] + 1, i+1]
            else:
                hashmap[numbers[i]] = i

