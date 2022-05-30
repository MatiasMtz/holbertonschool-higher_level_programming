#!/usr/bin/python3
def lookup(obj):
    methods = []
    for attribute in dir(obj):
        methods.append(attribute)
    return methods
