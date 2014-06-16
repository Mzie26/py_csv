`py_csv` - Ligthweight Python CSV Library
=========================================

This project is simply an quick attempt to implement a CSV library in python. It intends to follow the specification contained in Kernighan & Pike's *Practice of Programming*.

Essentially, the use case is initializing a `csv` object with some input stream or file and then using the `read_line` method of that object to return a tuple of all the fields in the next line. Like files in python, once a line is read, the position in the input buffer is moved forward, so no one is read more than once.

Quoted fields will be handled as single fields, so separators can occur within quotation marks. Additionally, quotes can be doubled up or escaped (i.e. `""`, `''`, or `\"`) to allow for a raw quotation mark within a quoted field.
