class Solution:
    #def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):

        answer = []

        if not head:
            return []

        i = len(head) - 1

        while i >= 0:
            answer.append(head[i])
            i -= 1

        return answer

head = []

solution = Solution()

print(solution.reverseList(head=head))

