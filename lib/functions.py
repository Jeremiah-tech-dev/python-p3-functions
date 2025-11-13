#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1=45, num2=55):
    print(num1 + num2)
    add_result = num1 + num2
    return add_result

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
    