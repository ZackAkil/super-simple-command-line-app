import argparse
parser = argparse.ArgumentParser(description="Nice little CL app!")
parser.add_argument("name", help="Just your name, nothing special")

parser.add_argument("-p", "--profession", help="Your nobel profession")

parser.add_argument("-c", "--cool", action="store_true", help="Add a little cool")

args = parser.parse_args()
print("Your name is what? " + args.name)

cool_addition = " and dragon tamer" if args.cool else ""

if args.profession:
    print("What is your profession!? a " + args.profession + cool_addition)
