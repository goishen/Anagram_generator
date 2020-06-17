import sys

def load(file):

    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
#            for word in loaded_txt:
#                if len(word) > 1 and word == word[::-1]:
#                    print(word, word[::-1])
            return loaded_txt
    except IOError as e:
        print(f"{IOError}\nError opening {file}.\n", file=sys.stderr)
        sys.exit(1)

