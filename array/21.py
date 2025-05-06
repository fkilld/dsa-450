# Factorials of large numbers
# This implementation allows calculating factorials of very large numbers
# without encountering integer overflow issues by using array-based arithmetic

class Solution:
    """
    A class that provides methods to calculate factorials of large numbers.
    
    The standard integer data types cannot handle very large factorials due to overflow.
    This class implements a method to compute factorials using array-based arithmetic.
    """

    def multiply(self, x, res, res_size):
        """
        Multiply the current factorial result stored in res[] with a number x.
        
        Args:
            x: The number to multiply with the current result
            res: Array storing the current factorial digits (in reverse order)
            res_size: Number of digits in the current result
        
        Returns:
            Updated size of the result after multiplication
        """
        carry = 0  # Initialize carry for the multiplication
        i = 0
        # Process each digit of the current result
        while i < res_size:
            prod = res[i] * x + carry  # Multiply current digit with x and add carry
            res[i] = prod % 10  # Store the last digit of the product
            carry = prod // 10  # Update the carry for the next iteration
            i += 1
        
        # Handle any remaining carry by adding new digits to the result
        while carry:
            res[res_size] = carry % 10  # Store the last digit of carry
            carry = carry // 10  # Update carry for next position
            res_size += 1  # Increase the result size as we add new digits

        return res_size  # Return the updated size of the result
        
    def factorial(self, n):
        """
        Calculate the factorial of n (n!).
        
        The factorial is calculated using array-based arithmetic to handle
        very large numbers. The result is returned as a list of digits.
        
        Args:
            n: The number for which factorial is to be calculated
        
        Returns:
            List of digits representing the factorial value (in correct order)
        """
        res = [0] * 3000  # Create an array to store digits (large enough for most practical cases)
        res[0] = 1  # Initialize result with 1 (0! = 1)
        res_size = 1  # Initial size of result is 1 digit

        # Calculate factorial by iterative multiplication
        x = 2
        while x <= n:
            res_size = self.multiply(x, res, res_size)  # Multiply current result with x
            x += 1  # Move to next number
            
        ans = []  # Initialize the final answer list
        # Convert the reversed digit array to a properly ordered list
        for i in range(res_size - 1, -1, -1):
            ans.append(res[i])
            
        return ans  # Return the factorial as a list of digits
