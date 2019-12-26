# A-Star-Navigation

![image](https://github.com/Bigpig4396/A-Star-Navigation/blob/master/haha.png)

Hi, this is a A star algorithm for navigation, from any start point to any goal point as shown in picture.
the cells are 4-connected (cannot go diagonally). The map is given by a numpy array each element is 1(wall) or 0(free). The coordinate is like

![image](https://github.com/Bigpig4396/A-Star-Navigation/blob/master/coordinate.png)

from 0 to map size-1

The example generates a random maze of size 15, 15, the goal is to go from 1, 1 to 13, 13, the planned path is given by
[array([1, 1]), array([1, 2]), array([1, 3]), array([1, 4]), array([1, 5]), array([2, 5]), array([3, 5]), array([4, 5]), array([5, 5]), array([6, 5]), array([7, 5]), array([8, 5]), array([9, 5]), array([10,  5]), array([11,  5]), array([12,  5]), array([13,  5]), array([13,  6]), array([13,  7]), array([13,  8]), array([13,  9]), array([13, 10]), array([13, 11]), array([13, 12]), array([13, 13])]

## References
github.com/138paulmiller
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
