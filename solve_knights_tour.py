from chess import Board, Knight
from knight_tour import solveOnce, searchForSolutions
import argparse

print('''
██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗██╗░██████╗  ████████╗░█████╗░██╗░░░██╗██████╗░
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝╚█║██╔════╝  ╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░░╚╝╚█████╗░  ░░░██║░░░██║░░██║██║░░░██║██████╔╝
██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░░░░░╚═══██╗  ░░░██║░░░██║░░██║██║░░░██║██╔══██╗
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░░░░██████╔╝  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝
''')

parser = argparse.ArgumentParser("Knight Tour Solver (Brute Force)")

parser.add_argument('x_position', metavar='x', type=int, nargs='+',
                    help='X Initial position of Knight')
parser.add_argument('y_position', metavar='y', type=int, nargs='+',
                    help='Y Initial position of Knight')

parser.add_argument('x_size', metavar='x', type=int, nargs='+',
                    help='X Chess board size')

parser.add_argument('y_size', metavar='y', type=int, nargs='+',
                    help='Y Chess board size')
parser.add_argument('-s', "--save", help='save solution as PNG file', action="store_true")
parser.add_argument('-sh', "--show", help='show solution when found', action="store_true")
parser.add_argument('-d', "--directory",
                    help='where the chess board image will be stored [default: same directory of script]')
parser.add_argument('-m', "--multiple", help='work out all solution  [gonna take a lot of time]', action='store_true')
args = parser.parse_args()

board = Board(args.x_size[0], args.y_size[0])
board.SAVE = args.save
board.GRAPHICS = args.show
if not args.directory:
    args.directory = ""
save_to = args.directory.strip('"')
board.SAVE_SOLUTION_DICT = save_to

knight = Knight(board, args.x_position[0], args.y_position[0])
print("Board Size: ", args.x_size[0], "x", args.y_size[0])
if args.multiple:
    print("Running....")
    print("Control + C to quit")
    searchForSolutions(args.x_size[0], args.y_size[0], args.save, args.show, save_to)
else:
    print("Knight Position: ", "(", args.x_position[0], ",", args.y_position[0], ")")
    print("Running....")
    solveOnce(board, knight)
