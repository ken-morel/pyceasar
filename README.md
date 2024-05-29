# pyceasar
python script, executable and setup to easily cipher and uncipher ceasar

## ceasar cipher

Ceasar cipher is a cipher method created during
antic egypt where letters were simply shifted forward or backeard, usally by 3 steps during that time.
Thus `Hello world` may shift by `3` to `Khoor zrupg`

and it is circular so in same conditions `z` maps to `c`.

## usage
```
usage: ceasar [-h] [-ceasar --c CEASAR] [-unceasar --u]
              [--dictionary -d DICTIONARY]
              infile outfile

A little program to cipher and uncipher ceasar cipher

positional arguments:
  infile                The input file to read text from
  outfile               The file to write output to

options:
  -h, --help            show this help message and exit
  -ceasar --c CEASAR
  -unceasar --u
  --dictionary -d DICTIONARY
                        The path to a file containing the
                        words to be counted seperated by
                        newlines
```
