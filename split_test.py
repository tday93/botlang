import re
pattern = ["#greeting#", ", ", "#place#", "!"]
stringIn = "Hello, World!"


def pattern_split(stringIn, pattern):
    wrapped_pat = [re.escape(pat) for pat in pattern]
    re_pat = re.compile("{}".format("|".join(wrapped_pat)))
    list_out = re_pat.split(stringIn)[:-1]
    return list_out

if __name__ == "__main__":

   print(pattern_split(stringIn, pattern))
