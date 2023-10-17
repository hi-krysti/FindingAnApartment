def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...')

apt_search1('Detroit', 1500, 3, True)
apt_search1('Chicago', 3500, 2, False)


def apt_search2(city, max_rent, min_beds = 2, pets_allowed = True):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...')

apt_search2('Toledo', 750)
apt_search2('Toledo', 750, 3)
apt_search2('Toldeo', 750, pets_allowed=False)


plus_one_hundred = lambda x: x + 100
square_num = lambda x: x ** 2
concatenate = lambda x: '- ' + x
divide_by_three = lambda x: x / 3

print(plus_one_hundred(1))
print(square_num(5))
print(concatenate('hello'))
print(divide_by_three(12))