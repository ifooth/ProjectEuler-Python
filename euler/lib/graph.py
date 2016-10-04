# -*- coding: utf-8 -*-
# Copyright 2016 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""图算法实现
http://www.cnblogs.com/yupeng/p/3414569.html
https://www.python.org/doc/essays/graphs/
图分类
============
有向图，无向图
加权图，无权图
有环图，无换图
简单图，非简单图
嵌入图和拓扑图
隐式图，显示图
有标号图，无标号图

数据结构
=======
字典，列表

基本算法
========
"""
import itertools


def bfs(graph, start):
    """
    宽度优先搜索
    breadth-first search
    """
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def find_path(graph, start, end, path=[]):
    """查找路径
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return []


def find_all_paths(graph, start, end, path=[]):
    """查找所有路径
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    """查找最短路径
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    shortest = []
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_farthest_path(graph, start, end, path=[]):
    """查找最远路径
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    farthest = []
    for node in graph[start]:
        if node not in path:
            newpath = find_farthest_path(graph, node, end, path)
            if newpath:
                if not farthest or len(newpath) > len(farthest):
                    farthest = newpath
    return farthest


def find_ring_path(graph, start, path=[]):
    """查找最长环路径
    """
    path = path + [start]

    if len(path) >= 2 and path[-1] == start:
        return path
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            print 'ring', node, path
            newpaths = find_ring_path(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def is_connect(graph, nodes):
    for start, end in itertools.combinations(nodes, 2):
        if start not in graph[end]:
            return False
    return True
