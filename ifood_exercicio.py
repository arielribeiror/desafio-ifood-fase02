restaurants = [
    ['Kibon Sorveteria - Saude', 4.9, 6.99],
    ['Makis Place - Saude', 4.7, 7.99],
    ['A Feijoada', 4.4, 9.90],
    ['Giraffas Carrefour Metrocar', 4.4, 5.99],
    ['Viena - Shopping Santa Cruz', 4.4, 12.49],
    ['Sukiya - Saude', 4.6, 7.99]
]

i = 0
j = 1
element = 0
length = len(restaurants)

while element < length:
    while j < length:
        if restaurants[i][1] < restaurants[j][1]:
            evaluation = restaurants[i]
            restaurants[i] = restaurants[j]
            restaurants[j] = evaluation
        elif restaurants[i][1] == restaurants[j][1]:
            if restaurants[j][2] < restaurants[i][2]:
                deliveryTax = restaurants[i]
                restaurants[i] = restaurants[j]
                restaurants[j] = deliveryTax
        else:
            evaluation = restaurants[i]
        i += 1
        j += 1
    i = 0
    j = 1
    element += 1

for restaurant in restaurants:
    print(restaurant)