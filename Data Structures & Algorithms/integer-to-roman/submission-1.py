class Solution:
    def intToRoman(self, num: int) -> str:
        VALUES_TO_NUMERAL = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        result = ""
        
        div = 1
        while num // (div * 10) > 0:
            div *= 10

        while num > 0:
            digit = num // div
            if digit == 9:
                result += VALUES_TO_NUMERAL[div]
                result += VALUES_TO_NUMERAL[div * 10]
                num -= digit * div
                div /= 10
            elif digit >= 5:
                result += VALUES_TO_NUMERAL[div * 5]
                num -= 5 * div
            elif digit == 4:
                result += VALUES_TO_NUMERAL[div]
                result += VALUES_TO_NUMERAL[div * 5]
                num -= digit * div
                div /= 10
            else:
                while digit > 0:
                    result += VALUES_TO_NUMERAL[div]
                    num -= div
                    digit -= 1
                div /= 10
        return result






