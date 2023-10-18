### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nurlan-Aliev/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Nurlan-Aliev/python-project-lvl1/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/e1183cfd34e2bf005cfe/maintainability)](https://codeclimate.com/github/Nurlan-Aliev/python-project-lvl1/maintainability)


# Welcome to the Brain Games!

Five math console games.
* brain-even - given a number, your task is to answer whether it is even or not
* brain-calc - an example is given that needs to be solved
* brain-gcd - find the common divisor of two numbers
* brain-prime - given a number, it’s tedious to answer whether the number is prime or not
* brain-progression - tedious find missing number</br>

To win each game you need to answer 3 questions correctly

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

## Docker

This repository contains the Docker image for [Brain Games](https://hub.docker.com/repository/docker/nualiev/brain-games/general).

### Instructions for use

To run a Docker image, follow these steps:

1. docker push nualiev/brain-games:latest
2. docker run -it nualiev/brain-games

## Start Game

To start, enter the name of the game.
```commandline
$ brain-even
$ brain-calc
$ brain-gcd
$ brain-prime
$ brain-progression
```


