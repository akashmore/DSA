class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)[::-1]
        if number[-1] == "-":
            number = int("-"+number[:-1])
        if -2147483648 < int(number) < 2147483647:
            return int(number)
        else:
            return 0