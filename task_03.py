#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON3:
TASK3 
Practice nested statements."""

PARENT = ['None', 'Seattle Gray', 'Manatee', 'Ceramic Glaze',
          'Culumus Nimbus', 'Platinum Mist', 'Spartan Sage']

NONE = ['Seattle Gray', 'Manatee']
SEATTLEGRAY = ['Ceramic Glaze', 'Culumus Nimbus']
MANATEE = ['Platinum Mist', 'Spartan Sage']
CERAMICGLAZE = ['Basically White', 'White']
CULUMUSNIMBUS = ['Off-White', 'Paper White']
PLATINUMMIST = ['Bone White', 'Just White']
SPARTANSAGE = ['Fractal White', 'Not White']

SELECTION = raw_input('Enter one of the following parent colors {0}'.format(PARENT))

if SELECTION == 'None':
    TYPE = 'Base'
    COLOR = raw_input('Enter one of the following colors {0}'.format(NONE))
    COLOR = COLOR if COLOR in NONE else None
elif SELECTION == 'Seattle Gray':
    TYPE = 'Accent'
    COLOR = raw_input('Enter one of the following colors {0}'.format(SEATTLEGRAY))
    COLOR = COLOR if COLOR in SEATTLEGRAY else None
elif SELECTION == 'Manatee':
    TYPE = 'Accent'
    COLOR = raw_input('Enter one of the following colors {0}'.format(MANATEE))
    COLOR = COLOR if COLOR in MANATEE else None
elif SELECTION == 'Ceramic Glaze':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(CERAMICGLAZE))
    COLOR = COLOR if COLOR in CERAMICGLAZE else None
elif SELECTION == 'Culumus Nimbus':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(CULUMUSNIMBUS))
    COLOR = COLOR if COLOR in CULUMUSNIMBUS else None  
elif SELECTION == 'Platinum Mist':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(PLATINUMMIST))
    COLOR = COLOR if COLOR in PLATINUMMIST else None
elif SELECTION == 'Spartan Sage':
    TYPE = 'Highlight'
    COLOR = raw_input('Enter one of the following colors {0}'.format(SPARTANSAGE))
    COLOR = COLOR if COLOR in SPARTANSAGE else None
else:
    if SELECTION not in PARENT or COLOR == None:
        print 'You have entered an invalid color'
COMPLETE = '{0}  has a parent color of {1} and a type of {2}'.format(COLOR, SELECTION, TYPE)
print COMPLETE
