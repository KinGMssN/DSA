# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        s=''
        while temp.next is not None:
            s=s+str(temp.val)
            temp=temp.next
        s=s+str(temp.val)
        if s==s[::-1]:
            return True
        else:
            return False
        



        