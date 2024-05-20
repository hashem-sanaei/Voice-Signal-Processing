# Voice-Signal-Processing
This repository contains a Python script for processing a voice signal using Fourier transform techniques. The script reads an audio file, applies a low-pass filter by zeroing out small Fourier coefficients, and saves the processed signal. Additionally, it provides a visualization of the original, processed, and difference signals.

## Features

- Read and process an audio signal
- Apply Fourier transform and low-pass filtering
- Save the processed audio signal
- Visualize the original, processed, and difference signals

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/voice-signal-processing.git
   cd voice-signal-processing
   ```

2. Install the required Python packages:

   ```sh
   pip install numpy scipy matplotlib
   ```

## Usage

1. Place your original voice signal file named `original_voice.wav` in the repository directory.

2. Run the script to process the voice signal:

   ```sh
   python process_voice.py
   ```

3. The processed voice signal will be saved as `processed_voice.wav`.

4. To visualize the signals, run the visualization script:

   ```sh
   python visualize_signals.py
   ```

## Script Details

### `process_voice.py`

This script reads an audio file, applies a Fourier transform, filters out small coefficients, and saves the processed audio.

```python
import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft, ifft

# Read the voice signal
rate, data = wav.read("original_voice.wav")
data = data.flatten()  # Flatten the array

# Perform Fourier transform
voice_fft = fft(data)

# Zeroing out small coefficients (simple low-pass filter)
threshold = 1000
voice_fft[np.abs(voice_fft) < threshold] = 0

# Perform inverse Fourier transform
processed_voice_signal = ifft(voice_fft).real

# Save the processed voice signal
wav.write("processed_voice.wav", rate, processed_voice_signal.astype(np.int16))
```

### `visualize_signals.py`

This script reads the original and processed audio files, calculates the difference signal, and plots all three signals for comparison.

```python
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Read the original and processed voice signals
rate, original_data = wav.read("original_voice.wav")
rate, processed_data = wav.read("processed_voice.wav")

# Flatten the data arrays
original_data = original_data.flatten()
processed_data = processed_data.flatten()

# Calculate the difference signal
difference_signal = original_data - processed_data

# Plot original, processed, and difference voice signals
plt.figure(figsize=(18, 6))

# Original voice signal
plt.subplot(1, 3, 1)
plt.plot(original_data)
plt.title("Original Voice Signal")

# Processed voice signal
plt.subplot(1, 3, 2)
plt.plot(processed_data)
plt.title("Processed Voice Signal")

# Difference signal
plt.subplot(1, 3, 3)
plt.plot(difference_signal)
plt.title("Difference Signal")

plt.tight_layout()
plt.show()
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NumPy](https://numpy.org/)
- [SciPy](https://www.scipy.org/)
- [Matplotlib](https://matplotlib.org/)

