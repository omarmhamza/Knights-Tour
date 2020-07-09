# Knights-Tour
There are mainly 4 ways of solving the knight's tour problem:
 - Brute force algorithm 
 - Divide and conquer 
 - Warnsdorff's rule
 - Using Neural Networks 
 
 The code in this repo solves the Knight's tour problem using backtracking/brute forcing with a graphical representation of the result as shown below.
 

<a href="https://github.com/omarmhamza/Knights-Tour/blob/master/Knight%20Tour%20Solutions/"><img src="https://github.com/omarmhamza/Knights-Tour/blob/master/Knight%20Tour%20Solutions/plot_8x8.png" width = 40% title="Knight's Tour Solution 5 x 5" alt="Knight's Tour Solution 5 x 5"></a>


## Requirements 
Python 3


## Installation 

```console
foo@bar:~$ git clone https://github.com/omarmhamza/Knights-Tour.git
foo@bar:/Knights-Tour$ pip install -r requirements.txt
```

## Getting Started

```console
#Solves Knight's tour for 8 x 8 board placing the Knight at the first coordinates (0,0) and shows the result graphically 
foo@bar:/Knights-Tour$ python solve_knights_tour.py 0 0 8 8 -sh 
```

## Arguments 

```console
foo@bar:/Knights-Tour$ python solve_knights_tour.py -h
```

```shell

██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ████████╗░█████╗░██╗░░░██╗██████╗░
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ░░░██║░░░██║░░██║██║░░░██║██████╔╝
██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ░░░██║░░░██║░░██║██║░░░██║██╔══██╗
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝

usage: Knight Tour Solver (Brute Force) [-h] [-s] [-sh] [-d DIRECTORY] [-m]
                                        x [x ...] y [y ...] x [x ...] y
                                        [y ...]

positional arguments:
  x                     X Initial position of Knight
  y                     Y Initial position of Knight
  x                     X Chess board size
  y                     Y Chess board size

optional arguments:
  -h, --help            show this help message and exit
  -s, --save            save solution as PNG file
  -sh, --show           show solution when found
  -d DIRECTORY, --directory DIRECTORY
                        where the chess board image will be stored [default:
                        same directory of script]
  -m, --multiple        work out all solution [gonna take a lot of time]

```
## Usage

### Saving and Showing Solution 

```console
# Knight @ 0,0 and Board of size 5 x 5
foo@bar:/Knights-Tour$ python solve_knights_tour.py  0 0 5 5 -s -sh 

██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ████████╗░█████╗░██╗░░░██╗██████╗░
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ░░░██║░░░██║░░██║██║░░░██║██████╔╝
██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ░░░██║░░░██║░░██║██║░░░██║██╔══██╗
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝

Board Size:  5 x 5
Knight Position:  ( 0 , 0 )
Running....
Found solution
Time took:  0.08 second(s)
[[ 1  6 15 10 21]
 [14  9 20  5 16]
 [19  2  7 22 11]
 [ 8 13 24 17  4]
 [25 18  3 12 23]]

```

<a href="https://github.com/omarmhamza/Knights-Tour/blob/master/Knight%20Tour%20Solutions/"><img src="https://github.com/omarmhamza/Knights-Tour/blob/master/Knight%20Tour%20Solutions/figure_output_example.png" width = 40% title="Knight's Tour Solution 5 x 5" alt="Knight's Tour Solution 5 x 5"></a>

### Saving to specific directory 
```console
foo@bar:/Knights-Tour$ python solve_knights_tour.py  0 0 8 8 -s -d "/Desktop/User"
or
foo@bar:/Knights-Tour$ python solve_knights_tour.py  0 0 8 8 -s -d /Desktop/User
```

## Search for all solutions for a specific board size

```console
#Board size is 8 x 8 
foo@bar:/Knights-Tour$ python solve_knights_tour.py 0 0 8 8 -m 

Board Size:  8 x 8
Running....
Control + C to quit
Setting knight at  (0, 0)
Found solution
Time took:  77.24 second(s)
[[ 1 60 39 34 31 18  9 64]
 [38 35 32 61 10 63 30 17]
 [59  2 37 40 33 28 19  8]
 [36 49 42 27 62 11 16 29]
 [43 58  3 50 41 24  7 20]
 [48 51 46 55 26 21 12 15]
 [57 44 53  4 23 14 25  6]
 [52 47 56 45 54  5 22 13]]
Setting knight at  (0, 1)
....

```


## Search for all solutions and save results 


```console
foo@bar:/Knights-Tour$ python solve_knights_tour.py 0 0 8 8 -m -s -d /Desktop/Solutions 
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://choosealicense.com/licenses/mit/)
