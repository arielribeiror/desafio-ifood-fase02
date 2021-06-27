def obj_to_list(restaurants, i, name, rate, shipping):
  restaurants[i].name = name
  restaurants[i].rate = rate
  restaurants[i].shipping = shipping
  return restaurants[i]

restaurants = []

while len(restaurants) != 1:
  name = "Digite o nome do {}º de 6 restaurantes mais próximos de você: ".format(len(restaurants) + 1)
  rate = "Digite a nota do {}º de 6 restaurantes mais próximos de você (0 à 5): ".format(len(restaurants) + 1)
  shipping = "Digite a valor fo frete do {}º de 6 restaurantes mais próximos de você: R$ ".format(len(restaurants) + 1)
  # for i in range(len(restaurants)):
  #   restaurants.append(obj_to_list(restaurants, i, input(name), float(input(rate)), float(input(shipping))))
  
for obj in restaurants:
  print(obj.name, obj.rate, obj.shipping, sep=" ")

# for passnum in range(len(restaurants)-1,0,-1):
#   for i in range(passnum):
#     if restaurants[i] > restaurants[i+1]:
#       temp = restaurants[i]
#       restaurants[i] = restaurants[i+1]
#       restaurants[i+1] = temp