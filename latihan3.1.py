stack = []

stack.append("Aku")
stack.append("Anak")
stack.append("Indonesia")
print(stack)

search = stack.index("Anak")
while search != -1 and search > 0:
    stack.pop()
    search -= 1

    print (stack.pop())
    print (not stack)