import os

import matplotlib.colors
# types
from numpy import array

# functions
from numpy import unique

# plotting
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


def visibility_map(_map: array, cur_cycle, cycles, path):
    figure, axis = plt.subplots()

    map_unique = unique(_map)

    plt.gca().set_aspect('equal')
    im = axis.imshow(_map, cmap="RdYlGn", extent=[0, 360, -90, 90], vmin=0, vmax=12)

    colors = [im.cmap(im.norm(value)) for value in map_unique]
    norm = matplotlib.colors.Normalize(vmin=0, vmax=24)
    patches = [mpatches.Patch(color=plt.cm.get_cmap("RdYlGn")(norm(i)), label=f"{i}") for i in range(0, min(map_unique))]
    patches += [mpatches.Patch(color=colors[i], label="{l}".format(l=map_unique[i])) for i in range(len(map_unique))]
    axis.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    print(f"[+] Heatmap plotted", flush=True)

    title = r"$\frac{%s}{%s}T$" % (cur_cycle + 1, cycles) if cur_cycle + 1 != cycles else r"$T$"
    figure.axes[0].set_title(title)
    axis.set_xlabel(r"Долгота, $\circ$")
    axis.set_ylabel(r"Широта, $\circ$")
    figure.savefig(os.path.join(path, f"cycle {cur_cycle}_{cycles}"), bbox_inches='tight')

    print(f"[+] Plot saved to a file.", flush=True)
