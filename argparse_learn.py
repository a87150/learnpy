import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
if args.verbosity:
  print(args)
print(args.echo)