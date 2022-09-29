# se-hw2-fall22

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7113804.svg)](https://doi.org/10.5281/zenodo.7113804)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
![Build](https://github.com/ekanshsinghal/se-hw2-fall22/actions/workflows/build.yml/badge.svg)
![Test](https://github.com/ekanshsinghal/se-hw2-fall22/actions/workflows/test.yml/badge.svg)
[![Code Coverage](https://img.shields.io/badge/Code%20Coverage-95%25-brightgreen)](https://github.com/ekanshsinghal/se-hw2-fall22/blob/main/coverage_report.txt)
[![codecov](https://codecov.io/gh/ekanshsinghal/se-hw2-fall22/branch/main/graph/badge.svg?token=9awZ8cDbJ7)](https://codecov.io/gh/ekanshsinghal/se-hw2-fall22)

## About the project

This project is python implementation of a lua script. It contains the following classes:
1. Num.py
2. Sym.py
3. Cols.py
4. Row.py
5. Data.py

## Installation
This project requires:
 - Python 3.6 or greater
 - pip (or) pip3
 
 To install the packages used by this project, run ```pip install -r requirements.txt``` in the command line. Alternatively, you could run ```pip install .``` in the command line. You may need to use pip3 depending on how it has been set up in your system.
 
## Code Coverage report

```
Name               Stmts   Miss  Cover
--------------------------------------
code/Cols.py          23      3    87%
code/Data.py          47      1    98%
code/Func.py          65      2    97%
code/Num.py           46      0   100%
code/Row.py           12      4    67%
code/Sym.py           25      0   100%
code/__init__.py       0      0   100%
code/main.py          15      0   100%
data/help.py           3      0   100%
test/TestCode.py     118      7    94%
test/__init__.py       0      0   100%
--------------------------------------
TOTAL                354     17    95%

Code coverage = 95%
```

## Testing
Run ```python -m code.main -e all``` in the command line to run the tests under the test folder.

## Test results
```
------------------------------------------------
{7 86 94 106 107 134 190 197 248 292 362 404 430 472 478 512 516 553 610 614 640 657 694 711 723 732 750 834 869 873 948 959}
!!!!!! PASS bignum True

------------------------------------------------
{Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
{8 304 193 4732 18.5 70 1 10}
{8 360 215 4615 14 70 1 10}
{8 307 200 4376 15 70 1 10}
{8 318 210 4382 13.5 70 1 10}
{8 429 208 4633 11 72 1 10}
{8 400 150 4997 14 73 1 10}
{8 350 180 3664 11 73 1 10}
{8 383 180 4955 11.5 71 1 10}
{8 350 160 4456 13.5 72 1 10}
!!!!!! PASS csv True

------------------------------------------------
{:at 4 :hi 5140 :isSorted False :lo 1613 :n 398 :name Lbs- :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512 :seed 10019} :w -1}
{:at 5 :hi 24.8 :isSorted False :lo 8 :n 398 :name Acc+ :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512 :seed 10019} :w 1}
{:at 8 :hi 50 :isSorted False :lo 10 :n 398 :name Mpg+ :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512 :seed 10019} :w 1}
!!!!!! PASS data True

------------------------------------------------
!!!!!! PASS list True

------------------------------------------------

Examples: 
python -m code.main -e <test_name>

List of available test names : 
	 all
	 bad
	 bignum
	 csv
	 data
	 list
	 ls
	 num
	 stats
	 sym
	 the
!!!!!! PASS ls True

------------------------------------------------
!!!!!! PASS num True

------------------------------------------------
xmid {:Clndrs 4 :Model 76 :Volume 146 :origin 73}
xdiv {:Clndrs 1.5503875968992247 :Model 3.875968992248062 :Volume 100.7751937984496 :origin 3.6906936271109134}
ymid {:Acc+ 15 :Lbs- 2800 :Mpg+ 20}
ydiv {:Acc+ 2.7131782945736433 :Lbs- 887.2093023255813 :Mpg+ 7.751937984496124}
!!!!!! PASS stats True

------------------------------------------------
{:div 1.378 :mid a}
!!!!!! PASS sym True

------------------------------------------------
{:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512 :seed 10019}
!!!!!! PASS the True
!!!!!! PASS all True
# Failures 0
```
 
## Directory structure
    .
    |   .coverage
    |   .gitignore
    |   CITATION.cff
    |   CODE-OF-CONDUCT.md
    |   CONTRIBUTING.md
    |   coverage.svg
    |   coverage_report.txt
    |   directory_tree.txt
    |   LICENSE
    |   README.md
    |   requirements.txt
    |   
    +---.github
    |   \---workflows
    |           build.yml
    |           test.yml
    |           
    +---code
    |   |   Cols.py
    |   |   csv_reader.py
    |   |   Data.py
    |   |   Func.py
    |   |   main.py
    |   |   Num.py
    |   |   Row.py
    |   |   Sym.py
    |   |   __init__.py
    |   |
    +---data
    |   |   help.py
    |   |   hw2-csv.csv
    |   |         
    +---docs
    |   |   code.rst
    |   |   conf.py
    |   |   index.rst
    |   |   Makefile
    |   |   modules.rst
    |   |   
    |   \---_build
    |       +---doctrees
    |       |       code.doctree
    |       |       environment.pickle
    |       |       index.doctree
    |       |       modules.doctree
    |       |       
    |       \---html
    |           |   .buildinfo
    |           |   code.html
    |           |   genindex.html
    |           |   index.html
    |           |   modules.html
    |           |   objects.inv
    |           |   py-modindex.html
    |           |   search.html
    |           |   searchindex.js
    |           |   
    |           +---_sources
    |           |       code.rst.txt
    |           |       index.rst.txt
    |           |       modules.rst.txt
    |           |       
    |           \---_static
    |                   alabaster.css
    |                   basic.css
    |                   custom.css
    |                   doctools.js
    |                   documentation_options.js
    |                   file.png
    |                   jquery.js
    |                   language_data.js
    |                   minus.png
    |                   plus.png
    |                   pygments.css
    |                   searchtools.js
    |                   underscore.js
    |                   
    \---test
        |   TestCode.py
        |   __init__.py


## Contributing to this project
Read the Contributing.md to find out how you can help contribute to this project.




