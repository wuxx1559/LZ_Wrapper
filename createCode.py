'''
This script creates a LocusZoom HTML file for the app to run with custom data.
It takes two inputs:
  1. A significant variants file. It is a tab delimited file with chromosome and position.
  2. A phenotypes file - it is a tab delimited file with a phenotype id and the name of a phenotype.
It uses user-specified data, head.html, mid.html and tail.html to output a LocusZoom html file.
'''

import math, argparse, re, os, datetime, sys
from subprocess import Popen, PIPE
import pandas

def main():
  parser = argparse.ArgumentParser(prog='createCode', usage='%(prog)s [options]')
  parser.add_argument('sigLoci', metavar='variants file', nargs='?', help = 'The path to the important variants')
  parser.add_argument('phenos', metavar='phenotype file', nargs='?', help = 'The path to the phenotypes file')
  args = parser.parse_args()

  colors = ["rgb(212, 63, 58)", "rgb(238, 162, 54)", "rgb(92, 184, 92)", "rgb(53, 126, 189)", \
            "rgb(255, 255, 51)", "rgb(255, 102, 255)", "rgb(160, 160, 160)"]
  
  with open('head.html', 'r') as f:
    for line in f.readlines():
      print line.rstrip()

  print '    var phenos = ['
  count = 0
  with open(args.phenos, 'r') as f:
    for line in f.readlines():
      fields = line.split('\t')
      s_id = fields[0].strip()
      s_name = fields[1].strip()
      print '\t{ namespace: "' + str(s_id) + '", title: "' + s_name + '" , color: "' + colors[count] +'", study_id: "' + str(s_id)  +'" },'
      count = count + 1
  print '     ];'

  with open('mid.html', 'r') as f:
    for line in f.readlines():
      print line.rstrip()

  print '    var top_hits = ['
  with open(args.sigLoci, 'r') as f:
    for line in f.readlines():
      fields = line.split('\t')
      chrom = fields[0].strip()
      pos = fields[1].strip()
      var = str(chrom) + ':' + str(pos)
      print '\t["' + var + '","' + var +'"],'

  print '    ];'
  with open('tail.html', 'r') as f:
    for line in f.readlines():
      print line.rstrip()
        
if __name__ == "__main__":
  main()
