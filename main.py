import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import colorchooser, simpledialog


SAMPLES = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050

audio = pyaudio.PyAudio()
plt.style.use('dark_background')
high = '#FF0000'
low = '#0000FF'
audBranch = 'all'

def selectColour():
    global high, low
    high = colorchooser.askcolor(title = 'Select High Colour')[1] or high
    low = colorchooser.askcolor(title = 'Select Low Colour')[1] or low

def selectAudBranch():
    global audBranch
    audBranch = simpledialog.askstring('Audio Branch', 'Enter the audio branch to display (all, left, right): ').lower()

def configure():
    root = tk.Tk()
    root.withdraw()
    selectColour()
    selectAudBranch()

def process(data):
    audData = np.frombuffer(data, dtype = np.int16)
    fft = np.fft.fft(audData, n = SAMPLES * 2)
    freqs = np.fft.fftfreq(len(fft), 1 / RATE)
    mags = np.abs(fft[:len(fft) // 2])

    if audBranch == 'bass':
        mags = mags[(freqs >= 20) & (freqs <= 250)]
    elif audBranch == 'mid':
        mags = mags[(freqs > 250) & (freqs <= 2000)]
    elif audBranch == 'treble':
        mags = mags[freqs > 2000]
    return (mags + 1e-6)

stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = SAMPLES)

figure, axis = plt.subplots()
X = np.linspace(0, RATE / 2, SAMPLES * 2 // 2)
y = np.zeros(SAMPLES * 2 // 2)
line, = axis.plot(X, y, color = low)
fill = axis.fill_between(X, y, color = low, alpha = 0.5)
axis.set_xlim(0, RATE / 2)
axis.set_ylim(0, 1000)

fill = None

def update(frame):
    global maxY, fill
    data = stream.read(SAMPLES)
    mags = process(data)
    line.set_ydata(mags)
    axis.set_ylim(0, np.max(mags) * 1.1)
    if fill is not None:
        for collection in axis.collections:
            collection.remove()
    fill = axis.fill_between(X, 0, mags, color = line.get_color(), alpha = 0.5)

    axis.set_yticks([])
    axis.set_yticklabels([])
    axis.set_xticks([])
    axis.set_xticklabels([])

    intensity = np.max(mags)
    normalised = np.clip((intensity / 32768), 0, 1)
    if normalised > 1.0:
        print(normalised)
    color = interpolate(low, high, normalised)
    line.set_color(color)
    
    return line,

def interpolate(low, high, value):
    low = np.array(list(int(low[i : (i + 2)], 16) for i in (1, 3, 5)))
    high = np.array(list(int(high[i : (i + 2)], 16) for i in (1, 3, 5)))
    interpolated = (high - low) * value + low
    return tuple(interpolated.astype(float) / 255.0)

if __name__ == '__main__':
    configure()
    animation = FuncAnimation(figure, update, interval = 25)
    plt.show()