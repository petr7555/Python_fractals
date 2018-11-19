import math


def tree_to_svg(tree):
    a, b = tree.get_vertices()
    ax = str(a.get_x())
    ay = str(a.get_y())
    bx = str(b.get_x())
    by = str(b.get_y())
    with open("tree.svg", "a") as f:
        f.write(
            "<line x1=\"" + ax + "\" y1=\"" + ay + "\" x2=\"" + bx + "\" y2=\"" + by +
            "\" style=\"fill:white;stroke:black;stroke-width:" + str(0.01 * SCALE) + "\" />\n")


class Vertex:
    def __init__(self, x, y, length, degrees):
        self.x = x
        self.y = y
        self.length = length
        self.degrees = degrees

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_left_branch_vertex(self):
        l = self.length * RATIO
        x = self.x - l * math.sin(math.radians(self.degrees))
        y = self.y + l * math.cos(math.radians(self.degrees))

        return Vertex(x, y, l, self.degrees)

    def get_right_branch_vertex(self):
        l = self.length * RATIO
        x = self.x + l * math.sin(math.radians(self.degrees))
        y = self.y + l * math.cos(math.radians(self.degrees))
        return Vertex(x, y, l, self.degrees)


class Tree:

    def __init__(self, a, b, depth="No argument"):
        self.vertices = [a, b]
        tree_to_svg(self)
        self.branches = [None, None]
        if depth != "No argument":
            self.divide(depth)

    def divide(self, depth="No argument"):
        if depth == "No argument":
            a = self.vertices[1]
            self.branches[0] = Tree(a, a.get_left_branch_vertex())
            self.branches[1] = Tree(a, a.get_right_branch_vertex())
            return True
        if depth < 1:
            return False
        self.divide()
        for i in range(2):
            self.branches[i].divide(depth - 1)
        return True

    def get_vertices(self):
        return self.vertices


with open("tree.svg", "w") as f:
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    f.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\n")

SCALE = 10
RATIO = 2 / 3
DEGREES = 20
LENGTH = 5 * SCALE
a = Vertex(10 * SCALE, 0 * SCALE, LENGTH, DEGREES)
b = Vertex(10 * SCALE, 10 * SCALE, LENGTH, DEGREES)
t = Tree(a, b, 8)

with open("tree.svg", "a") as f:
    f.write("</svg>\n")
