class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        def valid_combinations(sub_candidates, target, current_sum, cur_set):
            if current_sum == target:
                res.append(cur_set)
                return
            elif current_sum > target:
                return
            else:
                if sub_candidates:
                    # Include the first element and recurse
                    new_cur_set = cur_set + [sub_candidates[0]]
                    valid_combinations(sub_candidates, target, current_sum + sub_candidates[0], new_cur_set)

                    # Exclude the first element and recurse
                    new_cur = sub_candidates[1:]
                    valid_combinations(new_cur, target, current_sum, cur_set)

        res = []
        valid_combinations(candidates, target, 0, [])
        return res
