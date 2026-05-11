from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_nodes = []
        self.current_tag = None
        self.has_i18n = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attr_dict = dict(attrs)
        self.has_i18n = 'data-i18n' in attr_dict
        
    def handle_endtag(self, tag):
        self.current_tag = None
        self.has_i18n = False
        
    def handle_data(self, data):
        text = data.strip()
        if text and len(text) > 1 and not self.has_i18n and self.current_tag not in ['script', 'style']:
            self.text_nodes.append(text)

parser = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

unique_texts = list(dict.fromkeys(parser.text_nodes))
with open('untranslated.txt', 'w', encoding='utf-8') as f:
    for t in unique_texts:
        if '{' not in t and '}' not in t:
            f.write(t + '\n')
