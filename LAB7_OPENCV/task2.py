import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import blackman
import cv2 as cv


def plot_signal(X, Y, xlabel, ylabel, title):
    plt.figure()
    plt.plot(X, Y)
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

if __name__ == "__main__":
    a = 2


