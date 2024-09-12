# task 1

def reversestring(a):
    list_a = list(a)
    ans = list_a[::-1]
    return ''.join(ans)

a = input("any string : ")
ans = reversestring(a)
print(ans)