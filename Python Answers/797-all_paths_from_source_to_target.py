from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    myqueue = [[0]]
    target = len(graph) - 1
    ans = []
    # using DFS to loop this graph
    while myqueue:
        curr = myqueue.pop(0)
        if curr[-1] == target:
            ans.append(curr)
        else:
            for children in graph[curr[-1]]:
                myqueue.append(curr + [children])
    return ans
    