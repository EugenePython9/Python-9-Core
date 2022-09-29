points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) < 2:
        return 0
    prev_coor = None
    length = 0
    for coor in coordinates:        
        
        if prev_coor == None:
            prev_coor = coor
            continue
        next_coor = coor
        min_coor = min(next_coor, prev_coor)
        max_coor = max(next_coor, prev_coor)
        length += points[(min_coor, max_coor)]
        
        print(f'coor {coor}, prev_coor {prev_coor}, next_coor {next_coor}, min_coor {min_coor},max_coor {max_coor}, length {length}')

        prev_coor = coor
            
    return length

print(calculate_distance([0, 1, 3, 2, 0]))