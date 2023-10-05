from collections import Counter, defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mi = len(nums)//3
        out = []

        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1

            if cnt[n] > mi:
                out.append(n)

        return list(set(out))
