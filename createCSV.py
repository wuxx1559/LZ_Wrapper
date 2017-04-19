'''
This script creates a csv file from significant loci for each trait/phenotype.
It takes as input a list of significant loci files (1 for each phenotype). Each file has a list of variants.
It outputs a comma separated file (.csv) that contains pertinent information for LocusZoom and the
local server api.
'''

import math, argparse, re, os, datetime, sys
from subprocess import Popen, PIPE
import pandas

def main():
  parser = argparse.ArgumentParser(prog='createJson', usage='%(prog)s [options]')
  parser.add_argument('txtFiles', metavar='files', nargs='+', help = 'The path to the text file')
  args = parser.parse_args()
  
  data_dict = {"analysis":[], "chromosome":[], "log_pvalue":[], "position":[], "pvalue":[], "ref_allele":[], "variant":[]}
  for txtf in args.txtFiles:
    analysis = os.path.basename(txtf).split('.')[0].strip()
    print analysis
    with open(txtf, 'r') as infile:
      for line in infile.readlines():
        if not line.startswith(b'#'):
          fields = line.split('\t')
          data_dict["analysis"].append(analysis)
          data_dict["chromosome"].append(fields[0].strip())
          data_dict["position"].append(int(fields[1].strip()))
          data_dict["variant"].append(fields[3].strip())
          ref_allele = fields[3].strip().split('_')[1].split('/')[0]
          data_dict["ref_allele"].append(ref_allele)
          pvalue = float(fields[10].strip())
          logp = -math.log(pvalue, 10)
          data_dict["pvalue"].append(pvalue)
          data_dict["log_pvalue"].append(logp)

  df = pandas.DataFrame(data_dict)
  df.to_csv('assoc.csv', sep=',', index=False)
        
if __name__ == "__main__":
  main()
