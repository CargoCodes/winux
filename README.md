# Winux

Integration of some Linux terminal commands for Windows Command Prompt.

This CLA is in costant update with new command.

`Warning! Installing this library in a Linux OS or in a OS X (mac) machine may cause system commands overriding, 
which could become a serious problem. The code is ment to not work in non-Windows systems, but in Unix OSes it could 
overwite and "hide" the commands it provides.`



`Installation`:

    $ pip install winux

This Command Line Application allows to use Linux terminal commands in Windows Command Prompt.


`Integrated commands`: 
    
      Linux        Windows              Function

    $ clear         (cls)               Clear terminal window

    $ ls            (dir)               Show directory content

    $ mv            (move)              Move a file into another directory, or rename it

    $ cp            (copy)              Copy a file into another directory

    $ rm            (del)               Remove a file
    
    $ rm -rf        (rmdir)             Remove a directory

    $ cat           (type)              Show file content

    $ pwd           (chdir)             Shows current path

    $ date          (time)              Shows date and time

    $ nano          (edit)              Edit a file

    $ mem           (free)              Display free space

    $ kill          (taskkill)          Kill a process

    $ man           (?/)                Shows help for commands

    $ mkdir         (md)                Make a directory

    $ touch         (type nul >>)       Create an empty file

