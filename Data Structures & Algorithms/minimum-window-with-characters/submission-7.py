class Solution:
    # Time Limit Exceeded. You may have an infinite loop or your code is too inefficient.
    # def minWindow(self, s: str, t: str) -> str:
    #     hashMap1 = {}
    #     for i in range(len(t)):
    #         hashMap1[t[i]] = hashMap1.get(t[i],0) + 1
    #     total = len(t)
    #     seen = 0
    #     l = 0        
    #     res = ""
    #     while l < len(s):
    #         seen = 0
    #         hashMap2 = {}
    #         for r in range(l, len(s)):
    #             hashMap2[s[r]] = hashMap2.get(s[r],0) + 1
    #             if s[r] in hashMap1 and hashMap2[s[r]] <= hashMap1[s[r]]:
    #                 seen += 1
    #             if seen == total:
    #                 break

    #         if seen == total:
    #             if res == "":
    #                 res = s[l: r+1]
    #             else:
    #                 if r - l + 1 < len(res):
    #                     res = s[l:r+1]
    #         l += 1
    #         while l < len(s) and s[l] not in hashMap1:
    #             l += 1

    #     return res

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Count characters we need
        hashMap1 = {}
        for char in t:
            hashMap1[char] = hashMap1.get(char, 0) + 1

        hashMap2 = {}
        total = len(t)   # total required characters, including duplicates
        seen = 0

        l = 0
        res = ""

        for r in range(len(s)):

            # Add s[r] into the current window
            char = s[r]
            hashMap2[char] = hashMap2.get(char, 0) + 1

            # Only count it if we still need this character
            if char in hashMap1 and hashMap2[char] <= hashMap1[char]:
                seen += 1

            # Window contains everything required
            while seen == total:

                # Update shortest result
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r + 1]

                # Remove the left character
                left_char = s[l]

                # If removing it makes us lose a required character
                if (left_char in hashMap1 and
                    hashMap2[left_char] == hashMap1[left_char]):
                    seen -= 1

                hashMap2[left_char] -= 1
                l += 1

        return res