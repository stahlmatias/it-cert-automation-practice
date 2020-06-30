def squares(start, end):
  return [ n**2 for n in range(0, end + 1) ]

print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
