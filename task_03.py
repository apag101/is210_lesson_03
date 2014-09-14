#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON3:
TASK3 
Practice nested statements."""

PARENT = ['None', 'Seattle Gray', 'Manatee', 'Ceramic Glaze',
          'Culumus Nimbus', 'Platinum Mist', 'Spartan Sage']

NONE = ['Seattle Gray', 'Manatee']
SG = ['Ceramic Glaze', 'Culumus Nimbus']
MT = ['Platinum Mist', 'Spartan Sage']
CR = ['Basically White', 'White']
CU = ['Off-White', 'Paper White']
PL = ['Bone White', 'Just White']
SP = ['Fractal White', 'Not White']

SELECTION = raw_input('Enter one of the following parent colors {0}'.format(PARENT))

if SELECTION == 'None':
    TYPE = 'Base'
    COLOR = raw_input('Enter one of the following colors {0}'.format(NONE))
    COLOR = COLOR if COLOR in NONE else None
elif SELECTION == 'Seattle Gray':
    TYPE = 'Accent'
    COLOR = raw_input('Enter one of the following colors {0}'.format(SG))
    COLOR = COLOR if COLOR in SG else None
elif SELECTION == 'Manatee':
    TYPE = 'Accent'
    COLOR = raw_input('Enter one of the following colors {0}'.format(MT))
    COLOR = COLOR if COLOR in MT else None
elif SELECTION == 'Ceramic Glaze':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(CR))
    COLOR = COLOR if COLOR in CR else None
elif SELECTION == 'Culumus Nimbus':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(CU))
    COLOR = COLOR if COLOR in CU else None  
elif SELECTION == 'Platinum Mist':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(PL))
    COLOR = COLOR if COLOR in PL else None
elif SELECTION == 'Spartan Sage':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(SP))
    COLOR = COLOR if COLOR in SP else None
else:
    if SELECTION not in PARENT or COLOR is None:
        print 'You have entered an invalid color'
COMPLETE = '{0}  has a parent color of {1} and a type of {2}'.format(COLOR, SELECTION, TYPE)
print COMPLETE
