location_id_left = []
location_id_right = []

def find_total_distance():
    x = 0
    total_distance = 0

    for number in location_id_right:
        total_distance += abs(location_id_left[x] - number)
        x+=1
    return total_distance

def load_and_sort_file():
    with open("input.txt", 'r') as file:
        for line in file:
            left, right = line.strip().split()
            location_id_left.append(int(left))
            location_id_right.append(int(right))

    location_id_left.sort()
    location_id_right.sort()
    
    return location_id_left, location_id_right

def find_sim_score():
    sim_score = 0
    for number in location_id_left:
        count = location_id_right.count(number)
        sim_score += number * count
    return sim_score

load_and_sort_file()
print("Part 1: ", find_total_distance())
print("Part 2: ", find_sim_score())