import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        htmlNode = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        test_props_string = htmlNode.props_to_html()
        self.assertEqual(
            'href="https://www.google.com" target="_blank"', test_props_string
        )

    def test_props_none(self):
        htmlNode = HTMLNode()
        test_props_string = htmlNode.props_to_html()
        self.assertEqual("", test_props_string)

    def test_repr(self):
        htmlNode = HTMLNode(
            tag="<p>",
            props={
                "class": "btn-primary",
            },
        )
        test_props_string = "HTMLNode(<p>, None, None, {'class': 'btn-primary'})"
        self.assertEqual(test_props_string, htmlNode.__repr__())


if __name__ == "__main__":
    unittest.main()
