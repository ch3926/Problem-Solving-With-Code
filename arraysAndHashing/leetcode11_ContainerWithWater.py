# Jan 6, 2024 - Solution works... but is inefficient and exceeded time limit
def maxArea(height) -> int:
        most = 0
        for i, h1 in enumerate(height):
            r = len(height) - 1
            while i < r:
                currVol = min(h1,height[r]) * (r-i)
                if currVol > most:
                    most = currVol
                r -= 1
        return most


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# Jan 6, 2024 - Attempt 2
def maxArea(height):
    most = 0
    start = 0
    end = len(height) - 1
    most = 0

    while start < end:
        most = max(most, min(height[start], height[end]) * (end-start))
        if height[start] < height[end]: 
            start += 1
        elif height[start] >= height[end]: # if and elif and with only one checking equality, so that both pointers don't move!
            end -= 1
    return most
        
