import pandas as pd
import matplotlib.pyplot as plt

plot_configs = [
    {
        'plot_name': "mflops_plot.png",
        'fname': "mflops_data.csv",
        'plt_title': "MFLOP/s of 3 Sum Methods: Perlmutter CPU Node",
        'plt_ylabel': "MFLOP/s"
    },
    {
        'plot_name': "bandwidth_plot.png",
        'fname': "bandwidth_data.csv",
        'plt_title': "% of Bandwidth Used of 3 Sum Methods: Perlmutter CPU Node",
        'plt_ylabel': "% of Memory Bandwidth Used"
    },
    {
        'plot_name': "latency_plot.png",
        'fname': "latency_data.csv",
        'plt_title': "Memory Latency of 3 Sum Methods: Perlmutter CPU Node",
        'plt_ylabel': "Average Memory Latency (ns)"
    }
]

for config in plot_configs:
    plot_fname = config['plot_name']
    fname = config['fname']

    df = pd.read_csv(fname, comment="#")
    print(df)

    var_names = list(df.columns)
    print("var names =", var_names)

    problem_sizes = df[var_names[0]].values.tolist()
    code1_time = df[var_names[1]].values.tolist()
    code2_time = df[var_names[2]].values.tolist()
    code3_time = df[var_names[3]].values.tolist()

    plt.figure()
    plt.title(config['plt_title'])

    xlocs = [i for i in range(len(problem_sizes))]
    plt.xticks(xlocs, problem_sizes)

    plt.plot(code1_time, "r-o")
    plt.plot(code2_time, "b-x")
    plt.plot(code3_time, "g-^")

    plt.xlabel("Problem Sizes")
    plt.ylabel(config['plt_ylabel'])

    varNames = [var_names[1], var_names[2], var_names[3]]
    plt.legend(varNames, loc="best")
    plt.grid(axis='both')

    plt.savefig(plot_fname, dpi=300)
    plt.close()