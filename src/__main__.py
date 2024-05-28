from pathlib import Path
from argparse import ArgumentParser
import ceasar


def ExixtingPath(url):
    path = Path(url)
    assert path.exists(), f"path '{path!r}' does not exist"
    return path


parser = ArgumentParser(
    prog='ceasar',
    description='A little program to cipher and uncipher ceasar cipher',
)

parser.add_argument(
    'infile',
    type=ExixtingPath,
    help='The input file to read text from',
)
parser.add_argument(
    'outfile',
    type=Path,
    help='The file to write output to',
)

parser.add_argument(
    '-ceasar --c',
    dest='ceasar',
    type=int,
    default=3
)

parser.add_argument(
    '-unceasar --u',
    dest='unceasar',
    action='store_true',
)

parser.add_argument(
    '--dictionary -d',
    type=ceasar.Dictionary,
    dest='dictionary',
    help=(
        'The path to a file containing the words to be counted'
        ' seperated by newlines'
    ),
    default=ceasar.Dictionary(
        Path(__file__).resolve().parent / 'dictionary/en.txt',
    ),
)

args = parser.parse_args()


if args.unceasar:
    txt = args.infile.read_text()
    print(args.dictionary)
    un = ceasar.unceasar(txt, args.dictionary)
    args.outfile.write_text(un)
else:
    txt = args.infile.read_text()
    ce = ceasar.ceasar(txt, args.ceasar)
    args.outfile.write_text(ce)
