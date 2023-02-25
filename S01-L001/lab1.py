a = b = c = 10
print(a, b, c)
print(id(a), id(b), id(c))
a = 20
print(a, b, c)
print(id(a), id(b), id(c))

a = b = c = [1, 2, 3]
a += [4] # lub a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

x = 10
y = 10
print(id(x), id(y)) # różne zienne o tej samej wartości opytmalizator pythona nadaje to samo id

y = y + 1 - 1
print(id(x), id(y))
y = y + 1234567890 - 1234567890
print(id(x), id(y))
