# -*- coding: utf-8 -*-
"""

@author: CollegeBoreal
"""

import json

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

def main():
  print(charge('b300115065.json'))

if __name__== "__main__":
    main()
