import math


class collect_trash:
    # A: post office(560,440),B: T1 Building(605,700),C: T4 Building(860,535)
    # D: Administration Department(1020,535),E: 3rd Dormitory(890,270),F: T2 Building (1250,375)
    # The farther distance is, the higher coefficient of the trash can is.

    def setting(self, start, vertices):
        # start: (x0,y0) # vertices: a dictionary contains {(x,y):(weight,height)},
        # Find all trash cans with full garbage
        candidate = [
            vertex
            for vertex in vertices.keys()
            if (vertices.get(vertex)[0] > 5 or vertices.get(vertex)[1] > 5)
        ]
        output = []
        output.append(start)
        while (len(candidate) != 0):
            edge = self.edge_calculation(
                start, candidate)  # list -> dictionary
            sorted_vertices = [v for v in sorted(
                edge.items(), key=lambda d: d[1])]  # sort
            start = sorted_vertices[0][0][1]
            output.append(start)
            candidate.remove(start)
        final_output = []
        for i in range(0, len(output) - 1):
            final_output.append(
                [output[i], output[i + 1], i])
        return final_output

    # edge_calculation evaluates the set of distances between each vertices

    def edge_calculation(self, start, vertices):  # vertices: a list of vertices
        edge_distance = {}  # edge_distance : a dictionary
        for i in range(0, len(vertices)):
            distance = math.sqrt(
                math.pow((start[0] - vertices[i][0]), 2)
                + math.pow((start[1] - vertices[i][1]), 2)
            )
            edge_distance[(start, vertices[i])] = distance
        # for i in range(0, len(vertices)):  # Pythagorean theorem
        #     for j in range(i + 1, len(vertices)):
        #         distance = math.sqrt(
        #             math.pow((vertices[i][0] - vertices[j][0]), 2)
        #             + math.pow((vertices[i][1] - vertices[j][1]), 2)
        #         )
        #         edge_distance[(vertices[i], vertices[j])] = distance
        return edge_distance


test = {(5, 0): (5, 9), (15, 6): (1, 3), (6, 8): (6, 6), (5, 5): (0, 7)}
a = collect_trash()
output = a.setting((15, 6), test)
print(output)
