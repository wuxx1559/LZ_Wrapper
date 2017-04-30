import math, argparse, re, os, datetime, sys
from subprocess import Popen, PIPE
import pandas
from collections import OrderedDict

def main():
  parser = argparse.ArgumentParser(prog='createCode', usage='%(prog)s [options]')
  parser.add_argument('phenos', metavar='phenotype file', nargs='?', help = 'The path to the phenotypes file')
  args = parser.parse_args()

  colors = ["rgb(212, 63, 58)", "rgb(238, 162, 54)", "rgb(92, 184, 92)", "rgb(53, 126, 189)", \
            "rgb(255, 255, 51)", "rgb(255, 102, 255)", "rgb(160, 160, 160)"]
  
  count = 0
  out_dir = os.path.dirname(args.phenos)
  all_out = open(out_dir + '/index.html', 'w')
  w_out = open(out_dir + '/wrapper.html', 'w')
  write_head(all_out, "All phenotypes", "15:78800000-78820000")
  all_out.write('    var phenos = [' + '\n')

  sig_loci = {}

  with open('html/wrapper_top.html', 'r') as w:
    for line in w.readlines():
      w_out.write(line.rstrip() + '\n')

  w_out.write('    <a class="tab" href="index.html" target="tabIframe2">All Phenotypes</a>\n')

  with open(args.phenos, 'r') as f:
    for line in f.readlines():
      fields = line.split('\t')
      s_id = fields[0].strip()
      s_name = fields[1].strip()
      s_fname = out_dir + '/' + fields[2].strip()
      p_html = s_id + '.html'
      print p_html

      w_out.write('    <a class="tab" href="' + p_html + '" target="tabIframe2">' + s_name +'</a>\n')

      with open(out_dir + '/' + p_html, 'w') as out:
        write_sigs(out, s_fname, s_name, s_id, colors[count], sig_loci)

      all_out.write('\t{ namespace: "' + str(s_id) + '", title: "' + s_name + '" , color: "' + colors[count] +'", study_id: "' + str(s_id)  +'" },\n')
      count = count + 1

  all_out.write('     ];' + '\n')
  with open('html/mid_all.html', 'r') as a:
    for line in a.readlines():
      all_out.write(line.rstrip() + '\n')
  all_out.write('    var top_hits = [' + '\n')
  sort_write(all_out, sig_loci)
  all_out.write('    ];\n')
  write_tail(all_out)
  all_out.close()

  with open('html/wrapper_bottom.html', 'r') as w:
    for line in w.readlines():
      w_out.write(line.rstrip() + '\n')

  w_out.close()
        
def write_head(outfile, name, locus):
  with open('html/head_top.html', 'r') as a:
    for line in a.readlines():
      outfile.write(line.rstrip() + '\n')
  outfile.write('\t<p>This set of plots shows significant loci for ' + name + '.</p>\n')
  with open('html/head_mid.html', 'r') as a:
    for line in a.readlines():
      outfile.write(line.rstrip() + '\n')
  outfile.write('\t\t<div id="plot" data-region="' + locus + '"></div>\n')
  with open('html/head_bottom.html', 'r') as a:
    for line in a.readlines():
      outfile.write(line.rstrip() + '\n')

def write_mid(outfile):
  with open('html/mid.html', 'r') as a:
    for line in a.readlines():
      outfile.write(line.rstrip() + '\n')

def write_tail(outfile):
  with open('html/tail.html', 'r') as d:
    for line in d.readlines():
      outfile.write(line.rstrip() + '\n')

def write_sigs(outfile, sigfile, s_name, s_id, color, all_sig_loci):
  p_loci = {}
  with open(sigfile, 'r') as c:
    for line in c.readlines():
      fields = line.split('\t')
      chrom = fields[0].strip()
      pos = fields[1].strip()
      if chrom not in p_loci:
        p_loci[chrom] = []
      if pos not in p_loci[chrom]:
        p_loci[chrom].append(pos)

      if chrom not in all_sig_loci:
        all_sig_loci[chrom] = []
      if pos not in all_sig_loci[chrom]:
        all_sig_loci[chrom].append(pos)

  some_chr = p_loci.keys()[0]
  h_locus = str(some_chr) + ':' + str(int(p_loci[some_chr][0]) - 300000) + '-' + str(int(p_loci[some_chr][0]) + 300000)
  write_head(outfile, s_name, h_locus)
  outfile.write('    var phenos = [' + '\n')
  outfile.write('\t{ namespace: "' + str(s_id) + '", title: "' + s_name + '" , color: "' + color +'", study_id: "' + str(s_id)  +'" },\n')
  outfile.write('     ];' + '\n')
  write_mid(outfile)
  outfile.write('    var top_hits = [' + '\n')
  sort_write(outfile, p_loci)
  outfile.write('    ];\n')
  write_tail(outfile)

def sort_write(outfile, loci):
  sorted_keys = loci.keys()
  has_X = False
  if all(item.isdigit() for item in sorted_keys):
    sorted_keys.sort(key=int)  
  elif 'X' in sorted_keys:
    has_X = True
    sorted_keys.remove('X')
    if not all(item.isdigit() for item in sorted_keys):
      raise ValueError('Significant loci chromosomes have an invalid value: ' + str(sorted_keys) + '\n')
    sorted_keys.sort(key=int)
  else:
    raise ValueError('Significant loci chromosomes have an invalid value: ' + str(sorted_keys) + '\n')

  for key1 in sorted_keys:
    poss = loci[key1]
    poss.sort(key=int)
    for pos in poss:
      var = str(key1) + ':' + str(pos)
      outfile.write('\t["' + var + '","' + var +'"],\n')

  if has_X:
    poss = loci['X']
    poss.sort(key=int)
    for pos in poss:
      var = 'X' + ':' + str(pos)
      outfile.write('\t["' + var + '","' + var +'"],\n')

if __name__ == "__main__":
  main()
