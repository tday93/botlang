
    def test(self, stringIn):
        print(stringIn)
        if len(self.children) == 0:
            if stringIn in self.pattern:
                return True
            else:
                return False
        else:
            f_lists = self.funcy_list()
            print(f_lists)
            for f_list in f_lists:
                for item in f_list:
                    if type(item) == str:
                        if item == stringIn:
                            return True
                        if stringIn.startswith(item):
                            print(item)
                            stringIn = stringIn.split(item, 1)[1]
                    else:
                        new_string = self.child_test(item, stringIn)
                        print("New String = {}".format(new_string))
                        if new_string == False:
                            return False
                        if len(new_string) == len(stringIn):
                            return stringIn
                        stringIn = stringIn.split(new_string,1)[1]
            

    def child_test(self, item, stringIn):
        i = 1 
        for i in range(len(stringIn)):
            if item.test(stringIn[0:i]):
                s = stringIn[0:i]
                return s
        return False

    def funcy_list(self):
        print(self.pattern)
        funcy_lists = []
        for pattern in self.pattern:
            work_list = []
            for item in pattern:
                if self.sub_pattern_check([item]):
                    work_list.append(self.children[self.get_base_name(item)])
                else: 
                    work_list.append(item)
                stripped_list = [item for item in work_list if item != ""]
            funcy_lists.append(stripped_list)
        return funcy_lists
