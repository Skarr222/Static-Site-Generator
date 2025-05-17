from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Cannot convert to HTML because 'tag' is missing.")
        if self.children is None:
            raise ValueError("Cannot convert to HTML because 'children' is missing.")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"
