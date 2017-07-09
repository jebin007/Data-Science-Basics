from s5v3 import *

def create_line_chart(data_sample, title, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    prices = (sorted(map(float, data_sample)))

    x_axis_ticks = list(range(len(data_sample)))
    ax.plot(x_axis_ticks, prices, linewidth=2)
    ax.set_title(title)
    ax.set_xlim([0, len(data_sample)])
    ax.set_xlabel('This is the X')
    ax.set_ylabel('This is the Y')

    fig.savefig(exported_figure_filename)

create_line_chart([float(x[2]) for x in jcrew_ties[1:]], "This is the Title", "labels.png")
