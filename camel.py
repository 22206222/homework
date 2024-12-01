name = input("Please enter a variable name in Camel Case:")
snake = ' '

for i in range(len(name)):
    if name[i].isupper():
        snake = snake + '_' + name[i].lower()
    else:
        snake += name[i]
print(snake)
