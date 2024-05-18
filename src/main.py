import cmd
from pathlib import Path

import ceasar


class Cmd(cmd.Cmd):
    prompt = '# '
    def do_ceasar(self, args):
        """ceasar [fname] [offset]
applies ceasar cipher to a file of the given offset"""
        print(args)
        args = args.rsplit(' ',2)
        if len(args) < 3:
            print("Error: not enough arguments to ceasar;")
            return
        try:
            offset = int(args[2])
        except:
            print("Error: surely wrong integer value: '%s'"%args[1])
        p = Path(args[0])
        dest = Path(args[1])
        if not p.exists():
            print("path", p, "does not exist")
        with open(dest, "w") as fw:
            with open(p) as fr:
                for ln in fr:
                    print(fw.write(
                        ceasar.ceasar(
                            ln,
                            offset
                        )
                    ))
    def do_unceasar(self, args):
        try:
            p, d = args.split(" ", 1)
        except:
            print("wrong arguments")
            return
        open(d, "w", encoding='utf-8').write(
            ceasar.unceasar(open(p, encoding="utf-8").read())
        )
if __name__ == "__main__":
    Cmd().cmdloop()