camel_case = input("camelCase: ")

snake_case = ""

for char in camel_case:
    # Если символ является заглавной буквой
    if char.isupper():
        # Добавляем нижнее подчеркивание перед ним и делаем его строчным
        snake_case += "_" + char.lower()
    else:
        # Если символ строчный, добавляем его без изменений
        snake_case += char

print("snake_case:", snake_case)
