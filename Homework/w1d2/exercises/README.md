# Week 1 Day 2

Today we will start on file I/O and recursion as-well as `continue` with loop's flow control.

## Files

Files can be read and written to in python with the [`open()` object](https://docs.python.org/3.5/library/functions.html#open).
```python3
with open(file_name) as file:
  file_contents = file.read();

words = file_contents.split()
```

Here are some notable methods for the `open()` object:
* `read()`
* `readline()`
* `close()`
* `seek()`

**Other reseources**
[Reading and writing files python docs](https://docs.python.org/3.5/tutorial/inputoutput.html#reading-and-writing-files)

[Reading and writing files tutorial](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)

## Other notable Resources
Check out some of these functions, methods and [bultins](https://docs.python.org/3.5/library/functions.html). They *may* help you with todays work and will help with leaning python in genreal.


[`with` python doc's](https://docs.python.org/3/reference/compound_stmts.html#with)

[`enumerate()` python docs](https://docs.python.org/3.5/library/functions.html#enumerate)

[`zip()`](https://docs.python.org/3.5/library/functions.html#zip)

[Great CS 50 video on recursion](https://www.youtube.com/watch?v=t4MSwiqfLaY)
