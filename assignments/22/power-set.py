#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import FrozenSet
import random

def powerset(s: FrozenSet) -> set:
  """Compute powerset of a set."""
  if len(s) == 0:
    return [s]
  else:
    element = s.peek()
    powerset_of_rest = powerset(s - {element})
    print(powerset_of_rest)
    powerset_of_rest_with_element = set()
    for subset in powerset_of_rest:
      powerset_of_rest_with_element.add(subset)
      powerset_of_rest_with_element.add(subset | {element})
    return powerset_of_rest_with_element
  
if __name__ == "__main__":
  s = frozenset()
  for v in { 1, 2, 3 }:
    s = s | { v }
  print(f"""
    {s = },
    {powerset(s) = }
  """)
