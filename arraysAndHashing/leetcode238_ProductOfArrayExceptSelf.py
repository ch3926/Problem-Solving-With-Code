# Jan 7, 2024
def productExceptSelf(nums):
    products = [1] * len(nums)

    for i in range(1, len(nums)):
        products[i] = products[i-1] * nums[i-1]
    
    after = 1
    for i in range(len(nums) -1, -1, -1):
        products[i] *= after
        after *= nums[i]
    return products



nums = 1,2,3,4

print(productExceptSelf(nums))