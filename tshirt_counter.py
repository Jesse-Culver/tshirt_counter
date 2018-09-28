#! /usr/bin/env/python3

# It counts tshirts present in the tshirts.csv file

import csv

def main():
  with open('tshirts.csv') as csv_file:
    # read in the tshirts
    reader = csv.reader(csv_file, delimiter=',')
    tshirts_dict = {}
    # go through all the tshirts and add if not present to dict
    # otherwise increment
    for _tshirt, color in reader:
      if color in tshirts_dict:
        tshirts_dict[color] += 1
      else:
        tshirts_dict[color] = 1
    for color, count in tshirts_dict.items():
      print(f'Found {count} {color} tshirts')


if __name__ == '__main__':
  main()