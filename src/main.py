from textnode import TextNode, TextType

def main():
    object = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    print(object)


main()