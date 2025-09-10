def trap_brute_force(height: list[int]) -> int:
    if not height:
        return 0
    
    n = len(height)
    total_water = 0

    for i in range(1, n - 1):  
        left_max = height[i]
        for j in range(i):
            left_max = max(left_max, height[j])
        
        right_max = height[i]
        for j in range(i + 1, n):
            right_max = max(right_max, height[j])
        
        water_at_current = min(left_max, right_max) - height[i]
        if water_at_current > 0: 
            total_water += water_at_current
            
    return total_water
