# A line starting with "# " is a comment

# This file is the list of the action executed by the restaurant over the course of one evening.
# This file is created to analyse how many people are entering the restaurant and ordering in order
# for the manager to see if the restaurant has enough waiters and enough tables in the restaurant.

# The action possible are:
# "enter" meaning someone enters the restaurant
# "order" meaning a client orders something
# "receive" meaning a client receive his order
# "leave" meaning a client leaves the restaurant because there is not enough tables available
# "leave_served" meaning a client leaves the restaurant
# "state" is used when the manager of the restaurant wants to know the current state of the restaurant

# 6:00PM
15 enter
10 order
2 receive
state

# 6:30PM
21 enter
15 order
14 receive
state

# 7:00PM
48 enter
34 order
40 receive
6 leave
8 leave_served
state

# 7:30PM
34 enter
34 order
4 receive
8 leave
26 leave_served
state

# 8:00PM
16 enter
16 order
42 receive
24 leave_served
state

# 8:30PM
21 enter
35 order
35 receive
15 leave_served
state

# 9:00PM
2 enter
8 order
4 receive
37 leave_served
state

# 9:30PM
5 order
13 receive
5 leave
8 leave_served
state

# 10:00PM
3 receive
6 leave_served
state

# 10:30PM
14 leave_served
state