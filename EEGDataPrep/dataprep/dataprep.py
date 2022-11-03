import os
import mne

# Plot raw data
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    raw.plot(duration=4)