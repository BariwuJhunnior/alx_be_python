length = int(input("Enter the size of the pattern: "))

rows = 0

while rows < length:
  for cols in range(length):
    print("*", end="")
  print()

  rows += 1