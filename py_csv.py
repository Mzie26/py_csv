#! /usr/bin/python3
"""
    author: Nicholas Kachur <nkachur@drexel.edu>
    date: 2014-06-15

    This library is a quick implementation of a CSV algorithm.
    It draws on the specification in Chapter 4 of Kernighan & Pike's
    "The Practice of Programming". Typical usage is creating a csv
    object by passing it a file or input stream and then repeatedly calling
    read_line until it generates an EOF signal.
"""

class Csv:
    """ Object which can be used to read the lines in CSV format """
    from sys import stdin, stdout

    def __init__(self, input_file=stdin, separator=','):
        self.input_file = input_file
        self.separator = separator

    def readline(self):
        line = self.input_file.readline().strip()
        return line.split(self.separator)

def main():
    csv_reader = Csv()
    csv_line = csv_reader.readline()
    while csv_line != ['']:
        print(csv_line)
        csv_line = csv_reader.readline()

if __name__ == '__main__':
    from sys import exit
    exit(main())
