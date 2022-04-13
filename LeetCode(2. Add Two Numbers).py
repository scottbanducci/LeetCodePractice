# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = l1
        first_string = ""
        while(first_list != None):
            first_string += str(first_list.val)
            first_list = first_list.next
        
        print(first_string)
        second_list = l2
        second_string = ""
        while(second_list != None):
            second_string += str(second_list.val)
            second_list = second_list.next
        
        
        first_num = int(first_string)
        second_num = int(second_string)
        
        soln = first_num+second_num
            
        soln_string = str(soln)
        print(soln_string)
        soln_node = ListNode()
        soln_copy = soln_node

        for i in range(len(soln_string)):
            soln_node.val = int(soln_string[((len(soln_string)-1)-(i))])

            if (i<len(soln_string)-1):
                iter_node = ListNode()
                soln_node.next = iter_node
                soln_node = iter_node
            
        
        print(soln_copy)
        return soln_copy
        