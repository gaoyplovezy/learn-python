# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	print(head)
    	cur, prev = head, None
    	while cur:
    		cur.next, prev, cur = prev, cur, cur.next
    	return prev

if __name__ == "__main__":
	'''
	for i in range(1,6):
		Solution.reverseList(ListNode(i))
	'''
	g = Solution
	print(g.reverseList())

# leetcode submit region end(Prohibit modification and deletion)
