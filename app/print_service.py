"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files of the Small Proprietary Original Project OnSurf.
File content description: This file the print service file of the project.

This file contains functions that prints menus and welcome messages to the terminal.
"""

def print_line(char: str = "-") -> None:
    print(char * 61)


def print_OnSurf() -> None:
    print_line("=")
    print("                      WELCOME to OnSurf                      ")
    print_line("=")


def print_userspace() -> None:
    print_line("=")
    print("                       USERSPACE                         ")
    print_line("=")


def print_admin_menu() -> None:
    print_line("_")
    print("Administrator Menu:")
    print("delete user")


def print_welcome_menu() -> None:
    print_line("_")
    print("Menu:")
    print("'login'")
    print("'create user'")


def print_base_user_menu() -> None:
    print_line("_")
    print("Base User Menu:")
    print("'add location'")
    print("'remove location'")
    print("'display userspace'")
    print("'get weather'")
    print("'best surf spot'")


def print_user_menu() -> None:
    print_line("_")
    print("'logout'")
    print("'q' or 'quit'")
    print_line("_")
