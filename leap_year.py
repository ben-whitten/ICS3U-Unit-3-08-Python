#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you if a year is a leap year.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what tells you if the year is a leap year.
    print("")
    print("This program will tell you whether or not a year is a leap year...")
    print('')

    while True:
        # Input
        year_as_string = input(color.BOLD + color.YELLOW + 'Input a year: '
                               + color.END)

        # This is the joe mama easter egg, its just for fun.
        if year_as_string == ("who's joe"):
            print("")
            print(color.BOLD + 'JOE MAMA!' + color.END)

        # Process
        try:
            year_number = int(year_as_string)
            if year_number >= 0:
                if year_number % 4 == 0 and year_number % 100 != 0:
                    # Output
                    print('')
                    print(color.BOLD + color.GREEN + color.UNDERLINE +
                          'That year is a leap year' + color.END)
                    break
                elif year_number % 1000 == 0:
                    # Output
                    print('')
                    print(color.BOLD + color.GREEN + color.UNDERLINE +
                          'That year is a leap year' + color.END)
                    break
                else:
                    # Output
                    print('')
                    print(color.BOLD + color.RED + color.UNDERLINE +
                          'That year is not a leap year' + color.END)
                    break
            else:
                # Output
                print('')
                print(color.BOLD + color.RED + color.UNDERLINE +
                      'That year is not a leap year' + color.END)
                break
        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a year...' +
                  color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
