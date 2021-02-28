from math import pow


class Basic:
    def armstrong(self, value):
        if not value:
            return False

        string_value = str(value)
        length = len(string_value)
        total = 0
        while length > 0:
            current_value = int(string_value[length-1])
            total += pow(current_value, 3)
            length -= 1
        return value == total

    def factorial(self, value):
        fact = 1
        while value > 0:
            fact *= value
            value -= 1
        return fact
    
    def palindrome(self, value):
        str_value = str(value)
        length = len(str_value)
        result = str()
        while length:
            result += str_value[length-1]
            length-=1
        return result == str_value
