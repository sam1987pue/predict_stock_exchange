import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import glob
import numpy as np
import pandas as pd

stockstats_files = [f for f in glob.glob("*.csv") if not "TR_" in f ]
TR_files = [f for f in glob.glob("*.csv") if "TR_" in f ]


class Get_FIGURES:
    def TR_figures(self):
        for line in TR_files:
            data1 = pd.DataFrame.from_csv(line)
            data1[['close', '42d', '252d']].plot(grid=True, figsize =(8, 5))
            plt.savefig(line+'_2TR.png')

    def stockstats_figures(self):
        for line in stockstats_files:
            print line
            try:
                faname = cbook.get_sample_data(line, asfileobj=False)
                faname = faname[71:]
                plt.style.use("Solarize_Light2")
                plt.plotfile(faname, ('date','30','70','rsi_12'), subplots=False)
                plt.savefig(line+'_rsi.png')
                # plt.plotfile(faname, ('date','macdh','macd','macds'), plotfuncs={'macdh': 'bar'}, subplots=False)
                # plt.savefig(line+'_macd.png')
            except:
                pass

def main():
	column = Get_FIGURES()
	column.TR_figures()
	column.stockstats_figures()


if  __name__ =='__main__':
    main()
