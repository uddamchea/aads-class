#!/usr/bin/env python3
"""Dijkstra's algorithm usage"""


from pythonds3.graphs import Graph
import toml


def read_toml(filename: str) -> Graph:
    """Read TOML config file"""
    file = toml.load(filename)
    data = dict()
    graph = Graph()
    # n, g =  dict(), Graph()
    for i in file['routers']:
        data[i['address']] = i['name']
    
    for j in file['routers']:
        for k in j['neighbors']: graph.add_edge(j['name'], data[k['address']], k['cost'])
    return graph

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""
    print(g.dijkstra(g.get_vertex(start)))


def main():
    graph = read_toml("data/exercises/dijkstra/network.toml")
    find_path(graph, 'v')


if __name__ == "__main__":
    main()
