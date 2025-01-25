
# Audio Visualizer

## Description
This project is a real-time audio visualiser that reads audio data from a microphone for a selected audio branch (bass, mid, treble) and creates a dynamic, color-changing graph based on the intensity of different frequencies. The visualiser updates continuously, showing a graph that reflects the audio input, with customisation options for colors and audio focus.

## Tools and Libraries Used
- **Python**: The core programming language for this project.
- **Matplotlib**: Used for plotting and animating the audio visualization.
- **PyAudio**: A library for capturing live audio data from the microphone.
- **Tkinter**: Provides a simple graphical user interface (GUI) for the color selection and audio branch configuration part.
- **NumPy**: Used for processing and analysing the audio data using Fast Fourier Transform (FFT) to extract frequency magnitudes.

## Features
- **Color Customisation**: The user can choose a custom color scheme for high and low intensity frequencies.
- **Dynamic Visualisation**: The visualiser updates in real time with the intensity of the audio data, changing colors based on the volume of the frequencies.
- **Focus on Audio Branches**: The visualiser can focus on different parts of the audio spectrum (bass, midrange, treble) to highlight specific audio frequencies. 
> Note: These are indicated by 'left, all, right' in the program 

## How It Works
1. **Audio Capture**: The program uses the `PyAudio` library to capture real-time audio data from the microphone.
2. **FFT Processing**: The captured audio is processed using NumPy’s `np.fft.fft` to convert the audio into frequency data.
3. **Frequency Branches**: The program divides the frequency spectrum into different branches (bass, midrange, treble) based on user selection.
4. **Color Interpolation**: The color of the visualisation changes based on the intensity of the frequencies, with an interpolated color gradient between the chosen high and low colors.
5. **Real-time Update**: The visualization is continuously updated using Matplotlib's `FuncAnimation`, which redraws the plot as new audio data is captured and processed.

## How to Run
1. Clone this repository.
2. Install the necessary dependencies:
   ```bash
   pip install numpy matplotlib pyaudio tkinter
   ```
3. Run the script:
   ```bash
   python audio_visualiser.py
   ```
4. A window will open where you can select the audio source and color scheme. The visualisation will appear in real-time as audio is captured.

## Future Prospects
- **Add Support for Other Audio Sources**: Expand the visualiser to support additional audio sources, such as desktop audio (playing from your computer) and streaming services (Spotify or YouTube links).
- **Clean Audio for Smoother Visualisation**: Implement noise reduction and smoothening algorithms to improve the appearance of the visualisation, making it more stable and visually appealing.

## License
This project is licensed under the MIT License.
