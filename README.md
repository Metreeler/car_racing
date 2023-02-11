# Car racing

This project is a simple 2D car game. There are two part of this little game, first there is the `Map Creator` part and second there is `Player`. 

When using the `Map Creator` part of this project, it is possible by following the prompted instructions to create a new map for the game.

When using the `Player` part of this project, it is possible to choose a map to play and then to enjoy a futuristic experience of driving.
![game_image](deliverables/game.png)

---
## Use and understand Git

For this project, I am using GitHub. The IDE I am using allows me to execute the main Git commands (pull, add, commit, push). 
However, I might be a bit old-fashioned as I still write the command lines directly in a command window

## UML

Attached to this project are three UML diagrams : 
1. You can find [here](https://github.com//Metreeler/car_racing/blob/main/deliverables/Activity_diagram.png) the activity diagram of this application. We have two types of user with different interactions to this game
2. You can find [here](https://github.com//Metreeler/car_racing/blob/main/deliverables/Use_case_diagram.png) the use case diagram of this application with all the different action path for the two types of user
3. You can find [here](https://github.com//Metreeler/car_racing/blob/main/deliverables/Uml_class_diagram.png) the class diagram of this application, it represents how the different classes interact with each other.

## DDD

## Metrics

In order to get some metrics for this project I used SonarCloud which is an online version on SonarQube. SonarQube is a tool to get the metrics of a project such as number of bugs, technical debt, lines of code, etc. SonarCloud allows me to get different metrics and to display the up-to-date version of these metrics thanks to badges.

- lines of code : [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- code smells : [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- maintainability : [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- security rating : [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- bugs : [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- vulnerabilities : [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- duplicated lines : [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- reliability rating : [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)
- technical debt : [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Metreeler_car_racing&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Metreeler_car_racing)

## Clean Code Development

During this whole project I tried my best to respect my own clean code ideas that are available on my clean code cheat sheet [here](https://github.com/Metreeler/car_racing/blob/main/deliverables/cheat_sheet_for_clean_code_development.md).
- Use really clear method function and variable names in order to not get lost (3 in cheat sheet). The names of my variables may seem long but whenever I read them their roles are obvious. Moreover, with the autocompletion of Pycharm it's not even that long to write code. We can see an example of this in the `__init__()` method of the `Car` class [here](https://github.com/Metreeler/car_racing/blob/905af2d7aff6a66d5bb8ae64d44854ce267ec2e8/src/main/python/car.py#L6)
- Split the large methods into smaller ones whenever it's possible(5 in cheat sheet). This makes debugging way easier. I particularly did that when I created the `update()` function of the `Car` class [here](https://github.com/Metreeler/car_racing/blob/905af2d7aff6a66d5bb8ae64d44854ce267ec2e8/src/main/python/car.py#L56) by having multiple method called in this one. This also avoid side effects or at least makes them easier to spot.
- Create a function for code needed in multiple places (4 in cheat sheet). That's why my file [maths.py](https://github.com/Metreeler/car_racing/blob/main/src/main/python/maths.py) was created. RIght now all the functions are only used in one place because I needed to clean my code at some point. However, all functions in this file were created with the state of mind "This is a mathematical rule and I might need it again later".
- Respect the python's convention (6 in cheat sheet). I was really careful to use the right syntax for variable names, method names and class names. We can see for example in the file [editor.py](https://github.com/Metreeler/car_racing/blob/main/src/main/python/editor.py) that the name of the class starts with an uppercase and all variables and methods names are lowercase words.
- Removing the commented code when it's not used anymore (13 in cheat sheet). I did my best removing the code in comments before I committed my modification to the git but as you can see on this [commit](https://github.com/Metreeler/car_racing/commit/5d48be47a4fd0ce434dccd0573914f3b872c04d8#diff-f4f566c3202c07390491ea3a20bb2f8d88c304ff54138af7d63e91d33741fb8d) there are some time little part of commented code that need to be removed.

## Build Management

I am using PyBuilder to build this project. It's the first time that I have ever used a builder for a Python project.
The build file is available [here](https://github.com/Metreeler/car_racing/blob/main/build.py).
In order to build follow the following steps:
1. install pybuilder locally
2. clone the repository
3. open a command prompt in the `car_racing` directory
4. execute `pyb publish`

## Unit Tests

In order to test a part of my code I used the unittest library of python. To demonstrate some usage of this library I tested the file [editor.py](https://github.com/Metreeler/car_racing/blob/main/src/main/python/editor.py) with the Editor class. I did the testing in this [file](https://github.com/Metreeler/car_racing/blob/main/src/unittest/python/editor_tests.py).

I chose to test the `__init__()` method in order to check the good initialization of all the parameters and also the `save()` method as there is a file to save and I wanted to make sure it was well saved.

## Continuous Delivery

The continuous delivery of my project is handled by Travis CI. 
This software allows me to build the project each time I push a new commit, using the combination of PyBuilder and Travis CI.

The status of the build is available here :

[![Build Status](https://app.travis-ci.com/Metreeler/car_racing.svg?branch=main)](https://app.travis-ci.com/Metreeler/car_racing)

There is now a problem with Travis CI as I don't have anymore credit available. However, we can see on this [commit](https://github.com/Metreeler/car_racing/commit/2160191bc8b6c137fc5b412a916d00dcdae88875) that the Travis CI build was successful on the build.

## IDE

For this project and most of my project in Python I use PyCharm. This IDE is made specifically for Python project and is easy to handle. Almost every feature is intuitive and thanks to the different sub-windows, it is easy to navigate between the code, the directories, the run windows, etc.

This IDE also analyze the code in real time to tell whether there are errors or warning in the code, so you don't have to run it and patch all the errors one by one.

Pycharm also have an integrated Git interface, which is really intuitive. However, out of habit I still use command lines and a command window.

My favorite shortcuts in this IDE are `Ctrl + /` allowing me to comment multiple line, which is very useful whenever there is a bug in my project. Another one is `Ctrl + Tab` which allows to easily switch between the different tabs opened in the IDE. Finally, the best one among all of them is just using `Tab` in order to get autocompletion, it makes me spare a lot of time.

## DSL

I did the DSL part of this report as an outside part of the project. This isn't linked to the game.

For this Domain Specific Language part, I used the example of a restaurant manager who wants to know how many people enter, leave, are being served,... in his restaurant. 
In order to do that, he juste have to write in the [data.dsl](https://github.com//Metreeler/car_racing/blob/main/deliverables/DSL/data.dsl) file how many customers enter, order, receive their order, leave and are rejected.
Then in order to get the evolution of the customers in the restaurant, he just needs to insert a line with "state" to get the current state of the restaurant.
The DSL interpreter for this file is located [here](https://github.com//Metreeler/car_racing/blob/main/deliverables/DSL/dsl_reader.py)

## Functional Programming

