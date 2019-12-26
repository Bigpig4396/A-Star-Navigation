"""
    This is a modified version of the A* search based on the python code
    from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    Date: Dec, 5, 2019
"""
import numpy as np

class Node(object):
    """Cell in the 2D grid map"""
    def __init__(self, parent=None, position=None):
        """
        Initialization function:
            Input:
                parent: Node, parent cell of the current cell
                position: 1x2 array, position of the current cell
        """
        self.parent = parent
        self.position = position

        self.g = 0  # cost of the current path
        self.h = 0  # cost of the heuristic
        self.f = 0  # total cost

    def __eq__(self, other):
        """
        Check two same cells
        """
        return np.array_equal(self.position, other.position)

    def info(self):
        """
        Information printing function
        """
        print('Current position = ', self.position)
        print('Current cost = ', self.g)
        print('Heuristic cost = ', self.h)
        print('Total cost = ', self.f)

def A_star(temp_maze, start, end):
    # print("A star search begin: Start {} - End {}".format(start, end))
    maze = temp_maze.copy()
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0

    # convert to numpy
    start = np.array(start)
    end = np.array(end)
    maze = np.array(maze)

    # Create start and end node (initialize)
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []  # contains the node that need to be explored
    closed_list = []  # contains the node that are already explored

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # obtain the node with the least f value in open list
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # check if we reach the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[::-1]  # Return reversed path

        # remove the current node from the open list
        open_list.pop(current_index)
        # add the current node into closed list
        closed_list.append(current_node)

        # Generate neighbors
        children = []
        for pos in [[0, -1], (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            # Get node position
            node_pos = current_node.position + np.array(pos)

            # Make sure within range
            if node_pos[0] > maze.shape[0] - 1 or node_pos[0] < 0 or node_pos[1] > maze.shape[1] - 1 or node_pos[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_pos[0], node_pos[1]] == 1.0:
                continue

            # create a candidate node
            new_node = Node(current_node, node_pos)

            # if current node is already searched
            in_close_flag = False
            for closed_child in closed_list:
                if new_node == closed_child:
                    in_close_flag = True
                    break
            if in_close_flag:
                continue

            # compute the measures of current node
            new_node.g = current_node.g
            new_node.h = abs(new_node.position[0] - end[0]) + abs(new_node.position[1] - end[1])
            new_node.f = new_node.g + new_node.h

            # check whether add it into the open list
            in_open_flag = False
            for open_node in open_list:
                if not (open_node == new_node):
                    continue
                else:
                    in_open_flag = True
                    if open_node.f > new_node.f:
                        open_list.append(new_node)

            if not in_open_flag:
                open_list.append(new_node)
    return []



