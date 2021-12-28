# Knowledge Engineering - IT4362
 The project applies **Fuzzy Logic** to **determine the time to take the multiple-choice test**
 
## Prerequisites
You need [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed to run this project.
## Setup
1. To run this project, first clone this project locally using git:
```
git clone https://github.com/namcoi99/knowledge-engineering.git
```
2. Install [scipy](https://scipy.org/install/) for complex math calculation using pip:
```
pip install scipy
```
3. Run project using python:
```
py main.py
```
## How to use
1. Required inputs are the number of questions in an exam and their distribution of difficulty: 

(Number of questions is **ranged from 10 to 60** corresponding to the intervals "very few", "few", "medium", "large")
   
```
Please enter the number of questions[10-60]: 60

Please enter the number of questions of the question level: 
DIFFICULTY_HARD (Example: 20): 10
DIFFICULTY_MEDIUM (Example: 20): 10
DIFFICULTY_EASY (Example: 20): 10
DIFFICULTY_VERY_EASY (Example: 20): 30
```
2. The program will display membership function for Exam time corresponding to the inputs:
```
The distribution of difficulty (K) is as follows: [0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.5]

Membership function for Exam time:
Uc(z) = 0.3333333333333333*TIME_LONG + 0.6666666666666666*TIME_MEDIUM
```
3. Here is the result:
```
Result: The appropriate test time is about 51.67 minutes.
```
