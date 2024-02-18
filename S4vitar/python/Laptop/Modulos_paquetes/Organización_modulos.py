#!/usr/bin/env python3

def suma(x, y):

    return x+y

def resta(x, y):

    return x-y

def multi(x, y):

    if y==0:
        raise ValueError("[!] No es posible multiplicar entro cero")
    else: 
        return x*y

def division(x, y):

    if y==0:
        raise ValueError("[!] No es posible dividir entre cero")
    else:
        return x/y
