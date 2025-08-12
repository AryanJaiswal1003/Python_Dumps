## Python Calculator
A simple yet flexible calculator built in Python.

## Overview
This Python Calculator is a command-line tool that allows you to perform basic arithmetic operations — Addition, Subtraction, Multiplication, and Division.
It supports continuous calculations using the previous result or starting fresh anytime.

## Features
✅ Basic operations: +, -, *, /
✅ Continuous mode — keep calculating with the last result
✅ ASCII art banner from an external art.py file
✅ Clear screen between fresh calculations

## Customization
1. Add more mathematical functions by defining them and adding to maths_dict.

2. Replace print("\n" * 100) with OS-specific clear commands for better screen clearing:

import os
os.system('cls')   # Windows   
os.system('clear') # Linux/Mac