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
    print(f"N = {N}")
    print(f"T = {T}")
    xf = fftfreq(N, T)[:N//2]
    print(f"xf.shape = {xf.shape}")
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
    fp = 50000
    Tp = 1/fp

    # ------------------------------------------------------------------------
    # Without DMA
    t_1 = df['sample_id'].to_numpy()
    t_10 = df['sample_id'].to_numpy()
    t_40 = df['sample_id'].to_numpy()

    print(f"t_1 = {t_1}")
    y_1 = df['ADC_1kHz'].to_numpy()
    y_10 = df['ADC_10kHz'].to_numpy()
    y_40 = df['ADC_40kHz'].to_numpy()

    plot_data(t_1, y_1, "Time [ms]", "Voltage [V]", "ADC for 1kHz")
    plot_data(t_10, y_10, "Time [ms]", "Voltage [V]", "ADC for 10kHz")
    plot_data(t_40, y_40, "Time [ms]", "Voltage [V]", "ADC for 40kHz")
    plt.show()

    calculate_fft(N, Tp, y_1, "FFT for 1kHz")
    calculate_fft(N, Tp, y_10, "FFT for 10kHz")
    calculate_fft(N, Tp, y_40, "FFT for 40kHz")
    
    # ------------------------------------------------------------------------
    # With DMA
    N_dma = 300
    fp = 50000
    Tp = 1/fp
    dma_t_1 = df['DMA_sample_id'].to_numpy()[0:N_dma]
    dma_t_10 = df['DMA_sample_id'].to_numpy()[0:N_dma]
    dma_t_40 = df['DMA_sample_id'].to_numpy()[0:N_dma]

    dma_y_1 = df['DMA_1kHz'].to_numpy()[0:N_dma]
    dma_y_10 = df['DMA_10kHz'].to_numpy()[0:N_dma]
    dma_y_40 = df['DMA_40kHz'].to_numpy()[0:N_dma]

    plot_data(dma_t_1, dma_y_1, "Time [ms]", "Voltage [V]", "ADC for 1kHz")
    plot_data(dma_t_10, dma_y_10, "Time [ms]", "Voltage [V]", "ADC for 10kHz")
    plot_data(dma_t_40, dma_y_40, "Time [ms]", "Voltage [V]", "ADC for 40kHz")
    plt.show()

    calculate_fft(N_dma, Tp, dma_y_1, "FFT for 1kHz")
    calculate_fft(N_dma, Tp, dma_y_10, "FFT for 10kHz")
    calculate_fft(N_dma, Tp, dma_y_40, "FFT for 40kHz")