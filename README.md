﻿# Knowledge Engineering
## Prerequisites
You need [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed to run this project.
## Setup
To run this project, first clone this project locally using git:
```
git clone https://github.com/namcoi99/knowledge-engineering.git
```
Install [scipy](https://scipy.org/install/) for complex math calculation using pip:
```
pip install scipy
```
Run project using python:
```
py main.py
```
## How to use
Required inputs are the number of questions in an exam and their distribution of difficulty:
```
Please enter the number of questions: 60

Please enter the number of questions of the question level: 
DIFFICULTY_HARD (Example: 20): 10
DIFFICULTY_MEDIUM (Example: 20): 10
DIFFICULTY_EASY (Example: 20): 10
DIFFICULTY_VERY_EASY (Example: 20): 30
```

```
The distribution of difficulty (K) is as follows: [0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.5]

Membership function for Exam time:
Uc(z) = 0.3333333333333333*TIME_LONG + 0.6666666666666666*TIME_MEDIUM
```
Here is the result:
```
Result: The appropriate test time is about 51.67 minutes.
```
