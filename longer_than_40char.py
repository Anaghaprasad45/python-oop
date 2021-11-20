import sys

filenames = sys.argv

for file in filenames:
    for i in open(file):
        if len(i) > 40:
            print(i)
