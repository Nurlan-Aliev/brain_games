### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nurlan-Aliev/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Nurlan-Aliev/python-project-lvl1/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/e1183cfd34e2bf005cfe/maintainability)](https://codeclimate.com/github/Nurlan-Aliev/python-project-lvl1/maintainability)


# Welcome to the Brain Games!

## Example of starting a game with a player's victory
[![asciicast](https://asciinema.org/a/fxdk4s1c7cbKP76PAFs16xy6G.svg)](https://asciinema.org/a/fxdk4s1c7cbKP76PAFs16xy6G)

## An example of starting a game with a player defeat

[![asciicast](https://asciinema.org/a/33dANygrwijV0FJJrldLRID1H.svg)](https://asciinema.org/a/33dANygrwijV0FJJrldLRID1H)


## Instruction

|     |       Games       |                          Description                          |
|:----|:-----------------:|:-------------------------------------------------------------:|
| 1   |    brain-even     |  Answer "yes" if the number is even, otherwise answer "no".   |
| 2   |    brain-calc     |             What is the result of the expression?             |
| 3   |     brain-gcd     |      Find the greatest common divisor of given numbers.       |
| 4   |    brain-prime    | Answer "yes" if given number is prime. Otherwise answer "no". |
| 5   | brain-progression |          What number is missing in the progression?           |

## Installation
Clone the repository and install manually.
```commandline
$ git clone https://github.com/Nurlan-Aliev/python-project-lvl1.git
$ cd python-project-lvl1
```

#### Install using poetry
```commandline
$ poetry build
$ python3 -m pip install --user dist/*.whl
```

#### Install using pip
```
python3 -m build
python3 -m pip install --user dist/*.whl
```

## Start Game

To start, enter the name of the game.
```commandline
$ brain-even
$ brain-calc
$ brain-gcd
$ brain-prime
$ brain-progression
```
