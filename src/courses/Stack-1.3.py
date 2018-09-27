def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return closest_mod_5(x + 1)


print(closest_mod_5(11))
