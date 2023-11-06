# Define your functions here
def int_to_reverse_binary(n):
    bi = []
    while n >0:
        bi.append(n%2)
        n = n // 2
    return bi
    
def string_reverse(n):
    return list(reversed(n))

if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    num = int(input())
    temp = int_to_reverse_binary(num)
    temp = string_reverse(temp)

    # for i in temp:
    #     print(i,end='')
    print()
