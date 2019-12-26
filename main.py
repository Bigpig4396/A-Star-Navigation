from search_method import A_star
import maze
import matplotlib.pyplot as plt

if __name__ == '__main__':

    maze_obj = maze.Maze(width=15, height=15, seed=0)
    grid_map = maze_obj.get_map()

    path = A_star(grid_map, [1, 1], [13, 13])
    print(path)

    plt.figure(figsize=(3, 3))
    plt.imshow(grid_map)
    plt.xticks([])
    plt.yticks([])
    plt.show()

