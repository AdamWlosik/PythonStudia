x = "Hello Pycharm"
y = x
z = x + "!!"
print(x, y)
print(type(x), type(y))
print("Is value x, y the same:", x == y)
print("Is value x, z the same:", x == z)
print("Are the variables x,y the same:", x is y)
print("Are the variables x,z the same:", x is z)
print(id(x), id(y), id(z)) # adresy komórek w pamięci pc
d = z[:-2] # z bez 2 ostatnich znaków
print("Is value x, d the same:", x == d)
print("Are the variables x,d the same:", x is d)
print(id(x), id(d))

