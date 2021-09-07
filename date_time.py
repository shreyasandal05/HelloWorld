import datetime
from pathlib import Path

current_date_time = datetime.datetime.now()
print(current_date_time)
# Here we called now() method from 'datetime' class, from 'datetime' module

path = Path()
# print(path.mkdir())
# print(path.glob('*.*'))  # we get all files from directories and not directories
for file in path.glob('*'):
    print(file)
