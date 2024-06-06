#!/usr/bin/python3
# -*- coding: utf-8 -*-

# hello.py

"""
Learning git with nvim

author: Sebastian Kazimierski, mgr. inż.

date@time: 2024.06.06@10:12:51
version: 0.0.1
"""

import datetime

ftitle = __file__.split("/", maxsplit=-1)[-1].split(".", maxsplit=-1)[0]

print(f"{ftitle}: learning git, hello world!")

# Further changes:
name = input("Enter your name:\n> ")
name = "dude" if name == "" else (f"{name}." if len(name) == 1 else name)

# Git is working, fugitive also, but without reverting the changes…

# ────────────────────────────────────────────────────
# Another change, first after setting the remote repo,
# this thime not only with addition, but with deletion adn addition to the
# previous part.

greeting = f" Hello, {name}!"
opening = f"\n{greeting}\n{'─' * (len(greeting) + 1)}\n\n"
today = datetime.datetime.now()
day_name = today.strftime("%A")
date_str = today.strftime("%Y-%m-%d")
dnr = today.timetuple().tm_yday
hr_min = today.strftime("%H:%M")

print(f"{opening}Today is {day_name}, {date_str}, "
      f"it is {dnr} day of year and it is {hr_min}.")
