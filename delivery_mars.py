import sys


def sort(data):
    swapped = [None]
    last_index = len(data) - 1
    while swapped is not False:
        swapped = False
        for item in range(last_index):
            next_item = item + 1

            if data[item] > data[next_item]:
                data[item], data[next_item] = data[next_item], data[item]
                swapped = True

        last_index -= 1
    return data


def main():
    robots = []
    limit = 0
    robots = (sys.stdin.readline().rstrip()).split()
    limit = int(sys.stdin.readline().rstrip())
    cargo = 0
    plat = 0

    # print(robots)
    # print(limit)
    # cargo += robots[0]
    counter = 0

    robots = sort(robots)  

    while robots:
        plat += 1
        # print(f'----Plat = {plat}----')
        # print(f'Robots to load {robots}') 
        if counter == 0:
            # print(f'First robot with weight {robots[-1]} added to plat #{plat}')
            cargo += int(robots.pop(-1))
            # print(f'Weight = {cargo}')
            counter += 1
        if robots:
            # print(cargo, int(robots[0]), limit)
            if cargo + int(robots[0]) > limit:
                counter = 0
                cargo = 0
                # print('No robot to add, next plat')
            else:
                next_robot = None
                # print(f'Have robot to add to plat #{plat}')
                # print("Searching the biggest")
                # print(f'Robots to load {robots}')
                for robot in range(len(robots)):
                    if int(robots[robot]) + cargo <= limit:
                        next_robot = robot
                if next_robot is not None:
                    # print(f'Founded robot with {robots[next_robot]} weight.')
                    robots.pop(next_robot)
                    cargo = 0
                    counter = 0
                    # print(f'Second robot added to plat #{plat}')
                else:
                    counter = 0
                    cargo = 0
                    # print('No robot to add, next plat2')

    return plat


if __name__ == "__main__":
    print(main())
