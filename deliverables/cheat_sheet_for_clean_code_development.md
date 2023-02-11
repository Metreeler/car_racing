# Cheat sheet fo Clean code development

These are the advices I try to apply to myself as much as possible, sometimes it isn't always easy for me to think about it, but I try my best.
They are not ordered by importance but are randomly organized. In my mind, all of them are equally important.

## 1 - Start to code with a cool mind.

Whenever I start coding, I want to have first thought about what I will do. I want to start coding knowing which direction I'm headed to and how much time will be needed. Therefore, I can cool my mind and still enjoy programming.
I don't want to end up losing my appeal for programming that's why I want to keep coding with a cool mind as much as possible.

## 2 - Let's start it as clean as possible ...

On the long run, it's always better to have an understandable environment. It starts as early as creating the first file name. Naming it with a clear view about what this file is for is always nice.

## 3 - ... and don't just stop there

It's really important for me to keep variable and method name that are easy for me to understand.

For example to make an Euclidian division it's better to make it like this:

```python
def euclidian_division(dividend, divisor):
    quotient = int(dividend / divisor)
    remainder = dividend - (divisor * quotient)
    return quotient, remainder
```

rather than just like this :

```python
def function_1(a, b):
    c = int(a / b)
    d = a - (b * c)
    return c, d
```

That way, I don't struggle whenever I need to modify a function or when I need to use it.

## 4 - Split your code

Whenever a part of code is used at two different spaces, it needs to be simplified in one single extra function. 

## 5 - And split it as much as possible functions

Whenever a method is doing multiple thing, just cut it in multiple function with only one purpose.
It really is one of the best way to ease debugging as you can easily spot where the problem is coming from. 
Moreover, you avoid having a name on the function that doesn't say precisely what it does.

So instead of this :

```python
def function_that_does_many_things():
    thing_a() # can sometimes be 20 lines long
    thing_b() # can sometimes be 20 lines long
    thing_c() # can sometimes be 20 lines long
```

And ending up with a single function with 60 or more lines, nearly impossible to debug.
I would prefer this : 

```python
def function_that_does_many_things():
    function_that_does_thing_a()
    function_that_does_thing_b()
    function_that_does_thing_c()

def function_that_does_thing_a():
    thing_a() # can sometimes be 20 lines long
    
def function_that_does_thing_b():
    thing_b() # can sometimes be 20 lines long
    
def function_that_does_thing_c():
    thing_c() # can sometimes be 20 lines long
```

where I can debug easily each function separately

## 6 - Respect the convention of the language

Whenever I use a new language I try to stick as much as possible to the convention of this language.
For example in python, variables names with multiple words are written with lowercase words separated by underscore.
However, in Java, you should write your variables with the first word in lowercase and all the oth words after starting with an uppercase:

JAVA : 
```java
public int myMultipleWordsVariable = 0
```

PYTHON :
```python
my_multiple_words_variable = 0
```
This really helps when trying to read online documentation as you don't have too much problem understanding the way the documentation works.

## 7 - Use the TODO

TODO is really useful whenever you need to remind yourself that there is something you haven't done yet that needs to be done.

## 8 - COMMENT YOUR CODE !!!!!

This one is in capital letter because I almost always forget to do it even though I know I should do it and I often hate myself for not doing it.
THe comments don't need to be to precise but at least help understand what is going on.

## 9 - Using libraries is good, understanding them is better

Sometimes, when using a library, it is really nice because it does exactly what you want. However, when using multiple libraries there are sometimes conflicts between them and trying to get a solution to find a solution can be really tedious.
That's why I try my best to be sure to understand how the library works, whenever I use a method, I want to be sure I understand all the parameters and what there are corresponding to.
For example I once used two different libraries to manipulate images (pyglet and opencv) and I told myself that linking both together wouldn't be difficult... After three hours of raging against my computer I finally discovered the x and y axis on one library were inverted compared to the other library and that's why my code was not working...

## 10 - Do not hesitate to comment huge chunk of the code

If a problem isn't solved simply, I comment huge chunks of code in order to reduce most of the possible side effects that could be occurring and then I uncomment it part by part in order to get where the problem is coming from.

## 11 - global variables

If a value is used at different places in the code, try to put in a single variable when possible. This will allow easy changes if this value where to be change in the future.

## 12 - DRY
    
Don't repeat yourself! I have been told for my whole life as programmer to not repeat myself and up to this day it's something I try to avoid as much as possible. 

## 13 - Deleting code when it's not used anymore

Sometimes I tend to keep code in comments even though it's not used anymore however it's clearer to the mind when these are removed.
