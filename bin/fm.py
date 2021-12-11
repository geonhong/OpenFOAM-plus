#!/usr/bin/env python3

import os, sys

from math import pi

argv = sys.argv[1:]

nSamples = 720
if '-nSamples' in argv:
    i = argv.index('-nSamples')
    nSamples = int(argv[i+1])

if '-rpm' in argv:
    i = argv.index('-rpm')
    rpm = float(argv[i+1])
    omg = rpm/60*2*pi

forceName = 'forces'
if '-forceName' in argv:
    i = argv.index('-forceName')
    forceName = argv[i+1]

timeName = '0'
if '-timeName' in argv:
    i = argv.index('-timeName')
    timeName = argv[i+1]

forceFile = open('postProcessing/' + forceName + '/' + timeName + '/force.dat', 'r')
momentFile = open('postProcessing/' + forceName + '/' + timeName + '/moment.dat', 'r')

forceData = forceFile.readlines()
momentData = momentFile.readlines()

fsum = 0.0
msum = 0.0

omg = 0.0

for i in range(1, nSamples+1):
    f = forceData[-i]
    m = momentData[-i]

    if f[0] == '#':
        # skip comment
        pass

    f = f.replace('(','').replace(')','').split()
    fx = float(f[1])
    fz = float(f[3])
    fsum += fx

    m = m.replace('(','').replace(')','').split()
    mx = float(m[1])
    mz = float(m[3])
    msum += mx

fave = fsum/nSamples
mave = msum/nSamples

print('Averaged force : ', fave, ' N')
print('Averaged moment: ', mave, ' N-m')

if omg>0.0:
    P = mave*omg
    print('Averaged power : ', P, ' W')
