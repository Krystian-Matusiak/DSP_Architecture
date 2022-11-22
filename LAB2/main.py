try:
    from cProfile import label
    import numpy as np
    import time
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.fft import fft, fftfreq
    import os
except:
    print("Something went wrong")


def plot_data(X, Y, xlabel, ylabel, title):
    global plot_index
    plt.figure(plot_index)
    plt.plot(X, Y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.axvline()
    plt.axhline()
    plt.title(title)
    plot_index = plot_index + 1

def calculate_fft(N, T, Y, title):
    yf = fft(Y)
    xf = fftfreq(N, T)[:N//2]
    plt.plot(xf, np.abs(yf[:N//2]))
    plt.title(title)
    plt.xlabel("f [Hz]")
    plt.ylabel("Mag of FFT")
    plt.show()

plot_index = 1
if __name__ == "__main__":
    df = pd.read_excel('sines.ods', engine='odf')
    print(df)

    N = 500
    f1 = 50000
    f2 = 50000
    f3 = 50000
    T1 = 1/f1
    T2 = 1/f2
    T3 = 1/f3

    # ------------------------------------------------------------------------
    # Without DMA
    t_1 = df['sample_id'].apply(lambda x: x*T1).to_numpy()
    t_10 = df['sample_id'].apply(lambda x: x*T2).to_numpy()
    t_40 = df['sample_id'].apply(lambda x: x*T3).to_numpy()

    y_1 = df['ADC_1kHz'].to_numpy()
    y_10 = df['ADC_10kHz'].to_numpy()
    y_40 = df['ADC_40kHz'].to_numpy()

    plot_data(t_1, y_1, "samples", "ADC value", "ADC for 1kHz")
    plot_data(t_10, y_10, "samples", "ADC value", "ADC for 10kHz")
    plot_data(t_40, y_40, "samples", "ADC value", "ADC for 40kHz")
    plt.show()

    calculate_fft(N, T1, y_1, "FFT for 1kHz")
    calculate_fft(N, T2, y_10, "FFT for 10kHz")
    calculate_fft(N, T3, y_40, "FFT for 40kHz")
    
    # ------------------------------------------------------------------------
    # With DMA
    N_dma = 300
    dma_t_1 = df['DMA_sample_id'].apply(lambda x: x*T1).to_numpy()[0:N_dma]
    dma_t_10 = df['DMA_sample_id'].apply(lambda x: x*T2).to_numpy()[0:N_dma]
    dma_t_40 = df['DMA_sample_id'].apply(lambda x: x*T3).to_numpy()[0:N_dma]

    dma_y_1 = df['DMA_1kHz'].to_numpy()[0:N_dma]
    dma_y_10 = df['DMA_10kHz'].to_numpy()[0:N_dma]
    dma_y_40 = df['DMA_40kHz'].to_numpy()[0:N_dma]

    plot_data(dma_t_1, dma_y_1, "samples", "ADC value", "ADC for 1kHz")
    plot_data(dma_t_10, dma_y_10, "samples", "ADC value", "ADC for 10kHz")
    plot_data(dma_t_40, dma_y_40, "samples", "ADC value", "ADC for 40kHz")
    plt.show()

    calculate_fft(N_dma, T1, dma_y_1, "FFT for 1kHz")
    calculate_fft(N_dma, T2, dma_y_10, "FFT for 10kHz")
    calculate_fft(N_dma, T3, dma_y_40, "FFT for 40kHz")