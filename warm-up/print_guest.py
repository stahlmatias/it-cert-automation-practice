def guest_list(guests):
  for guest in guests:
    name = guest[0]
    age = guest[1]
    proffesion = guest[2]
    print("{name} is {age} years old and works as {proffesion}." .format(name=name, age=age, proffesion=proffesion))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


