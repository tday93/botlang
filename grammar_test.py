import re
import random

class Node(object):

    def __init__(self, name, rules, parent = None):
        self.name = name
        self.rules = rules
        self.parent = parent
        self.children = {}
        self.pattern = []
        self.build_pattern()
        self.birth_children()

    def generate(self):
        selected_pattern = random.choice(self.pattern)
        if type(selected_pattern) is str:
            return selected_pattern
        else:
            new_pattern = []
            for item in selected_pattern:
                if self.sub_pattern_check([item]):
                    sub_pattern_name = self.get_base_name(item)
                    new_item = self.children[sub_pattern_name].generate()
                    new_pattern.append(new_item)
                else:
                    new_pattern.append(item)
            new_string = "".join(new_pattern)
            return new_string

    def test(self, stringIn):
        # WORK IN PROGRESS
        if len(self.children) == 0:
            if stringIn in self.pattern:
                return True
            else:
                return False
        else:
            for pattern in self.pattern:
                if pattern in stringIn:
                    split_string = stringIn.split(pattern)
                    
    


    def birth_children(self):
        for item in self.pattern:
            if self.sub_pattern_check(item):
                for element in item:
                    if self.sub_pattern_check([element]):
                        child_name = self.get_base_name(element)
                        if child_name not in self.children:
                            child = Node(child_name, self.rules, self.name)
                            self.children[child_name] = child

    def get_base_name(self, stringIn):
        unwrapped = stringIn[1:-1]
        if "." in unwrapped:
            name = unwrapped.split(".",1)[0]
        else:
            name = unwrapped
        return name


    def build_pattern(self):
        pattern = self.rules[self.name]
        if not self.sub_pattern_check(pattern):
            self.pattern = pattern
            return
        else:
            new_pattern = []
            for item in pattern:
                if self.sub_pattern_check([item]):
                    new_pattern.append(self.reg_split(item))
                else:
                    new_pattern.append(item)
            self.pattern = new_pattern
            return

    def reg_split(self, stringIn):
        pattern = re.compile("(#[^#]+#)")
        split_string = pattern.split(stringIn)
        return split_string
    
    def sub_pattern_check(self, listIn):
        if type(listIn) is not list:
            return False
        pattern = re.compile("#[^#]+#")
        for element in listIn:
            if pattern.search(element) is not None:
                return True
        return False


if __name__ == "__main__":
    rules = {
        "greeting": ["Hello", "Welcome", "Bonjour"],
        "place": ["World", "Universe", "Bar", "Camelot"],
        "sentence": ["#greeting#, #place#!"]
    }
    new_rules = {
        "given_names": ["Bobcat", "Dave", "Francis", "Chelsea", "Stuart", "Louis", "Kriste"],
        "surnames": ["Goldthwait", "Smith", "Truk", "Davis", "Stilinski", "Herbert"],
        "honorifics": ["Mrs.", "Mr.", "Ms.", "Sir", "Dame", "Admiral"],
        "suffixes": ["esq.", "III", "Jr.", "Sr."],
        "simple_name": ["#given_names# #surnames#"],
        "complicated_name" : ["#honorifics# #simple_name# #suffixes#"]
    }
    test_node2 = Node("complicated_name", new_rules)
    test_node = Node("sentence", rules)
    print(test_node.pattern)
    print(test_node.children)
    for k,v in test_node.children.items():
        print(v.pattern)
    print(test_node.generate())
    print(test_node2.generate())
