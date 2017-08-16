#!/usr/bin/python
import sys, getopt

def main(argv):
   input = ''
   output = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["input="])
   except getopt.GetoptError:
      print 'test.py -i <input> '
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'reverse.py -i <input>'
         print 'Example: reverse.py -i "this is my string"'
         sys.exit()
      elif opt in ("-i", "--input"):
         input = arg
# Revers the string
         reverse = input[::-1]
   print 'Input is  :"', input
   print 'Output is :"', reverse

if __name__ == "__main__":
   main(sys.argv[1:])
