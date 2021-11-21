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
