### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nurlan-Aliev/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Nurlan-Aliev/python-project-lvl1/actions)

<a href="https://codeclimate.com/github/Nurlan-Aliev/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/f787b300615a3ec8be61/maintainability" /></a>


[![asciicast](https://asciinema.org/a/Vf3pirDl9ZBjQWhkV5jxMaEYO.svg)](https://asciinema.org/a/Vf3pirDl9ZBjQWhkV5jxMaEYO)

# Welcome to the Brain Games!

## Instruction

|     |       Games       |                          Description                          |
|:----|:-----------------:|:-------------------------------------------------------------:|
| 1   |    brain-even     |  Answer "yes" if the number is even, otherwise answer "no".   |
| 2   |    brain-calc     |             What is the result of the expression?             |
| 3   |     brain-gcd     |      Find the greatest common divisor of given numbers.       |
| 4   |    brain-prime    | Answer "yes" if given number is prime. Otherwise answer "no". |
| 5   | brain-progression |          What number is missing in the progression?           |

## Installation
Clone the repository and install manually
```commandline
$ git clone https://github.com/Nurlan-Aliev/python-project-lvl1.git
$ cd python-project-lvl1
```

#### install using poetry
```commandline
$ poetry build
$ python3 -m pip install --user dist/*.whl
```

#### install using pip
```
python3 -m build
python3 -m pip install --user dist/*.whl
```

## Start Game

To start, enter the name of the game
```commandline
$ brain-even
$ brain-calc
$ brain-gcd
$ brain-prime
$ brain-progression
```
