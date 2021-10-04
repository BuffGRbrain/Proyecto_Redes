import random as rd
import matplotlib.pyplot as plt
import pandas as pd

#SampleRTT
#time


def ewma_calculation(csv,alpha=0.125):
    if not csv:
        SampleRTT = []
        time = []
        for i in range(200):
            SampleRTT.append(rd.randrange(150,351))
            time.append(i)
    else:
        csv0 = pd.read_csv(csv, usecols= ['RTT'])
        csv1 = pd.read_csv(csv, usecols= ['time'])

        csv2 = csv0.to_records(index=False)
        csv3 = csv1.to_records(index=False)

        SampleRTT = list(csv2)
        time = list(csv3)

    ewma = [SampleRTT[0]]
    for i in range(1,len(SampleRTT)):
        ewma.append((1-alpha)*ewma[i-1]+alpha*SampleRTT[i])
    plt.plot(time,SampleRTT, label = 'SampleRTT')
    plt.plot(time,ewma, label = 'EstimatedRTT')
    plt.xlabel('Time(s)')
    plt.ylabel('RTT (ms)')
    plt.legend()
    return ewma
ewma = ewma_calculation('test.csv')
print(ewma[:5])
