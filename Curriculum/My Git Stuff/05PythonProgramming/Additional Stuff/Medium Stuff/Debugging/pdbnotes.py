'''
to run pdb enter at cmd
python -m pdb FILE NAME 

ie:
python -m pdb list_largest_row_column.py

can also enter this at a line in the file: import pdb; pdb.set_trace()

get a prompt of pdb for python debugger

typing h or help outputs:

(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

important ones:

n or next:
runs through the next line in the funciton until it completes or moves to the next funciton

continue or c:
continues until it sees a break point

help or h

typing h and then another command gives more details

list or l:
Shows where you are at in code

p or print:
prints

s or step:
goes through a function ie steps into the function

quit

'''