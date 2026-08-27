# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        p=None 
        while s:
            n=s.next
            s.next=p
            p=s
            s=n
        l=head
        r=p
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True



        