from pathlib import Path

path = Path("ecommerce")
print(path.exists())  # o/p-True

path2 = Path("emails")
path2.rmdir()
