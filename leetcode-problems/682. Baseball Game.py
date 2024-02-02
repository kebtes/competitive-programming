class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for char in operations:
            if char.isdigit():
                output.append(int(char))
            elif str(char)[0] == '-' and len(char) > 1 and char[1:].isdigit():
                output.append(int(char))

            if char == "D":
                output.append(output[-1]*2)
            elif char == "C":
                output.pop()
            elif char == "+":
                x = output[-1] + output[-2]
                output.append(x)
        
        return sum(output)