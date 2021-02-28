import math
def armstrong(value):
    if not value:
        return False
    else:
        str_value = str(value)
        length = len(str_value)
        total=0
        while length>0:
            current_value = int(str_value[length-1])
            total += current_value * current_value * current_value
            length-=1
        return total==value

if __name__ == "__main__":
    print('Enter the number')
    armstrong(input())

       