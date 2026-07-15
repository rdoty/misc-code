import unittest
from collections import deque

def dfs_graph_path(graph:dict, start:str, target:str, visited=None):
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


def bfs_graph_path(graph:dict, start:str, target:str):
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
        self.test_functions = [dfs_graph_path, bfs_graph_path]
        self.test_graph = {  # graph with two ways to get to 'D'
            'A': ['B', 'C'],
            'B': ['E'],
            'C': ['D'],
            'D': [],
            'E': ['D']
        }
        self.test_data_list = [
            {'start_node': 'A', 'target_node': 'C', 'expected': ['A', 'C']},
            {'start_node': 'A', 'target_node': 'E', 'expected': ['A', 'B', 'E']},
            {'start_node': 'B', 'target_node': 'C', 'expected': None},
            {'start_node': 'E', 'target_node': 'A', 'expected': None},
        ]

    def test_graph_searches(self):
        for def_name in self.test_functions:
            print(f"\nTesting {def_name.__name__}():")
            for count, test_data in enumerate(self.test_data_list):
                self.assertEqual(
                    def_name(self.test_graph, test_data['start_node'], test_data['target_node']),
                    test_data['expected']
                )

        # Since output differs, separately confirm breath-first finds shorter path
        self.assertEqual(dfs_graph_path(self.test_graph, 'A', 'D'), ['A', 'B', 'E', 'D'])
        self.assertEqual(bfs_graph_path(self.test_graph, 'A', 'D'), ['A', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
