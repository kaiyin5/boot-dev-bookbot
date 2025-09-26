# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! Bookbot is a python script which takes text file and generate a report with data: word count and character count, in the terminal. 

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

## Prerequisites

* Python 3.10+ installed (see the [project page](https://www.boot.dev/lessons/6120f97b-117f-4a84-94d6-a3436f21f1a4) for help if you don't already have it)
* Access to a unix-like shell (e.g. zsh or bash)

## How to clone and run it

```
# clone the project
git clone https://github.com/kaiyin5/bookbot.git
cd bookbot
# run the script with path of text file argument
python3 main.py <path_to_book>
```
