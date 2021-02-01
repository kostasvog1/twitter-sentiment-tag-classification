import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_pie(data, screen_name, figsize=(12,6)):
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(aspect="equal"))
    colors = ['red','orange','dodgerblue']
    agg_data = data['polarity'].value_counts(normalize=True).reset_index().sort_values('index')
    pie_data = agg_data['polarity']
    labels = [ str(round(row_.polarity*100,1))+'% '+ row_[0] for k, row_ in agg_data.iterrows() ]
    wedges, texts = ax.pie(pie_data, colors=colors,wedgeprops=dict(width=0.5), startangle=0)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
    title = '{}\nPolarity Breakdown of {} tweets'.format(screen_name, data.shape[0])
    ax.set_title(title)
    plt.tight_layout()
    plt.show()
    
    
def plot_trend(data, screen_name, figsize=(12, 4)):
    fig, ax = plt.subplots(figsize=figsize)
    data.groupby(data['Date'].dt.to_period('M')).agg({'free_text':'count'}).reset_index().plot('Date','free_text',ax=ax)
    ax.set_ylabel('# tweets')
    title = '# tweets posted each month'
    ax.set_title(title)
    plot_legend = plt.legend()
    plot_legend.get_texts()[0].set_text(screen_name)
    plt.tight_layout()
    plt.show()