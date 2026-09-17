#Stacks
#A Stack is a linear data structure where the element that is added last is removed first.
#This pincipals call LIFO - Last IN First OUT 
#stack operations are push,pop,peek and isempty
stack=[]
stack.append("java")
stack.append("python")
stack.append("sql")
print(stack)
print(len(stack))
print(stack[-1])
print(stack.pop())
print(stack)
for skills in stack:
    print(skills)

