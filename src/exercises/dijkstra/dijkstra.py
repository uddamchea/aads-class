#!/usr/bin/env python3
"""Dijkstra's algorithm usage"""


from pythonds3.graphs import Graph
import toml, heapq


def read_toml(filename: str) -> Graph:
    """Read TOML config file"""
    file = toml.load(filename)
    data = dict()
    graph = Graph()

    for i in file['routers']:
        data[i['address']] = i['name']
    
    for j in file['routers']:
        for k in j['neighbors']: graph.add_edge(j['name'], data[k['address']], k['cost'])

    return graph

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""

    # dijkstra from pythonds3
    # start.distance = 0
    # not_yet_visited = [[start.distance, start]]
    # heapq.heapify(not_yet_visited)
    # while not_yet_visited:
    #     current_vertex = heapq.heappop(not_yet_visited)[1]
    #     for next_vertex in current_vertex.get_neighbors():
    #         new_distance = current_vertex.distance + current_vertex.get_neighbor(
    #             next_vertex
    #         )
    #         if new_distance < next_vertex.distance:
    #             next_vertex.distance = new_distance
    #             next_vertex.previous = current_vertex
    #             found = False
    #             for vertex in not_yet_visited:
    #                 if vertex[1].key == next_vertex.key:
    #                     vertex[0] = next_vertex.distance
    #                     heapq.heapify(not_yet_visited)
    #                     found = True
    #             if not found:
    #                 heapq.heappush(
    #                     not_yet_visited, [next_vertex.distance, next_vertex]
    #                 )

    getVertex = g.get_vertex(start)
    g.dijkstra(getVertex)

def main():
    graph = read_toml("data/exercises/dijkstra/network.toml")
    find_path(graph, 'v')
    # pass


if __name__ == "__main__":
    main()
