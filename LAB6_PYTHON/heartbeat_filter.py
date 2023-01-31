import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import blackman
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp
from scipy.signal import butter
from scipy.signal import lfilter
from scipy.signal import filtfilt
from scipy.signal import find_peaks
from scipy.signal import find_peaks_cwt

def plot_signal(X, Y, xlabel, ylabel, title):
    plt.figure()
    plt.plot(X, Y)
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


def moving_average(signal, f):
    averaged = signal.copy()
    window_size = round(0.150 * f)
    sum = 0

    for i in range(signal.size):
        sum += signal[i]/window_size
        # To ensure that average will be calculated only for window (subtract too old samples)
        if i > window_size:
            sum -= signal[i-window_size]/window_size
        averaged[i] = sum

    averaged = averaged/averaged.max()
    return averaged


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter(order, [lowcut, highcut], fs=fs, btype='bandpass')
    y = lfilter(b, a, data)
    y = y/y.max()
    return y


if __name__ == "__main__":
    total = len(sys.argv)
    cmdargs = str(sys.argv)

    # ----------------------------------------------------------------------------------------------------------
    # Time-domain
    f, y_signal = wavfile.read('./hearth_signal.wav')
    # f, y_signal = wavfile.read('./LAB6_PYTHON/hearth_signal.wav')
    T = 1.0/f
    N = len(y_signal)
    N_fft = N//2
    t = np.linspace(0, N*T, N)

    plot_signal(t, y_signal, "Time [s]",
                "Amplitude", "Time-domain heartbeat signal")
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # Frequency-domain
    y_fft = fft(y_signal)
    y_fft = y_fft[0:N_fft]
    x_fft = fftfreq(N, 1/f)[:N_fft]

    plot_signal(x_fft, np.abs(y_fft[:N_fft]), "Frequency [Hz]",
                "Amplitude", "Frequency-domain heartbeat signal")
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # Bandpass filter
    F_low = 80
    F_high = 220
    y_filtered = butter_bandpass_filter(y_signal,
                                        lowcut=F_low,
                                        highcut=F_high,
                                        fs=f,
                                        order=5)
    y_filtered_fft = fft(y_filtered)

    plot_signal(x_fft, np.abs(y_filtered_fft[:N_fft]), "Frequency [Hz]",
                "Amplitude", "Frequency-domain heartbeat signal after filter")
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # Plot time-domain after filtration
    plot_signal(t, y_filtered, "Time [s]", "Amplitude",
                "Time-domain heartbeat signal after filter")
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # HearthPy process for unfiltered
    a, b = hp.process(y_signal, f, report_time=True)
    hp.plotter(a, b)
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # HearthPy process after filtration
    a, b = hp.process(y_filtered, f, report_time=True)
    hp.plotter(a, b)
    # plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # Both signals compared
    plt.figure()
    plt.plot(t, y_signal, label="Before filtering")
    plt.plot(t, y_filtered*32768, label="After filtering")
    plt.grid()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.title("Both signal comparison")


    # ----------------------------------------------------------------------------------------------------------
    # Heartbeat analysis without external library
    y_processed = y_filtered**2
    y_processed = y_processed/y_processed.max()
    plot_signal(t, y_processed, "Time [s]", "Amplitude",
                "Processed signal")
    # plt.show()

    y_ave = moving_average(y_processed, f)
    plot_signal(t, y_ave, "Time [s]", "Amplitude",
                "Averaged signal")
    # plt.show()

    peaks_id, _ = find_peaks(y_ave, distance=0.45*f)#, prominence=30)
    peaks_time = np.take(t, peaks_id)
    peaks_value = np.take(y_ave, peaks_id)
    minute_scale = 60/(t.size/f)
    print(f"bpm: {peaks_time.size*minute_scale}")
    plot_signal(t, y_ave, "Time [s]", "Amplitude",
                "Averaged signal with peaks")
    plt.scatter(peaks_time, peaks_value, label="Peaks", c="red")
    plt.show()

    # ----------------------------------------------------------------------------------------------------------
    # Save to .wav file
    y_filtered = sp.real(y_filtered)
    y_normalized = y_filtered / sp.absolute(y_filtered).max() * 32767
    y_filtered_int16_scaled = sp.int16(y_normalized)

    wavfile.write("filtered_signal_int16_scaled.wav",
                  f//2, y_filtered_int16_scaled)
