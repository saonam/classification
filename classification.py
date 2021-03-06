import argparse

from models import classifier

parser = argparse.ArgumentParser("classification.py")
text = parser.add_argument_group("The following arguments are mandatory for text option")
text.add_argument("text", metavar="TEXT", help="text to predict", nargs="?")
file = parser.add_argument_group("The following arguments are mandatory for file option")
file.add_argument("--fin", help="text file input")
args = parser.parse_args()

if not (args.text or args.fin):
    parser.print_help()

if args.text:
    text = args.text
    try:
        predict = classifier(text)[0]
        label = predict.replace("_", " ").capitalize()
        print(label)
    except:
        print("Don't predict label")

if args.fin:
    if not args.fin:
        parser.error("File option requires --fin")
    fin = args.fin
    with open(fin) as f:
        text = f.read()
    try:
        predict = classifier(text)[0]
        label = predict.replace("_", " ").capitalize()
        print(label)
    except:
        print("Don't predict label")
