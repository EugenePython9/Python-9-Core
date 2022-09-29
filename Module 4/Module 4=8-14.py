def game(terra, power):
    energy = power
    print(energy)
    for ostrov in terra:
        for E in ostrov:
            if energy >= E:
                energy += E
                
            else:
                break
            print(energy)
        print('level ', energy)
    return energy

print('SUM ', game([[1, 1, 5, 10], [10, 2], [1, 1, 1]],1))
