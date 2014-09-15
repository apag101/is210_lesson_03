#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON3:
TASK5
Compound Examples."""
import decimal
NAME = raw_input('What is your name ?')
P = raw_input('What is the principal amount ?')
T = raw_input('How many years is the loan ?')
Q = raw_input('Are you pre-qualified ? (Yes or No)').lower()
N = 12
R = 0
TOTAL = None

if int(P) > 0 <= 199999:
    if int(T) >= 1 and int(T) <= 15:
        R = .0363 if Q == 'y' else .0465
    if int(T) >= 16 and int(T) <= 20:
        R = .0404 if Q == 'y' else .0498
    if int(T) >= 21 and int(T) <= 30:
        R = .0577 if Q == 'y' else .0639
if int(P) >= 200000 <= 999999:
    if int(T) >= 1 and int(T) <= 15:
        R = .0302 if Q == 'y' else .0398
    if int(T) >= 16 and int(T) <= 20:
        R = .0327 if Q == 'y' else .0408
    if int(T) >= 21 and int(T) <= 30 and Q == 'y':
        R = .0466
if int(P) >= 1000000:
    if int(T) <= 15 and Q == 'y':
        R = .0205
    if int(T) >= 16 and int(T) <= 20 and Q == 'y':
        R = .0262

TOTAL = int(round(int(P) * (1 + decimal.Decimal(R) / N) ** (N * int(T)), 0))

REPORT = '''Loan Report For: {n}
-----------------------------
    Principal:      {pr} 
    Duration:       {Time}
    Prequalified?:  {q}
    Total:          {total}'''.format(n=NAME, pr=P, Time=T, q=Q, total=TOTAL)
print REPORT
