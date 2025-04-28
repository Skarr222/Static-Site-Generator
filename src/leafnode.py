from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()

        if self.tag is None:
            return f'"{self.value}"'

        return f"<{self.tag}>{self.value}</{self.tag}>"
