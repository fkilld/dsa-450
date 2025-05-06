class Solution:
    def trap(self, arr, n):
        """
        Method to calculate trapped water using extra space
        Args:
            arr: List of heights of blocks
            n: Number of blocks
        Returns:
            Total water trapped
        """
        # Arrays to store maximum height of bar from left and right ends
        l = [0] * n  # Stores max height from left up to current position
        r = [0] * n  # Stores max height from right up to current position

        ans = 0  # Total water trapped initialization
        
        # Initialize the first and last values of left and right arrays
        max_left = l[0] = arr[0]  # Max height from left starts with first element
        max_right = r[n - 1] = arr[n - 1]  # Max height from right starts with last element

        # Step 1: Calculate maximum height from left for each position
        for i in range(1, n):
            if max_left < arr[i]:
                max_left = arr[i]  # Update max_left if current height is greater
            l[i] = max_left  # Store max height from left for this position
        
        # Step 2: Calculate maximum height from right for each position
        for i in range(n-2, -1, -1):  # Traverse from right to left
            if max_right < arr[i]:
                max_right = arr[i]  # Update max_right if current height is greater
            r[i] = max_right  # Store max height from right for this position
        
        # Step 3: Calculate water trapped at each position
        for i in range(n):
            # Water trapped at current position is min of left and right max heights minus current height
            ans += min(l[i], r[i]) - arr[i]

        return ans
    
    def trap2(self, arr, n):
        """
        Method to calculate trapped water without using extra space (two-pointer approach)
        Args:
            arr: List of heights of blocks
            n: Number of blocks
        Returns:
            Total water trapped
        """
        ml = mr = 0  # Initialize max left and max right heights
        lo = 0       # Left pointer starts at beginning of array
        hi = n - 1   # Right pointer starts at end of array
        ans = 0      # Total water trapped initialization
        
        # Step 1: Use two pointers to traverse the array
        while lo <= hi:
            # Step 2: Compare heights at left and right pointers
            if arr[lo] <= arr[hi]:
                # If left side has smaller or equal height
                if arr[lo] > ml:
                    ml = arr[lo]  # Update max left height
                else:
                    # Water trapped at current left position
                    ans += ml - arr[lo]
                lo += 1  # Move left pointer right
            else:
                # If right side has smaller height
                if arr[hi] > mr:
                    mr = arr[hi]  # Update max right height
                else:
                    # Water trapped at current right position
                    ans += mr - arr[hi]
                hi -= 1  # Move right pointer left
        
        return ans