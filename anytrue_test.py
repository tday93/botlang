list_1 = ["A", "B", "C", "D", "E", "F"]
list_2 = ["1", "22", "3", "4", "5", "6"]

test_list = [["A", "6"],
["1", "D"],
["1", "1"],
["Q", "1"],
["w", "w"],
["C","F"]]

def anytrue(check_list1, check_list2, test_list):
   return all(item in check_list1 or item in check_list2 for item in test_list)

if __name__ == "__main__":
   for list in test_list:
      print(anytrue(list_1, list_2, list))
