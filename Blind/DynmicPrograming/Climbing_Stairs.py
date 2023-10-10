class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        one_step_before = 2
        two_step_before = 1

        for i in range(2, n):
            current = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = current
        return current

solution = Solution()

n = 4

print(solution.climbStairs(n=n))