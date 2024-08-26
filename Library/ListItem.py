
# 定义列表
class ListItem:

	# 列表基础知识整理
	def basicListPrint(self):   
		num:list[int] = []  
		print("初始化列表:{}".format(num))
		nums:list[int] = [1,3,2,5,4]
		print("列表{}".format(nums))

		print("访问元素",nums[1])
		nums[1] = 0
		print("列表{}".format(nums))

		# 清空列表
		nums.clear()

		# 在尾部添加元素
		nums.append(1)
		nums.append(3)
		nums.append(2)
		nums.append(5)
		nums.append(4)
		# 在中间插入元素
		nums.insert(3, 6)  # 在索引 3 处插入数字 6
		# 删除元素
		nums.pop(3)        # 删除索引 3 处的元素
		print("列表{}".format(nums))

		# 通过索引遍历列表
		count = 0
		for i in range(len(nums)):
			count += nums[i]

		# 直接遍历列表元素
		for num in nums:
			count += num

		return -1     