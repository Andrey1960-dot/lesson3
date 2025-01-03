def introspection_info(obj):
    # получение типа объекта
    obj_type = type(obj).__name__
    # получение атрибутов объекта
    all_attributes = dir(obj)
    # получение методов объекта
    all_methods = [method for method in all_attributes if callable(getattr(obj, method))and not method.startswith('__')]
    attributes = [attr for attr in all_attributes if not attr.startswith('__') and attr not in all_methods]
    # определение модуля, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', '__main__')
    # создание словаря с информацией об объекте
    info = {'type':obj_type, 'attributes': attributes,
            'methods': all_methods, 'module': obj_module},

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
