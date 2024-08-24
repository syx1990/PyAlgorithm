import Array
import LinkedList
import ListItem        
# -*- coding:utf-8 -*-     

if __name__ == '__main__':
	array = Array.Array()
	result = array.index() # 初始化数组        
	print(result)

	# 随机输出数组的数字
	nums:list[int] = [1,3,2,5,4]
	print("数组 nums = {}".format(nums))
	random_num :int = array.random_access(nums)
	print("在 nums 中获取随机元素", random_num)

	# 插入元素
	array.insert(nums,6,3)
	print("在索引 3 处插入数字 6 ，得到 nums =", nums)  

	# 删除元素
	array.remove(nums,2)
	print("删除索引 2 处的元素，得到 nums ={}".format(nums))  
 
	# 遍历数组
	print("数组 nums ={}".format(array.traverse(nums)))

	# 查询元素
	index :int = array.find(nums,3)
	print("在 nums 中查找元素 3 ，得到索引 =", index) 

	# 长度扩展
	nums = array.extend(nums,3)
	print("将数组长度扩展至 8 ，得到 nums ={}".format(nums))

	# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
	# 初始化各个节点
	# n0 = LinkedList.LinkedList(1)  
	# n1 = LinkedList.LinkedList(3)
	# n2 = LinkedList.LinkedList(2) 
	# n3 = LinkedList.LinkedList(5)            
	# n4 = LinkedList.LinkedList(4)   
	# # 构建节点之间的引用
	# n0.next = n1
	# n1.next = n2 
	# n2.next = n3  
	# n3.next = n4

	# # 插入节点
	# p = LinkedList.LinkedList(0)                 
	# LinkedList.insert(n0,p)     

	# # 删除节点

	# # LinkedList.remove(n0)   


	# 基础知识列表
	List = ListItem.ListItem()   
	List.basicListPrint()       

