class _Console:
    def __init__(self):
        self.ppnl = self.print_panel
        self.br = self.print_blank_line

        from rich.console import Console
        self.__console = Console()
    def print(self, *s, sep=" ", color="white", end="\n"):
        """Normal print statement"""
        self.__console.print(sep.join(s), end=end, style=color)
    def printil(self, *s, sep=" ", color="white"):
        """Print in-line, equal to console.print(..., end="")"""
        self.__console.print(sep.join(s), end="", style=color)
    def print_blank_line(self):
        """Print a blank line"""
        print()
    def print_panel(self, *s, sep=" ", text_color=None, border_color=None, color="white", title=""):
        """Print a modern panel"""
        from rich.panel import Panel
        self.__console.print(Panel(sep.join(s), title=title, title_align="left", border_style=border_color if border_color is not None else color), style=text_color if text_color is not None else color)
    def input(self, *s, sep=" ", color="white"):
        self.printil(*s, sep=sep, color=color)
        return input()
    def password_input(self, *s, sep=" ", color="white"):
        self.printil(*s, sep=sep, color=color)
        import getpass
        return getpass.getpass("")
def new_console():
    return _Console()