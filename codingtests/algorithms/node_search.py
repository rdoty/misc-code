import unittest
from collections import deque

def dfs_graph_path(graph:dict, start:char, target:char, visited=None):
    """
    Use Depth-First Search (Recursive) to find path from start to target.
    Return path as a list of nodes, or None.
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    if start == target:
        return [start]
        
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_graph_path(graph, neighbor, target, visited)
            if path is not None:
                return [start] + path
                
    return None


def bfs_graph_path(graph:dict, start:char, target:char):
    """
    Use Breadth-First Search (Iterative) to find shortest path from start to target
    Return path as a list of nodes, or None.
    """
    if start == target:
        return [start]

    queue = deque([(start, [start])])  # Tuples of (current_node, path_taken_to_reach_it)
    visited = {start}
    
    while queue:
        current, path = queue.popleft()        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == target:
                    return new_path
                visited.add(neighbor)
                queue.append((neighbor, new_path))
                
    return None


class TestGraphSearches(unittest.TestCase):
    def setUp(self):
        self.graph = {  # graph with two ways to get to 'D'
            'A': ['B', 'C'],
            'B': ['F'],
            'C': ['D'],
            'F': ['D'],
            'D': []
        }

    def test_dfs_path_found(self):
        self.assertEqual(dfs_graph_path(self.graph, 'A', 'C'), ['A', 'C'])
        self.assertEqual(dfs_graph_path(self.graph, 'A', 'D'), ['A', 'B', 'F', 'D'])
        self.assertEqual(dfs_graph_path(self.graph, 'A', 'F'), ['A', 'B', 'F'])

    def test_dfs_no_path(self):
        self.assertIsNone(dfs_graph_path(self.graph, 'B', 'C'))

    def test_bfs_path_found(self):
        self.assertEqual(bfs_graph_path(self.graph, 'A', 'C'), ['A', 'C'])
        self.assertEqual(bfs_graph_path(self.graph, 'A', 'D'), ['A', 'C', 'D'])
        self.assertEqual(bfs_graph_path(self.graph, 'A', 'F'), ['A', 'B', 'F'])

    def test_bfs_no_path(self):
        self.assertIsNone(bfs_graph_path(self.graph, 'E', 'A'))

    def test_bfs_shortest_path(self):
        # Should find shorter route A -> C -> D
        # instead of A -> B -> F -> D (length 4)
        self.assertEqual(bfs_graph_path(self.graph, 'A', 'D'), ['A', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
