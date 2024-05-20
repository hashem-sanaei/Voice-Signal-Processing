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
