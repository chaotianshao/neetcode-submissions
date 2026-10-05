class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        nums = []
        for char in tokens:
            if char not in op:
                nums.append(int(char))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if char == "+":
                    nums.append(num1 + num2)
                elif char == "-":
                    nums.append(num1 - num2)
                elif char == "*":
                    nums.append(num1 * num2)
                else:
                    nums.append(int(num1 / num2))
        
        return nums[-1]