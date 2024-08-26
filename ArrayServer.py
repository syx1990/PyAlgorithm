from Library.Array import Array

class ArrayServer:
	def run(self):
		arr = Array()   
		result = arr.index()
		print(result)
		# 随机输出数组的数字    
		nums:list[int] = [1,3,2,5,4]
		print("数组 nums = {}".format(nums))
		random_num :int = arr.random_access(nums)
		print("在 nums 中获取随机元素", random_num)
		# 随机输出数组的数字    
		nums:list[int] = [1,3,2,5,4]  
		print("数组 nums = {}".format(nums))
		random_num :int = arr.random_access(nums)
		print("在 nums 中获取随机元素", random_num)
		# 插入元素
		arr.insert(nums,6,3)
		print("在索引 3 处插入数字 6 ，得到 nums =", nums)  
		# 删除元素
		arr.remove(nums,2)
		print("删除索引 2 处的元素，得到 nums ={}".format(nums))  
		# 遍历数组
		print("数组 nums ={}".format(arr.traverse(nums)))
		# 查询元素
		index :int = arr.find(nums,3)
		print("在 nums 中查找元素 3 ，得到索引 =", index) 
		# 长度扩展
		nums = arr.extend(nums,3)
		print("将数组长度扩展至 8 ，得到 nums ={}".format(nums))
