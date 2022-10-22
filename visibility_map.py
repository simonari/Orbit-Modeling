import os

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
    im = axis.imshow(_map, cmap="hot", extent=[0, 360, -90, 90])

    colors = [im.cmap(im.norm(value)) for value in map_unique]
    patches = [mpatches.Patch(color=colors[i], label="{l}".format(l=map_unique[i])) for i in range(len(map_unique))]
    axis.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    print(f"[+] Heatmap plotted", flush=True)

    figure.axes[0].set_title(f"Cycle {cur_cycle}/{cycles}")
    figure.savefig(os.path.join(path, f"cycle {cur_cycle}_{cycles}"), bbox_inches='tight')

    print(f"[+] Plot saved to a file.", flush=True)
