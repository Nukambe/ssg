import functools
from typing import List, Dict
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], props: Dict[str, str]= None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A ParentNode must have a tag!")
        if not self.children:
            raise ValueError("A ParentNode must have children!")
        return f"<{self.tag}{self.props_to_html()}>{functools.reduce(lambda acc, node: acc + node.to_html(), self.children, "")}</{self.tag}>"
