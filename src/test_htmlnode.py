import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

 def test_props_to_html(self):
        tag = "p"
        value = "hello world"
        children = None
        props = {
                "href": "https://www.google.com", 
                "target": "_blank",
                }
        
        testnode = HTMLNode(tag,value,children,props)

        test_html = testnode.props_to_html()

        self.assertEqual(test_html,  'href="https://www.google.com" target="_blank"')

        test_html = HTMLNode().props_to_html() #Make sure there is not an error if props is empty
 def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()