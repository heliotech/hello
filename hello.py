#!/usr/bin/python3
# -*- coding: utf-8 -*-

# hello.py

"""
Learning git with nvim

author: Sebastian Kazimierski, mgr. inż.

date@time: 2024.06.06@10:12:51
version: 0.0.1
"""

ftitle = __file__.split("/", maxsplit=-1)[-1].split(".", maxsplit=-1)[0]

print(f"{ftitle}: learning git, hello world!")

# Further changes:
name = input("Enter your name: ")

print(f"Hello, {name}!")
