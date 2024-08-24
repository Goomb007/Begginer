immutable_var = 1, True, "Привет", 1.5
print(immutable_var)
# immutable_var[0] = 2 <- пытаемся поменять значение первого элемента в кортеже на другое
# print(immutable_var[0]) <- выводим значение в принте
#  immutable_var[0] = 2
# TypeError: 'tuple' object does not support item assignment <- ловим ошибку,
                                              # что кортеж(tuple) не поддерживает смену элементов
mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 3
print(mutable_list)