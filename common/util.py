def location_to_point(n, location_id):
    x = location_id // n
    y = location_id % n
    return (x, y)


def point_to_location(n, point):
    x, y = point
    return x * n + y


def matrix_to_array(mat):
    n = len(mat)
    arr = []
    for x in range(n):
        arr += mat[x]
    return arr


def array_to_matrix(arr):
    n = int(len(arr) ** 0.5)
    mat = []
    for x in range(n):
        mat.append(arr[x*n:(x+1)*n])
    return mat


def print_matrix(mat):
    n = len(mat)
    for y in range(n):
        for x in range(n):
            print(mat[x][-y-1], end=' ')
        print()


def parse_locations(locations):
    arr = [0] * len(locations)
    for location in locations:
        arr[location['id']] = location['located_bikes_count']
    return arr
