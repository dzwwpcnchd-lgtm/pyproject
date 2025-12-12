from math_tools import add,max
import os
from pathlib import Path

print(add(1,2))
print(max(1,2))

file_and_dictionary = os.listdir()
print(file_and_dictionary)

p= Path("exercise/data")
p.mkdir(parents=True,exist_ok=True)
# p.rmdir()