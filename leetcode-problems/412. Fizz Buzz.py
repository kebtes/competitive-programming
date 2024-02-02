class Solution:
    def fizzBuzz(self, n):
        output = []
        
        for i in range(1,n+1):
            answer = ""

            if i%3 == 0: answer += "Fizz"
            if i%5 == 0: answer += "Buzz"

            if answer == "": answer = str(i)
            output.append(answer)
        
        return output

            