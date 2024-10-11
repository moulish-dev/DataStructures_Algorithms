#STATIC TYPING
#allows to add type annotations to code
#has tools to check errors at compile-time

# typing module
#improves readability
#enhances tooling support

from typing import List, Dict, Optional

#function that accepts a list of integers and returns a dictionary
def process_numbers(nums: List[int]) -> Dict[str, int]:
    total = sum(nums)
    return {'total': total}

# Optional typing: allows None to be passed
def get_username(user_id: int) -> Optional[str]:
    if user_id == 0:
        return None
    return "John Doe"

# type alias
from typing import List

#creating a custom type alias for charity
Vector = List[float]

def scale_vector(vector: Vector, scalar: float) -> Vector:
    return [x * scalar for x in vector]

# Mypy : Static Type Checker for Python
# type checking without executing code
# real time error checking

#  install mypy
#    pip install mypy
# run mypy on code
#    mypy my_script.py

def add_numbers(a: int, b: int) -> int:
    return a+b

#incorrect call
add_numbers("3", 4) 
#when run with mypy this will be spotted by mypy

# Pydantic : Data Validation with static typing
#mainly useful when working with external data
#automatically converts and validates data types
#supports complex nested data models

#install pydantic
#  pip install pydantic
from pydantic import Basemodel

class User(Basemodel):
    id: int
    name: str
    age: int

# pydantic will validate the data based on type hints
user = User(id=123, name="James", age="23")
print(user.age) #age string will be automatically be converted to integer

#Pyre : Fast Type Checker by Meta
# designed for large codebases
# fast and only checks changed code
# integrates with pyre server for live feedback

# installing pyre
#   pip install pyre-check

#setting up pyre
#   pyre init

#run pyre
#   pyre check

def greet(name: str) -> str:
    return "Hello, " + name

# Incorrect usage, as passing an integer instead of  string
greet(123)

#pyre will notify this error



# Pyright: static type checker by microsoft
#lightweight and fast
#real-time feedback 
#strict type-checking

# ALL TOOLS

# Typing: Use it in all Python projects for better readability and documentation.
# Mypy: Use for general-purpose static type checking in any Python project.
# Pydantic: Use in projects where you need to validate external data (e.g., APIs or user input).
# Pyre: Use if you need a fast type checker for large codebases with incremental checking.
# Pyright: Use with VS Code for real-time type checking and autocompletion in your Python projects.
