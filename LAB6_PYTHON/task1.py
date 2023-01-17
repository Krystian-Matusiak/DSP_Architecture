import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import blackman




if __name__ == "__main__":
    total = len(sys.argv)
    cmdargs = str(sys.argv)

    print(f"The total numbers of args passed to the script: {total}")
    print(f"Arg list: {cmdargs}")

    print(f"Script name: {str(sys.argv[0])}")
    print(f"First argument: {str(sys.argv[1])}")

    f, y_signal = wavfile.read('./hearth_signal.wav')
    T = 1.0/f
    N = y_signal.size
    N_fft = N//2
    t = np.linspace(0,N*T,N)

    # -----------------------------------------------------
    # Plot time-domain
    plt.figure()
    plt.plot(t, y_signal)
    plt.grid()
    plt.xlabel("time [s]")
    plt.ylabel("Amplitude")
    plt.title("Time-domain heartbeat signal")
    # plt.show()

    y_fft = fft(y_signal)
    y_fft = y_fft[0:N_fft]
    x_fft = fftfreq(N, 1/f)[:N_fft]

    # -----------------------------------------------------
    # Plot frequency-domain
    plt.figure()
    plt.plot(x_fft, 2.0/N * np.abs(y_fft[:N_fft]), '-b')
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title("Frequency-domain heartbeat signal")
    # plt.show()

    # -----------------------------------------------------
    # Bandpass
    f_1 = 120
    f_2 = 220
    deltaF1 = x_fft[-1] / N_fft
    deltaF2 = x_fft[-1] / N_fft
    f_1_index = int(f_1//deltaF1)
    f_2_index = int(f_2//deltaF2)
    y_fft[0:f_1_index] = 0
    y_fft[f_2_index:-1] = 0
    y_fft[-1] = 0    


    # -----------------------------------------------------
    # Plot frequency-domain after filtr
    plt.figure()
    plt.plot(x_fft, 2.0/N * np.abs(y_fft[:N_fft]), '-b')
    plt.grid()
    plt.xlabel("frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title("Frequency-domain heartbeat signal after filter")
    # plt.show()

    y_filtered = ifft(y_fft)

    print(f"y_filtered = {y_filtered}")    
    print(f"y_filtered.size = {y_filtered.size}")    
    print(f"t.size = {t.size}")    

    # -----------------------------------------------------
    # Plot time-domain after filter
    plt.figure()
    plt.plot(t[:t.size//2], y_filtered)
    plt.grid()
    plt.xlabel("time [s]")
    plt.ylabel("Amplitude")
    plt.title("Time-domain heartbeat signal after filter")
    plt.show()
