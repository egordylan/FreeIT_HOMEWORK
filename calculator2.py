a = input('''  Введите строку из трех целых чисел, и двух знаков
(допускаются знаки "+", "-", "*", "/"). Выражение
вводится как символьная строка, все числа целые. Операция "/"
выполняется как целочисленное деление.

  Ввести выражение: ''', )

code = compile(a, "<string>", "eval")
b = (eval(code))

print(int(b))
