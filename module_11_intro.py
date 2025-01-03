def introspection_info(obj):
    # получение типа объекта
    obj_type = type(obj).__name__
    # получение атрибутов объекта
    attributes = dir(obj)
    # получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]
    # определение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', '__main__')
    # создание словаря с информацией об объекте
    info = {'type':obj_type, 'attributes': attributes,
            'methods': methods, 'module': module}

    return info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)
# Интроспекция строки
string_info = introspection_info('Hello world')
print(string_info)
# Интроспекция списка
list_info = introspection_info([1, 5, 2.5, 'people'])
print(list_info)
