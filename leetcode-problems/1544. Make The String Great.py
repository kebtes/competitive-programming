class Solution:
    def makeGood(self, s: str) -> str:
        string = str(s)
        output = []

        for char in string:
            if output and (char.islower() and output[-1].isupper() and output[-1].lower() == char or char.isupper() and output[-1].islower() and output[-1].upper() == char):
                output.pop()

            else:
                output.append(char)

        return "".join(output)

        