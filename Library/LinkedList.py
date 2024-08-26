
class LinkedList:
	def __init__(self, val: int):       
		self.val : int = val # 节点值
		self.next : LinkedList | None = None # 指向下一节点的引用

	# # 插入节点
	# def insert(self,n0: LinkedList, P: LinkedList):     
	# 	"""在链表的节点 n0 之后插入节点 P"""
	# 	n1 = n0.next 
	# 	P.next = n1 
	# 	n0.next = P

	# # 删除节点
	# def remove(n0: LinkedList):  
	# 	"""删除链表的节点 n0 之后的首个节点"""
	# 	if not n0.next:
	# 		return
	# 	# n0 -> P -> n1
	# 	P = n0.next
	# 	n1 = P.next
	# 	n0.next = n1

	# # 访问节点
	# def access(head:LinkedList,index:int) -> LinkedList:
	#    	"""访问链表中索引为 index 的节点"""
	#    	for _ in range(index):
	#    		if not head:
	#    			return None
	#    		head = head.next
	#    	return head

	# # 查询节点
	# def find(head:LinkedList,target:int) -> int:

	#     """在链表中查找值为 target 的首个节点"""
	#     index = 0
	#     while head:
	#     	if head.val == target:
	#     		return index
	#     	head = head.next
	#     	index += 1
	#     return -1   