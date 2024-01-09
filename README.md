# N-Queens Problem Solvers

* N-Queens Problem

The N-Queens problem is a classic puzzle in which the objective is to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal. It is a well-known combinatorial problem that has applications in various areas of computer science and artificial intelligence.

* Motivation

The motivation behind this project is to explore different solutions to the N-Queens problem using various search algorithms. The problem is not only an interesting puzzle but also serves as a valuable exercise in understanding and implementing different search strategies. By comparing the performance of different algorithms, we aim to gain insights into their strengths and weaknesses in solving combinatorial problems.

## Overview

This project implements different solutions for the N-Queens problem using various search algorithms. The N-Queens problem is a classic combinatorial problem where the goal is to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other.

## Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Algorithms](#algorithms)
6. [Contributing](#contributing)
7. [Authors](#authors)
8. [License](#license)

## Introduction

Briefly describe the N-Queens problem and the motivation behind this project. Explain the different algorithms used to solve the problem and how they are implemented.

## Project Structure

Describe the structure of your project. Highlight important files and directories. Explain the purpose of each file or directory.

```
AI Homework/
    PA1/
        AI_PA1.pdf
        AI_PA1_Base.py
    PA2/
        AI_PA2.pdf
        AI_PA2.py
        PA_2_KESKIN_ERTUGRUL_KARDAS.pdf
        Report.docx
        result.txt
    PA3/
        AI_PA_1_2_3_Report_200316059_200316011_200316045.docx
        AI_PA_1_2_3_Report_200316059_200316011_200316045.pdf
        AI_PA3.pdf
        result.txt
        resultv2.txt
    LICENSE
    README.md
```


## Installation

Provide instructions on how to install the necessary dependencies and set up the project environment. Include any external libraries or frameworks required.

```bash
pip install -r requirements.txt
```

## Usage
In this section, provide instructions on how users can run and interact with your N-Queens problem solver. Include examples and command-line instructions if applicable.

### Running the Solver

Navigate to the directory containing the solver script.
```
cd PA1 
cd PA2
cd PA3
```
Execute the following command to run the solver:
```bash
python nqueens_solver.py [options]
```
### Options
* -n, --queens: Specify the number of queens (N) for the N-Queens problem.
* -algorithm: Choose the search algorithm (e.g., DFS, BFS, A*).
* -verbose: Enable verbose mode for additional output.
Example

```bash
python nqueens_solver.py -n 8 -algorithm DFS -verbose
```
## Algorithms

Describe the different search algorithms implemented in your project for solving the N-Queens problem. Provide a brief overview of each algorithm's approach.

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking. In the context of N-Queens, it involves placing queens on the board and exploring the solution space until a valid placement is found or all possibilities are exhausted.

### Breadth-First Search (BFS)

BFS explores the solution space level by level. It starts with the initial state (empty board) and explores all possible configurations with one queen placed before moving to configurations with two queens, and so on.

### A* Search

A* is an informed search algorithm that uses a heuristic to guide the search. In the context of N-Queens, A* considers both the cost to reach the current state and an estimate of the remaining cost (heuristic) to find an optimal solution efficiently.

## Contributing
If you'd like to contribute to the project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Implement your changes.

Test thoroughly to ensure no regressions.

Create a pull request with a clear description of your changes.

## Authors

List the authors or contributors of the project along with their contributions.

Musa Sina ERTUĞRUL - Implemented DFS algorithm
İkram Celal KESKİN - Contributed to BFS algorithm
Mert KARDAS        -
## License

