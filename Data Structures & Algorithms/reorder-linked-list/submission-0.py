# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list into two halves
        second_head = slow.next
        slow.next = None

        # 3. Reverse the second half
        prev = None
        curr = second_head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        second_head = prev

        # 4. Merge the two halves
        first_head = head

        while first_head and second_head:
            next_first = first_head.next
            next_second = second_head.next

            first_head.next = second_head
            second_head.next = next_first

            first_head = next_first
            second_head = next_second