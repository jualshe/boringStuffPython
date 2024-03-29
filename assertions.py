# assert False, 'This is the error message'

# traffic simulator program

market_2nd = {'ns': 'green', 'ew': 'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


# assert that this condition is always holds true, if not- there is a bug in a program

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
