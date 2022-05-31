#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object", 0):str.find("language", 0)] + str[-22:-17] + str[:6]
print(str)
