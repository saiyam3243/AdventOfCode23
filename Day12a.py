a = "?#####???????#.. 5,1,1,1"
a = "#?#???##??#.?#?#?#? 3,3,1,7"
a = a.split(" ")
print(a)
num = a[1].split(",")
s = ""
for i in num:
    s += i*int(i) + "."
s = s[:-1]
print(s)
print(len(s))

num = list(map(int,num))
print(num)
print(a[0])
print(len(a[0]))
b = a[0]
#b = [x for x in b if x]

print(b)

count = 0
modified = False
skip = False
for j in num:
    count = 0
    for i in b:
        if skip :
            skip = False
            continue
        if i == ".":
            continue
        if i == "#":
            j -= 1
            if j - count <= 0:
                modified = True
                skip = True
                break
        if i == "?":
            count += 1
            if count >= j:
                break
