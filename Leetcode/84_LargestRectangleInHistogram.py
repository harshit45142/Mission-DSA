def largestRectangle(h):
    stack = []  
    max_area = 0
    n = len(h)

    for i in range(n):
        while stack and h[i] < h[stack[-1]]:
            height = h[stack.pop()]
           
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = h[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area
