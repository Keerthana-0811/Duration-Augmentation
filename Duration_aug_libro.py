#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:53:06 2025

@author: vksit
"""

import os
import numpy as np
import librosa
import soundfile as sf

# Set paths
input_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/0_Control/CM9"
output_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/Librosa_Augmented/Duration_Modification/Normal/CM9"
os.makedirs(output_folder, exist_ok=True)

# Target sample rate (or set to None to preserve original)
sample_rate = 16000

# Loop through audio files
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(input_folder, filename)

        # Load the audio
        y, sr = librosa.load(filepath, sr=sample_rate)

        # Apply random speed change
        speed_change = np.random.uniform(0.85, 1.5)
        print(f"{filename}: speed_change = {speed_change:.2f}")

        # Time stretch
        y_stretched = librosa.effects.time_stretch(y=y.astype('float64'), rate=speed_change)


        # Save stretched audio
        output_path = os.path.join(output_folder, f"speed_{filename}")
        sf.write(output_path, y_stretched, sr)

print("Duration transformation complete. Files saved to 'output_audio_duration_changed'.")
