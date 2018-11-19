def triangle_to_svg(triangle):
    a, b, c = triangle.get_vertices()
    ax = str(a.get_x())
    ay = str(a.get_y())
    bx = str(b.get_x())
    by = str(b.get_y())
    cx = str(c.get_x())
    cy = str(c.get_y())
    with open("sierpinksi_triangle.svg", "a") as f:
        f.write(
            "<polygon points=\"" + ax + "," + ay + " " + bx + "," + by + " " + cx + "," + cy +
            "\" style=\"fill:white;stroke:black;stroke-width:1\" />\n")


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def create_middle(self, other_vertex):
        x = (self.get_x() + other_vertex.get_x()) / 2
        y = (self.get_y() + other_vertex.get_y()) / 2
        return Vertex(x, y)


class Triangle:

    def __init__(self, a, b, c, depth="No argument"):
        self.vertices = [a, b, c]
        triangle_to_svg(self)
        self.smaller_triangles = [None, None, None]
        if depth != "No argument":
            self.divide(depth)

    def divide(self, depth="No argument"):
        if depth == "No argument":
            for i in range(3):
                a = self.vertices[i]
                b = self.vertices[i].create_middle(self.vertices[(i + 1) % 3])
                c = self.vertices[i].create_middle(self.vertices[(i + 2) % 3])
                self.smaller_triangles[i] = Triangle(a, b, c)
            return True
        if depth < 1:
            return False
        self.divide()
        for i in range(3):
            self.smaller_triangles[i].divide(depth - 1)
        return True

    def get_vertices(self):
        return self.vertices


with open("sierpinksi_triangle.svg", "w") as f:
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    f.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\n")

a = Vertex(0, 86.6)
b = Vertex(100, 86.6)
c = Vertex(50, 0)
t = Triangle(a, b, c, 5)

with open("sierpinksi_triangle.svg", "a") as f:
    f.write("</svg>\n")
