import re
import os
import pandas as pd
import matplotlib.pyplot as plt


def analysis(path_in, path_out, **kwargs):
    """ A short analysis for selected kpi of a Cbc logfile
        Version Cbc Solver: 2.9.7
        Setting: -printingOptions all
        """
    summary = kwargs.get('summary', True)
    plot = kwargs.get('plot', False)

    if(summary is False and plot is False):
        print('ma dai, stai scherzando ;-)')

    if not os.path.isdir(path_out):
        os.makedirs(path_out)

    files = os.listdir(path_in)

    if summary is True:
        """ org_problem_bins: Number of binaries of the original problem
            pre_problem_bins: Number of binaries of the presolved problem
            rows: Number of rows of the presolved problem
            cols: Number of columns of the presolved problem
            obj: Objective value
            gap: Gap
            time: Time (Wallclock seconds)
            """
        kpi = ['org_problem_bins', 'pre_problem_bins', 'rows', 'cols',
               'obj', 'gap', 'time']
        df_summary = pd.DataFrame(columns=kpi)
        phrases = ['Original problem has',
                   'Presolved problem has',
                   'Problem has',
                   'Objective value:',
                   'Gap:',
                   'Time (Wallclock seconds):']
        for file in files:
            infile = path_in+file
            with open(infile) as f:
                f = f.readlines()
            dict_ = {}
            for line in f:
                for phrase in phrases:
                    if phrase in line:
                        dict_.update({phrase: [float(s)
                                     for s in re.findall(r'-?\d+\.?\d*', line)]})
                        break

            name = file.split('.')[0]

            df_summary.loc[name, 'org_problem_bins'] = dict_['Original problem has'][0]
            df_summary.loc[name, 'pre_problem_bins'] = dict_['Presolved problem has'][0]
            df_summary.loc[name, 'rows'] = dict_['Problem has'][0]
            df_summary.loc[name, 'cols'] = dict_['Problem has'][1]
            df_summary.loc[name, 'obj'] = dict_['Objective value:'][0]
            if 'Gap:' in dict_:
                df_summary.loc[name, 'gap'] = dict_['Gap:'][0]
            else:
                df_summary.loc[name, 'gap'] = 0
            df_summary.loc[name, 'time'] = dict_['Time (Wallclock seconds):'][0]

        export = pd.ExcelWriter(path_out+'logs_summary'+'.xlsx',
                                engine='xlsxwriter')
        df_summary.to_excel(export, 'output', startrow=0,
                            startcol=0, float_format='%0.2f')
        export.save()

    if plot is True:
        kpi = ['nodes', 'tree', 'best_sol', 'best_pos', 'time', 'gap']
        phrases = ['best solution, best possible']
        for file in files:
            df_plot = pd.DataFrame(columns=kpi)
            found_line = []
            infile = path_in+file
            with open(infile) as f:
                f = f.readlines()

            for line in f:
                for phrase in phrases:
                    if phrase in line:
                        found_line.append(line)
                        break

            for line in range(len(found_line)):
                if(found_line[line].find('1e+050') < 0):
                    poi = [float(s)
                           for s in re.findall(r'-?\d+\.?\d*', found_line[line])]
                    df_plot.loc[line, 'nodes'] = poi[1]
                    df_plot.loc[line, 'tree'] = poi[2]
                    df_plot.loc[line, 'best_sol'] = poi[3]
                    df_plot.loc[line, 'best_pos'] = poi[4]
                    df_plot.loc[line, 'time'] = poi[5]
                    df_plot.loc[line, 'gap'] = abs(df_plot.loc[line, 'best_pos'] -
                                                   df_plot.loc[line, 'best_sol']) /\
                        abs(df_plot.loc[line, 'best_sol'])
            name = file.split('.')[0]
            if len(df_plot) < 2:
                print(name, ': nothing to plot')
            else:
                x = df_plot['time']
                y = df_plot['gap']
                fig = plt.figure(figsize=(16, 9))
                ax = fig.add_subplot(111)
                ax.plot(x, y, marker='o', linestyle='--', linewidth=1.2, label=name)
                plt.title(name, loc='left')
                plt.xlabel('time [sec]')
                plt.ylabel('gap [%]')
                plt.legend(loc='upper right')
                plt.grid()
                if not os.path.isdir(path_out+'plots/'):
                    os.makedirs(path_out+'plots/')
                fig.savefig(path_out+'plots/'+name)
