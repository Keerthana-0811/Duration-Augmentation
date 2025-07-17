# Duration Augmentation 
This script applies **random speed (duration) changes** to `.wav` audio files using the `librosa` library. It creates time-stretched versions of each file, helping augment datasets for ASR or speech-related ML tasks.

---

# What It Does
- Loads `.wav` audio files from an input folder
- Applies a random speed change between 0.85× and 1.5×
- Uses `librosa.effects.time_stretch()` to modify duration
- Saves the augmented files to a new output folder

# Folder Structure
duration-augmentation/
- duration_augmentation.py # Python script for time-stretching-
- README.md # This documentation
- .gitignore # Optional, to ignore .wav or temp files


# Setup Instructions
1. Install Required Packages

```bash
pip install librosa soundfile numpy
```
2.Modify Input and Output Paths
- input_folder = "/path/to/input/folder"
- output_folder = "/path/to/output/folder"

3.Optional Parameters
- sample_rate: You can adjust this if needed (default = 16000)
- Speed range is currently set between 0.85 and 1.5 (can be changed via np.random.uniform())

 # Run the Script
    python duration_augmentation.py
 # output will be like:
- CM9_001.wav: speed_change = 1.32
- CM9_002.wav: speed_change = 0.97

 # Output files will be saved like:
 - speed_CM9_001.wav
 - speed_CM9_002.wav

 # License
 This script is provided for academic and research use. The librosa and soundfile libraries     are under their respective licenses.

 # Acknowledgements
  - librosa
  - soundfile
 




    

 







