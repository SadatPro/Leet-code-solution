class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while (curr != None):
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        return prev

