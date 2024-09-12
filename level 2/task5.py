# task 5

f = open("kuldip.txt","r")

a = list(f.read())

for i in range (len(a) -1, -1, -1):
    if a[i] == " ":
        a.pop(i)

an = sorted(a)
ans = {}
for i in an:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

print(ans)