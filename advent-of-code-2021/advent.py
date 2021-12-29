import unittest
import re
import collections

def file_to_lines(fname):
    return open(fname).read().splitlines()

def bool_list_to_decimal(lst):
    return int("".join([ str(n) for n in lst ]), 2)

def partition(seq, predicate):
    yes, no = [], []

    for item in seq:
        (yes if predicate(item) else no).append(item)

    return yes, no

# Code from Peter Norvig's Advent of Code utilities

def ints(text):
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))

def digits(text):
    """A tuple of all the digits in text (as ints 0–9), ignoring non-digit characters."""
    return mapt(int, re.findall(r'[0-9]', text))

def words(text):
    """A list of all the alphabetic words in text, ignoring non-letters."""
    return re.findall(r'[a-zA-Z]+', text)

def atoms(text):
    """A tuple of all the atoms (numbers or symbol names) in text."""
    return mapt(atom, re.findall(r'[a-zA-Z_0-9.+-]+', text))

def atom(text):
    """Parse text into a single float or int or str."""
    try:
        x = float(text)
        return round(x) if round(x) == x else x
    except ValueError:
        return text
    
def parse(day, parser=str, sep='\n', print_lines=7):
    """Split the day's input file into entries separated by `sep`, and apply `parser` to each."""
    fname   = f'day{day:02}.txt'
    text    = open(fname).read()
    entries = mapt(parser, text.rstrip().split(sep))
    
    if print_lines:
        all_lines = text.splitlines()
        lines     = all_lines[:print_lines]
        head      = f'{fname} ➜ {len(text)} chars, {len(all_lines)} lines; first {len(lines)} lines:'
        dash      = "-" * 100
        
        print(f'{dash}\n{head}\n{dash}')
        
        for line in lines:
            print(trunc(line))
            
        print(f'{dash}\nparse({day}) ➜ {len(entries)} entries:\n'
              f'{dash}\n{trunc(str(entries))}\n{dash}')
        
    return entries

def trunc(s: str, left=70, right=25, dots=' ... '):
    """All of string s if it fits; else left and right ends of s with dots in the middle."""
    dots = ' ... '
    return s if len(s) <= left + right + len(dots) else s[:left] + dots + s[-right:]

def mapt(fn, *args) -> tuple:
    """map(fn, *args) and return the result as a tuple."""
    return tuple(map(fn, *args))
