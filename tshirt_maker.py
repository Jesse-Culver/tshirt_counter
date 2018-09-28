#! /usr/bin/env/python3

# Generates a random million tshirts and saves to a csv file

import sys
import random

def main():
  colors = ['red','orange','yellow','green','blue','indigo','violet']
  file = open("tshirts.csv","w")
  for num in range(1000000):
    name = 'tshirt_'+f'{num}'
    color = random.choice(colors)
    file.write(f'{name},{color}\n')
  file.close()

if __name__ == '__main__':
  main()