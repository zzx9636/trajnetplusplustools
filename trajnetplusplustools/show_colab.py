import matplotlib.pyplot as plt

def predicted_paths(input_paths, pred_paths, pred_neigh_paths=None, output_file=None):
    """Context to plot paths."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.grid(linestyle='dotted')
    ax.set_aspect(1.0, 'datalim')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')

    # primary
    xs = [r.x for r in input_paths[0]]
    ys = [r.y for r in input_paths[0]]
    # track
    ax.plot(xs, ys, color='black', linestyle='solid', label='primary',
            marker='o', markersize=2.5, zorder=1.9)
    # markers
    ax.plot(xs[0:1], ys[0:1], color='black', marker='x', label='start',
            linestyle='None', zorder=0.9)
    ax.plot(xs[-1:], ys[-1:], color='black', marker='o', label='end',
            linestyle='None', zorder=0.9)

    # neigh tracks
    for ped_rows in input_paths[1:]:
        xs = [r.x for r in ped_rows]
        ys = [r.y for r in ped_rows]
        # markers
        ax.plot(xs[0:1], ys[0:1], color='black', marker='x', linestyle='None')
        ax.plot(xs[-1:], ys[-1:], color='black', marker='o', linestyle='None')
        # track
        ax.plot(xs, ys, color='black', linestyle='dotted')

    # primary
    for name, primary in pred_paths.items():
        xs = [r.x for r in primary]
        ys = [r.y for r in primary]
        # track
        ax.plot(xs, ys, linestyle='solid', label=name,
                marker='o', markersize=2.5, zorder=1.9)

    # neigh predictions
    if pred_neigh_paths is not None:
        for name, neigh_paths in pred_neigh_paths.items():
            for neigh_path in neigh_paths:
                xs = [r.x for r in neigh_path]
                ys = [r.y for r in neigh_path]
                # track
                ax.plot(xs, ys, linestyle='solid',
                        marker='o', markersize=2.5, zorder=1.9)

    # frame
    ax.legend()
    return fig

