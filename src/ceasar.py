from pathlib import Path
from argparse import ArgumentParser


class Dictionary:
    min_len = 3
    file = None

    def __init__(self, file):
        self.file_path = file

    def __iter__(self):
        self.file = open(self.file_path)
        return self

    def __next__(self):
        try:
            if self.file is not None:
                ln = next(self.file)
            else:
                raise TypeError()
        except StopIteration as e:
            self.file.close()
            self.file = None
            raise StopIteration from e
        else:
            return ln.strip()


def ceasar(txt, offset):
    ret = ""
    for char in txt:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            char = chr(
                (
                    ord(
                        char
                    ) - ord(
                        base
                    ) + offset
                ) % 26 + ord(base)
            )
        ret += char
    return ret


def countWords(txt, dictionnary):
    c = 0
    for word in dictionnary:
        if word.strip() in txt.split(' '):
            c += 1
    return c


def unceasar(txt, dictionnary):
    best = None
    tests = []
    for i in range(26):
        test = ceasar(txt, i)
        count = countWords(test, dictionnary)
        print("  -", i, "counts:", count)
        tests.append((test, count))
    best = [('', 0)]
    for test, count in tests:
        best_count = best[-1][1]
        if best_count < count:
            best = [(test, count)]
            continue
        elif best_count == count:
            best.append((test, count))
    if len(best) != 1:
        choice = None
        num_show = 20
        while choice not in range(len(best)):
            try:
                print('conflicting word counts:')
                for i, val in enumerate(best):
                    print(f'{i:02d}. {val[0][:num_show]!r}')
                choice = input('enter the index of your preffered option: ')
                choice = int(choice)
            except ValueError:
                num_show += 10
                continue
            else:
                text = best[choice][0]
    else:
        text = best[0][0]
    return text


def ExistingPath(url):
    path = Path(url)
    assert path.exists(), f"path '{path!r}' does not exist"
    return path


parser = ArgumentParser(
    prog='ceasar',
    description='A little program to cipher and uncipher ceasar cipher',
)

parser.add_argument(
    'infile',
    type=ExistingPath,
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
    type=Dictionary,
    dest='dictionary',
    help=(
        'The path to a file containing the words to be counted'
        ' seperated by newlines'
    ),
    default=Dictionary(
        Path(__file__).resolve().parent / 'dictionary/en.txt',
    ),
)

args = parser.parse_args()


if args.unceasar:
    txt = args.infile.read_text()
    print(args.dictionary)
    un = unceasar(txt, args.dictionary)
    args.outfile.write_text(un)
else:
    txt = args.infile.read_text()
    ce = ceasar(txt, args.ceasar)
    args.outfile.write_text(ce)
