import unittest
from who_follows_you_back import DirectedGraph


class DirectedGraphTest(unittest.TestCase):

    def setUp(self):
        self.my_graph = DirectedGraph()

    def test_add_edge(self):
        self.my_graph.add_edge("A", "B")
        self.assertEqual(self.my_graph.graph, {"A": ["B"]})

    def test_add_edges_more_than_one(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.assertEqual(self.my_graph.graph, {"A": ["B", "C"]})

    def test_get_neighbours_for(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.assertEqual(self.my_graph.get_neighbours_for("A"), ["B", "C"])

    def test_path_between_direct_path(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.assertTrue(self.my_graph.path_between("A", "C"))

    def test_path_between_there_is_no_path(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.my_graph.add_edge("B", "E")
        self.assertFalse(self.my_graph.path_between("A", "D"))

    def test_path_between_not_direct_path(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "D")
        self.my_graph.add_edge("B", "C")
        self.assertTrue(self.my_graph.path_between("A", "C"))

    def test_path_between_with_a_cycle(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.my_graph.add_edge("B", "A")
        self.my_graph.add_edge("C", "B")
        self.my_graph.add_edge("C", "D")
        self.assertTrue(self.my_graph.path_between("A", "D"))

    def test_path_between_with_not_existing_node(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.assertFalse(self.my_graph.path_between("D", "E"))

    def test__str__(self):
        self.my_graph.add_edge("A", "B")
        self.my_graph.add_edge("A", "C")
        self.my_graph.add_edge("B", "A")
        self.my_graph.add_edge("C", "B")
        self.my_graph.add_edge("C", "D")
        self.my_graph.__str__()


if __name__ == '__main__':
    unittest.main()
