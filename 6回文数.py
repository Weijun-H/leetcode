class Solution:
    def isPalindrome(self, x: int) -> bool:
        digital = []
        num = x
        if x < 0:
            return False
        while num != 0:
            reminder = num % 10
            num = num//10
            digital.append(reminder)
        print(digital)
        return digital == digital[::-1]