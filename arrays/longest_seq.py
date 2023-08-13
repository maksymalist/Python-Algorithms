def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0
        
        max_el = 1
        curr_el = 0
        num_set = set(nums)
        visited_nums = set()

        for n in num_set:
            if not n in visited_nums:

                i = 0
                while n+i in num_set:
                    visited_nums.add(n+i)
                    curr_el+=1
                    i+=1

                max_el = max(max_el, curr_el)
                curr_el = 0

        return max_el
