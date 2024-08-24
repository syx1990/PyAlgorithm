import random

# 定义数组,初始化数组
class Array:
	def index(self):
		arr: list[int] = [0] * 5
		nums:list[int] = [1,3,2,5,4]
		return (arr,nums)

	# 随机访问元素
	def random_access(self,nums:list[int]) -> int:
		"""随机访问元素"""
		# 在区间 [0, len(nums)-1] 中随机抽取一个数字
		random_index = random.randint(0,len(nums) - 1)
		# 获取并返回随机元素
		random_num = nums[random_index]

		return random_num

	# 数组中插入元素
	def insert(self,nums:list[int],num:int,index:int):
	    """在数组的索引 index 处插入元素 num"""
	    # 把索引 index 以及之后的所有元素向后移动一位
	    for i in range(len(nums) - 1, index, -1):
	        nums[i] = nums[i - 1]
	    # 将 num 赋给 index 处的元素
	    nums[index] = num

	# 删除元素
	def remove(self,nums:list[int],index:int):
		"""删除索引 index 处的元素"""
		# 把索引 index 之后的所有元素向前移动一位
		for i in range(index,len(nums) - 1):
			nums[i] = nums[i + 1]

	# 遍历数组
	def traverse(self,nums:list[int]):
		"""遍历数组"""
		count = 0
		# 通过索引遍历数组
		for i in range(len(nums)):
			count += nums[i]
		# 直接遍历数组元素
		for num in nums:
			count += num
		# 同时遍历数据索引和元素
		for i,num in enumerate(nums):
			count += nums[i]
			count += num

		return nums

	# 查找元素
	def find(self,nums:list[int],target:int) -> int:
		"""在数组中查找指定元素"""
		for i in range(len(nums)):
			if nums[i] == target:
				return i

		return -1

	# 扩容数组
	def extend(self,nums: list[int], enlarge: int) -> list[int]:
		"""扩展数组长度"""
		# 初始化一个扩展长度后的数组
		res = [0] * (len(nums) + enlarge)
		# 将原数组中的所有元素复制到新数组
		for i in range(len(nums)):
			res[i] = nums[i] 
		# 返回扩展后的新数组
		return res
