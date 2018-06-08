# Bash Commands

## Learning Objectives

***Students Will Be Able To...***

* Navigate their computers in the terminal
* Create new files and folders in the terminal
* Manipulate files and folders in the terminal
* Never use finder again

## Context

* Programmers are lazy, and all about speed. 

---

## Lesson

## Introduction

* Bash is the shell language we will be using to work with and navigate through our computers

***What is the shell/terminal?***

* This is our way of talking directly to the computer. 
* You may be familiar with the Finder on a Mac or Explorer on the PC
* Those are Graphical User Interfaces, also known as GUI's. Something we'll discuss later on in the course
* We don't want to deal with GUI's and want to talk directly to the computer. 
* We do this using the terminal

***Why did you say programmers are lazy and like speed?***

* Another reason why many programmers use the terminal is because it is faster, and we don't want to have to grab a mouse or use the touch pad to click folders. 
* With the shell our fingers never have to leave the keyboard

---

## Bash Commands

##### Navigation

* `cd` - change directory to the user home directory
* `cd ..` - change directory to one level above current
* `cd ../..` - change directory to two levels above current
* `cd folder_name` - change director to specifc folder
* `pwd` - print working directory. Gives you the absolute path of where you currently are
* `ls` - List all the files and folders inside of your current directory

##### Create Some Thangs

* `mkdir folder_name` - make a new folder and give it a name
* `touch file_name` - create a new file and give it a name

##### Moving / Copy / Renaming

* `mv folder_to_move ending_destination` - move a folder to a specific destination
	* You can move multiple files at once
	* `mv file1 file2 file3 final_folder`
* `cp file_name destination` - copy a file to a specific destination
* `cp -r folder final_desination` - the "-r" is "recursive". Meant to copy all the files recursively from one folder to another
* `rm file_name` - remove a file 
* `rm -rf folder_name` - **BE CAREFUL WITH THIS COMMAND** the "-rf" will FORCEFULLY REMOVE anything you tell it to. If you typed the command but did not specify a folder to delete it will delete **EVERYTHING**... Forcefully...
* `open file_name` - will open a file with it's default program
* `open folder_name` - will open a folder in Finder
* `open .` - will open everything within this folder in Finder


---

## Relative Path / Absolute Path

***What is a path?***

* A path is the unique location to a file or folder on your computer

***What is the relative path?***

* A relative path is the path to a file or folder from the current working location in the directory
* example
* Current Directory

```
$ pwd
$ /Users/Admin/Documents/Pictures
```
* Target Directory

```
$ /Users/Admin/Videos/2016
```

* Change Directory using the Relative Path

```
$ cd ../../Videos/2016
```

***What is the absolute path?***

* A absolute path is the path to a file or folder from the root directory
* Absolute Path Example using same folder structure from above
* Current Directory

```
$ pwd
$ /Users/Admin/Documents/Pictures
```
* Target Directory

```
$ /Users/Admin/Videos/2016
```

* Change Directory using the Absolute Path

```
$ cd ~/Users/Admin/Videos/2016
```

