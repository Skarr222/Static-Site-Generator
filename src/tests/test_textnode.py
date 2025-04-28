import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "test")
        node2 = TextNode("This is a text node", TextType.BOLD, "test")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "test1")
        node2 = TextNode("This is a text node", TextType.BOLD, "test2")
        self.assertNotEqual(node, node2)

    def test_does_url_exists(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(None, node.url)


if __name__ == "__main__":
    unittest.main()
