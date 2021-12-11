#!/usr/bin/env python3

import os, sys

argv = sys.argv[1:]

pardir = os.getcwd()
trgdir = argv[0]
fname = argv[1]

pvdfile = open(trgdir + "_" + fname + '.pvd', 'w')

pvdfile.write('''<?xml version="1.0"?>
<VTKFile type="Collection" version="0.1"
         byte_order="LittleEndian"
         compressor="vtkZLibDataCompressor">
  <Collection>
''')

if os.path.isdir(trgdir):
    os.chdir(trgdir)

    timedir = sorted(os.listdir('.'))

    for t in timedir:
        pvdfile.write('  <DataSet timestep="' + t + '" group="" part="0"\n'
                      '           file="' + trgdir + '/' + t + '/' + fname + '.vtp" />\n')

pvdfile.write("  </Collection>\n"
              "</VTKFile>")

pvdfile.close()
