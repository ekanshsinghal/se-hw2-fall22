# se-hw2-fall22

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7113804.svg)](https://doi.org/10.5281/zenodo.7113804)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
![Build](https://github.com/ekanshsinghal/se-hw2-fall22/actions/workflows/build.yml/badge.svg?maxAge=10000)
![Test](https://github.com/ekanshsinghal/se-hw2-fall22/actions/workflows/test.yml/badge.svg?maxAge=10000)
![Python](https://img.shields.io/badge/python-v3.8+-yellow.svg)
[![GitHub Release](https://img.shields.io/github/release/ekanshsinghal/se-hw2-fall22)](https://github.com/ekanshsinghal/se-hw2-fall22/releases/)
![GitHub issues](https://img.shields.io/github/issues/ekanshsinghal/se-hw2-fall22)
![Repo Size](https://img.shields.io/github/repo-size/ekanshsinghal/se-hw2-fall22?color=brightgreen)
[![codecov](https://codecov.io/gh/ekanshsinghal/se-hw2-fall22/branch/main/graph/badge.svg?token=9awZ8cDbJ7&maxAge=10000)](https://codecov.io/gh/ekanshsinghal/se-hw2-fall22)


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
 

## Demo Video 
https://user-images.githubusercontent.com/30636208/193187254-7ed8de42-cda7-42af-934f-4045b585bb16.mp4


## Code Coverage report

```
Name               Stmts   Miss  Cover
--------------------------------------
code/Cols.py          20      1    95%
code/Data.py          46      1    98%
code/Func.py          63      2    97%
code/Num.py           46      0   100%
code/Row.py            6      0   100%
code/Sym.py           25      0   100%
code/__init__.py       0      0   100%
code/main.py          15      0   100%
data/help.py           3      0   100%
test/TestCode.py     108      7    94%
test/__init__.py       0      0   100%
--------------------------------------
TOTAL                332     11    97%

Code coverage = 97%
```

## Testing
Run ```python -m code.main -e all``` in the command line to run the tests under the test folder.

## Test results
```
------------------------------------------------
Invalid field
!!!!!! FAIL bad True

------------------------------------------------
{8 47 94 117 163 201 238 260 318 319 359 381 386 425 452 559 561 562 595 614 617 634 675 763 771 838 856 863 881 898 908 944}
!!!!!! PASS bignum True

------------------------------------------------
{Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
{8.0 304.0 193.0 4732.0 18.5 70.0 1.0 10.0}
{8.0 360.0 215.0 4615.0 14.0 70.0 1.0 10.0}
{8.0 307.0 200.0 4376.0 15.0 70.0 1.0 10.0}
{8.0 318.0 210.0 4382.0 13.5 70.0 1.0 10.0}
{8.0 429.0 208.0 4633.0 11.0 72.0 1.0 10.0}
{8.0 400.0 150.0 4997.0 14.0 73.0 1.0 10.0}
{8.0 350.0 180.0 3664.0 11.0 73.0 1.0 10.0}
{8.0 383.0 180.0 4955.0 11.5 71.0 1.0 10.0}
{8.0 350.0 160.0 4456.0 13.5 72.0 1.0 10.0}
!!!!!! PASS csv True

------------------------------------------------
{:at 3 :hi 5140.0 :isSorted False :lo 1613.0 :n 398 :name Lbs- :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512.0 :seed 10019.0} :w -1}
{:at 4 :hi 24.8 :isSorted False :lo 8.0 :n 398 :name Acc+ :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512.0 :seed 10019.0} :w 1}
{:at 7 :hi 50.0 :isSorted False :lo 10.0 :n 398 :name Mpg+ :the {:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512.0 :seed 10019.0} :w 1}
!!!!!! PASS data True

------------------------------------------------
!!!!!! FAIL list True

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
xmid {:Clndrs 4.0 :Model 76.0 :Volume 151.0 :origin 1.0}
xdiv {:Clndrs 1.55 :Model 3.88 :Volume 100.78 :origin 1.33}
ymid {:Acc+ 15.5 :Lbs- 2807.0 :Mpg+ 20.0}
ydiv {:Acc+ 2.713 :Lbs- 886.822 :Mpg+ 7.752}
!!!!!! PASS stats True

------------------------------------------------
{:div 1.378 :mid a}
!!!!!! PASS sym True

------------------------------------------------
{:Seperator , :dump False :eg all :file ../data/auto93.csv :help False :nums 512.0 :seed 10019.0}
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




