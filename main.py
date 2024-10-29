import random
import argparse


__version__ = "1.0"


parser = argparse.ArgumentParser(prog="ironiser", description=__version__)

parser.add_argument("-f", "--file", type=argparse.FileType("r"), help="Pass in a file.", nargs="?")
parser.add_argument("-s", "--string", help="Pass in a string", nargs="?")
parser.add_argument("-o", "--output", help="Output file", nargs="?")

args = parser.parse_args()


if args.file:
    with args.file as f:
        content = f.read()
elif args.string:
    content = args.string
else:
    content = input("> ")


output = ""
content = content.lower()

for s in content:
    action = random.randint(0, 4096)

    if action % 2 == 0:
        output += s.upper()
    else:
        output += s.lower()

if args.output:
    with open(args.output, "w") as f:
        f.write(content)
        print("ironiser: Saved!\n")

print(output)

