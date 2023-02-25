number = 10
print("Variable number:", number, id(number))
number += 2
print("Variable number:", number, id(number))
# zmienia id

text = "Africa"
print("Variable text:", text, id(text))
text += "is hot"
print("Variable text:", text, id(text))
# zmienia id

list = [1, 2, 3]
print("Variable lista", list, id(list))
list.append(4)
print("Variable lista", list, id(list))
# nie zmienia id

list2 = list
print("Variable lista2", list2, id(list2))
list2.append(5)
print("Variable lista2", list2, id(list2))
print("Variable lista", list, id(list))
# do list i list2 zostało dodane 5, ponieważ listy miały to samo id (miejsce w pamięci)

list3 = list.copy()
print("Variable lista", list, id(list))
print("Variable lista3", list3, id(list3))
list3.append(6)
print("Variable lista", list, id(list))
print("Variable lista3", list3, id(list3))
# tworzymy kupie list z nowym id wiec 6 dodana tylko do list3