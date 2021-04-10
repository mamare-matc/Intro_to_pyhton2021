#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="This is Mahlet script")

#basic
parser.add_argument('-m', dest='BASIC', help='Enter some text')


#interger
parser.add_argument('-i', '--interger', dest='varInteger', metavar='[an integer]',
default=10, type=int, required=False, help='<required> Enter a simple Integer')


#float
parser.add_argument('-d','--float',dest='varFloat', metavar='[a float]', default=10.0,
type=float, required=False, help='Enter a simple Float')

#string
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]',
default='hello', type=str, required=False, help='Enter a simple string')

#list
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+',
required=False,  help='Enter a list of strings (space delimited)')

#boolean
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true',
required=False, help='Toggle from default False to True')

parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false',
required=False, help='Toggle from default True to False')

#script version
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

#using the parser
args = parser.parse_args()

if len(sys.argv) == 1:
   print(parser.print_help())
   exit(0)




