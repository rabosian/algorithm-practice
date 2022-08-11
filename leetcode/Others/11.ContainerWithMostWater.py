# two pointer
def maxArea(height):
    if len(height) == 2:
        return min(height[0], height[1])

    maxWater = 0
    start, end = 0, len(height) - 1

    while start < end:
        area = (end-start) * min(height[start], height[end])
        if area > maxWater:
            maxWater = area
        if min(height[start], height[end]) == height[start]:
            start += 1
        else: end -= 1
    return maxWater

height = [2, 1, 2]
print(maxArea(height))
