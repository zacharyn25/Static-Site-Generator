#TextNode Class

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        # self.text - The text content of the node
        # self.text_type - The type of text this node contains, which is just a string like "bold" or "italic"
        # self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'