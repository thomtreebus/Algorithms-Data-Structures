class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(grid, start, end):
    # create start and end nodes
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # initialize open and closed list
    open_list = []
    closed_list = [] # use set for O(1) lookups

    # add start node
    open_list.append(start_node)

    # loop through list until end node is found
    while open_list:
        # locate current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop current node from open list and add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # found the goal
        if current_node == end_node:
            path = generate_path(current_node)
            return path[::-1]
        
        # generate children
        children = generate_children(grid, current_node)

        for child in children:
            if child in closed_list:
                continue
            
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if child in open_list:
                continue
            
            open_list.append(child)
def generate_path(current_node):
    path = []
    current = current_node
    while current:
        path.append(current.position)
        current = current.parent
    return path
    
def generate_children(grid, current_node):
    children = []
    adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for x, y in adjacent_squares:
        new_x = current_node.position[0] + x
        new_y = current_node.position[1] + y
        if new_x > (len(grid)-1) or new_x < 0 or new_y > (len(grid[0]) - 1) or new_y < 0:
            continue
        
        if grid[new_x][new_y] != '0':
            continue

        new_node = Node(current_node, (new_x, new_y))
        children.append(new_node)
    return children

def print_path(grid, path):
    grid[path[0][0]][path[0][1]] = 'S'
    path.pop(0)
    end = path[-1]
    grid[end[0]][end[1]] = 'E'
    path.pop()
    for x, y in path:
        grid[x][y] = 'x'
    
    for row in grid:
        print(row)

def main():
    grid = [['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0,0)
    end = (7, 6)

    path = astar(grid, start, end)
    print_path(grid, path)


main()
            
            