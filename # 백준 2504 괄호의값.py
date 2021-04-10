# 백준 2504 괄호의값

s= list(input()) # input: (()[[]])([])
stack=[]
count=0

for i in s:
    if i== ')':
        temp=0   # 괄호가 완성되었을 때 괄호의 값 대신해서 들어갈 임시
        while len(stack) != 0:
            top=stack.pop(-1)
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break

            elif top =='[':
                print(0)
                exit(0)
            else:
                temp= temp + int(top)

    elif i == ']':
        temp=0
        while len(stack)!=값 0:
            top=stack.pop(-1)
            if top =='[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append((3*temp))
                break

            elif top =='(':
                print(0)
                exit(0)

            else:
                temp = temp + int(top)

    else:
        stack.append(i)     #  '(','['이 오면 stack에 담

# 스택안에 담긴 값 더하
for i in stack:
    if i=='('or i=='[':
        print(0)
        exit(0)

    else:
        count += i

print(count)