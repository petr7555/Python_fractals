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
            "\" style=\"fill:white;stroke:black;stroke-width:0.1\" />\n")


class Vertex:
    def __init__(self, x, y, length, radians):
        self.x = x
        self.y = y
        self.length = length
        self.radians = radians

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_left_branch_vertex(self):
        l = self.length / 2
        x = self.x - l * math.sin(self.radians)
        y = self.y + l * math.cos(self.radians)
        return Vertex(x, y, l, radians)

    def get_right_branch_vertex(self):
        l = self.length / 2
        x = self.x + l * math.sin(self.radians)
        y = self.y + l * math.cos(self.radians)
        return Vertex(x, y, l, radians)


class Tree:

    def __init__(self, a, b, depth="No argument"):
        self.vertices = [a, b]
        tree_to_svg(self)
        self.branches = [None, None]
        if depth != "No argument":
            self.divide(depth)

    def divide(self, depth="No argument"):
        if depth == "No argument":
            for i in range(2):
                a = self.vertices[i]
                if i == 0:
                    b = self.vertices[i].get_left_branch_vertex()
                else:
                    b = self.vertices[i].get_right_branch_vertex()
                self.branches[i] = Tree(a, b)
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

degrees = 60
radians = math.radians(degrees)
length = 5
a = Vertex(10, 0, length, radians)
b = Vertex(10, 5, length, radians)
t = Tree(a, b, 1)

with open("tree.svg", "a") as f:
    f.write("</svg>\n")
