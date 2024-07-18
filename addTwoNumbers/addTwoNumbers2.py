class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        head = ListNode(0)
        current = head
        carry = 0
        
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry, value = divmod(total, 10)
            
            current.next = ListNode(value)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        result = reverseList(head.next)
        return result
