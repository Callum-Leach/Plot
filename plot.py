import os
from collections import namedtuple

class Menu():

    Option = namedtuple('Option', 'label')
    _separator = "=" * 25
    _options = {1: Option("option one"), 2: Option("option two"),
                3: Option("option three"), 4: Option("option four")}

    def print_header(self):
        print ("{0}\n Please Select An Option\n{0}\n".format(self._separator))

    def print_mainMenu(self):
        self.print_header()
        for option in sorted(self._options.keys()):
            print ("{0} {1}".format(option, self._options[option].label))

    def prompt(self):
        return input("Select Option: ")

    def handle_input(self, chosen_option):
        try:
            print (self._options[chosen_option].label)
        except KeyError:
            print ("Wrong Option")


def main():
    menu = Menu()
    menu.print_mainMenu()
    menu.handle_input(menu.prompt())

if __name__ == '__main__':
    main()