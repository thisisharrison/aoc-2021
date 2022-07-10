
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

def get_name_with_age(name: str, age: int):
    str_age = str(age)
    name_with_age = name + " is this old: " + str_age
    return name_with_age

print(get_name_with_age("john", 12))

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

# Creating a type
Vector = list[float] # try change this to str

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

from typing import NamedTuple

class ParseResult(NamedTuple): 
    name: str
    value: str

def parse_value(text: str): 
    '''
    Split text of the form name=val into (name, val)
    '''
    parts = text.split('=', 1)
    return ParseResult(parts[0].strip(), parts[1].strip())

result = parse_value('url=http://www.python.org')
print(result)
print(result.value)

