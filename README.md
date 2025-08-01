# reca

radial elementary cellular automaton experimentation. the code is not pretty, nor fast, but it's okay as an experiment.

![](reca_14_92_010_False_1.5.png)

### how it works?

<table>
  <tbody>
    <tr>
      <td colspan="3">
        for the most part this is just a simple (and probably buggy) elementary cellular automaton https://en.wikipedia.org/wiki/Elementary_cellular_automaton, with an added wraparound at the edges that can be enabled. however the twist is that the projection happens on a polar grid instead of cartesian. combined with the wraparound this creates a radial elementary cellular automaton. rendering is being done via matplotlib, each row of the automaton becomes a bar chart with the number of cells it has. all bar charts have the same total length and are then placed on a polar plot.
      </td>
    </tr>
    <tr>
      <td>
        <img src="lin.png"/>
      </td>
      <td>
        <img src="rad.png"/>
      </td>
      <td>
        <img src="reca_14_92_010_False_1.5.png"/>
      </td>
    </tr>
  </tbody>
</table>

### gallery

a more extensive gallery can be found at [/gallery](https://github.com/Jana-Marie/reca/gallery)

### usage

```
usage: RECA [-h] [-i ITERATIONS] [-r RULE] [-s START [START ...]] [-a] [-m MULT] [-n] [-S]

Radial Elementary Cellular Automaton

options:
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS
                        number of iterations
  -r RULE, --rule RULE  ruleset, 0-255
  -s START [START ...], --start START [START ...]
                        start condition, must be a list of bits, e.g. [0,1,0]
  -a, --alt             alternative wrapover
  -m MULT, --mult MULT  cell growth factor
  -n, --no-display      display the plot
  -S, --save            save the plot

e.g. python3 recy.py -i 14 -Sn  # 14 iterations, do not display the plot, but save the figure
```

### batch generation

for bash, this can be used to iterate over rules. warning though, this will generate 256 pngs in the current directory, so you maybe want to run this in a seperate directory (via `... python3 ../reca.py ...` in a sub directory)

```
for i in {0..255}; do python3 reca.py -i 8 -Sna -r $i -m 2 -s 0 0 1 1 0 0 1 1; done;
```