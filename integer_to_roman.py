class Solution:
    def intToRoman(self, num: int) -> str:
        
        a = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
       
        # Result Variable
        r = ''
       
       
        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If i in list then add the roman value to result variable
            while i <= num:
                r += a[i]
                num = num-i
        return r
