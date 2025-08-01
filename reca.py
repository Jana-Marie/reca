#!/bin/python3

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math, argparse

class RECA(object):
  def __init__(self, iterations, rule, start, alt_mode, mult, no_display, save):
    super(RECA, self).__init__()
    self.iterations = iterations
    self.intrule = rule
    self.rule = self.generate_rule(rule)
    self.start = start
    self.vals = {0: self.start}
    self.alt_mode = alt_mode
    self.mult = mult
    self.no_display = no_display
    self.save = save

  # code partly by https://thehardcorecoder.com/2025/04/28/elementary-cellular-automaton/
  def generate_rule(self, rule):
    bit_string = f'{rule:08b}'
    return {f'{bx:03b}':b for bx,b in enumerate(reversed(list(int(b) for b in bit_string)))}

  def run(self):
    row = self.start
    rows = [row]

    for i in range(self.iterations):
      new_row = [0]*(round(len(rows[i])*self.mult)+1)
      print('iteration', i+1, 'of', self.iterations, 'with a length of', len(new_row), 'elements', end='\r')
      if self.alt_mode:
        keyrow = row + row + row
        for j in range(round(len(rows[i])*self.mult-1)):
          key = "".join(str(x) for x in keyrow[j:j+3])
          val = self.rule[key]
          new_row[j+1] = val
      else:
        keyrow = row + row[0:3]
        for j in range(len(rows[i])-1):
          key = "".join(str(x) for x in keyrow[j:j+3])
          val = self.rule[key]
          new_row[j+1] = val
      row = new_row
      self.vals[i+1] = row
      rows.append(row)
    print()
    return rows

  def show(self):
    print('setting up plot')

    fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
    size = 0.1

    cmap = plt.colormaps["bone"]
    for i in range(0, self.iterations):
      valsnorm = [2*np.pi/len(self.vals[i])]
      color_ = []
      for j,k in enumerate(self.vals[i]):
        if j >= 1:
          valsnorm.append(valsnorm[j-1]+valsnorm[0])
        color_.append(255*(1-k))
      color = cmap(color_)

      ax.bar(x=valsnorm,
             width=valsnorm[0],
             bottom=i*size+0.2, height=size,
             color=color, edgecolor='w',
             linewidth=0, align="edge")

    ax.set_axis_off()

    print('rendering plot')
    if self.no_display:
      print('displaying plot')
      plt.show()
    if self.save:
      print('saving plot')
      fig.savefig('reca_' + str(self.iterations) + '_' + str(self.intrule) + '_' + ''.join(map(str, self.start)) + '_' + str(self.alt_mode) + '_' + str(self.mult) + '.png',
                  bbox_inches='tight', dpi=1051.5)

if __name__ == '__main__':
  
  parser = argparse.ArgumentParser(
    prog='RECA',
    description='Radial Elementary Cellular Automaton',
    epilog='e.g. python3 reca.py -i 14 -Sn')
  parser.add_argument('-i', '--iterations', type=int, help='number of iterations', default=8) 
  parser.add_argument('-r', '--rule', type=int, help='ruleset, 0-255', default=92) 
  parser.add_argument('-s', '--start', nargs='+', type=int, help='start condition, must be a list of bits, e.g. [0,1,0]', default=[0,1,0]) 
  parser.add_argument('-a', '--alt', action='store_true', help='alternative wrapover') 
  parser.add_argument('-m', '--mult', type=float, help='cell growth factor', default=1.5) 
  parser.add_argument('-n', '--no-display', action='store_false', help='display the plot') 
  parser.add_argument('-S', '--save', action='store_true', help='save the plot') 
  args = parser.parse_args()
  
  reca = RECA(args.iterations, args.rule, args.start, args.alt, args.mult, args.no_display, args.save)
  reca.run()
  reca.show()