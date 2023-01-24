import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import blackman
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp


def plot_signal(X, Y, xlabel, ylabel, title):
    plt.figure()
    plt.plot(X, Y)
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

if __name__ == "__main__":
    total = len(sys.argv)
    cmdargs = str(sys.argv)


    f, y_signal = wavfile.read('./hearth_signal.wav')
    T = 1.0/f
    N = len(y_signal)
    N_fft = N//2
    t = np.linspace(0,N*T,N)

    # -----------------------------------------------------
    # Plot time-domain
    plot_signal(t, y_signal,"Time [s]","Amplitude", "Time-domain heartbeat signal")
    # plt.show()

    y_fft = fft(y_signal)
    y_fft = y_fft[0:N_fft]
    x_fft = fftfreq(N, 1/f)[:N_fft]

    # -----------------------------------------------------
    # Plot frequency-domain
    plot_signal(x_fft, 2.0/N * np.abs(y_fft[:N_fft]),"Frequency [Hz]","Amplitude", "Frequency-domain heartbeat signal")
    # plt.show()

    # -----------------------------------------------------
    # Bandpass
    # f_1 = 1.5
    # f_2 = 2.3
    f_11 = 40
    f_12 = 70
    f_21 = 85
    f_22 = 110
    f_31 = 140
    f_32 = 160
    deltaF = x_fft[-1] / N_fft
    f_11_index = int(f_11//deltaF)
    f_12_index = int(f_12//deltaF)
    f_21_index = int(f_21//deltaF)
    f_22_index = int(f_22//deltaF)
    f_31_index = int(f_31//deltaF)
    f_32_index = int(f_32//deltaF)
    y_fft[0:f_11_index] = 0
    y_fft[f_12_index:f_21_index] = 0
    y_fft[f_22_index:f_31_index] = 0
    y_fft[f_32_index:-1] = 0
    y_fft[-1] = 0    


    # -----------------------------------------------------
    # Plot frequency-domain after filtration
    plot_signal(x_fft, 20*np.log10(np.abs(y_fft[:N_fft])),"Frequency [Hz]","Amplitude", "Frequency-domain heartbeat signal after filter")
    # plt.show()

    y_filtered = ifft(y_fft,axis=0)

    print(f"y_filtered = {y_filtered}")    
    print(f"y_filtered.size = {y_filtered.size}")    
    print(f"t.size = {t.size}")    

    # -----------------------------------------------------
    # Plot time-domain after filtration
    plot_signal(t[:t.size//2], y_filtered,"Time [s]","Amplitude", "Time-domain heartbeat signal after filter")
    # plt.show()

    # -----------------------------------------------------
    # HearthPy process for unfiltered
    a ,b = hp.process(y_signal, f, report_time=True)
    hp.plotter(a,b)
    # plt.show()

    # -----------------------------------------------------
    # HearthPy process after filtration

    beats_unfiltered = 0
    for i in range(1,len(y_filtered)):
        if y_filtered[i] > 0 and y_filtered[i-1] < 0 :
            beats_unfiltered = beats_unfiltered + 1
    print("BPM for filtered signal: ", beats_unfiltered * 3 )
    a ,b = hp.process(y_filtered, f, report_time=True)
    hp.plotter(a,b)
    plt.show()


    y_filtered = sp.real(y_filtered)
    y_filtered_int16_scaled = sp.int16(y_filtered / sp.absolute(y_filtered).max() * 32767)
    y_filtered_int16 = sp.int16(y_filtered)

    # wavfile.write("filtered_signal_float.wav", f//2, y_filtered)
    wavfile.write("filtered_signal_int16_scaled.wav", f//2, y_filtered_int16_scaled)
    wavfile.write("filtered_signal_int16.wav", f//2, y_filtered_int16)
