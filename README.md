EchoShield - Real-Time Noise Cancellation
A Python-based real-time noise cancellation application with a graphical user interface for removing background noise from audio streams.
Features
Real-time Processing: Stream-based callback architecture for minimal latency
Easy Toggle Control: Simple GUI button to start/stop noise cancellation
Device Selection: Support for custom input/output audio devices
Configurable Parameters: Adjustable sample rates and chunk sizes
Cross-Platform: Works on Windows with audio device routing support (VB-Cable compatible)
Requirements
Python 3.12+
See requirements.txt for dependencies
Installation
Method 1: Quick Install (Recommended)
pip install -r requirements.txt
Method 2: Manual Install
pip install sounddevice noisereduce numpy scipy matplotlib
Method 3: Virtual Environment (Isolated Setup)
# Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
Quick Start
Run the main application:

py pr.py
This launches the GUI with a Start/Stop Noise Cancellation button.

Usage
Main Application (pr.py)
Best for: Most users - callback-based streaming with GUI
Features: Responsive UI, real-time processing, minimal latency
Command: py pr.py
Device Selection (noise_canceller.py)
Best for: Custom audio device routing
Features: Interactive device selection, VB-Cable support
Command: py noise_canceller.py
List Devices (ec.py)
Best for: Finding audio device indices
Command: py ec.py
Output: Lists all available audio input/output devices
Basic Real-Time (echo.py / echoshield.py)
For: Testing and experimentation
echo.py - 1-second chunks
echoshield.py - 100ms chunks (lower latency)
Project Structure
EchoShield/
├── pr.py                      # Main application (callback-based, GUI)
├── echoshield.py             # Optimized real-time processing
├── noise_canceller.py        # Device selection with GUI
├── echo.py                   # Basic real-time processing
├── ec.py                     # Audio device enumeration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── echosheld-env/            # Virtual environment (optional)
How It Works
Architecture Evolution
ec.py - Device Discovery

Lists available audio devices
No processing, just enumeration
echo.py - Blocking Real-Time (Proof of Concept)

Record → Process → Playback loop
1-second chunks
Simple but higher latency
echoshield.py - Optimized Blocking (Better Latency)

100ms chunks for improved responsiveness
Still blocking I/O
noise_canceller.py - User Device Selection

Interactive device selection
Streaming with device routing
GUI toggle control
pr.py - Production-Ready (Callback-Based)

Most efficient implementation
Uses sd.Stream() with callback function
Lowest latency, best responsiveness
Recommended for production use
Technology Stack
Component	Purpose	Version
sounddevice	Audio I/O	0.5.5+
noisereduce	Noise reduction	3.0.3+
numpy	Numerical computing	2.2.5+
scipy	Scientific computing	1.15.2+
matplotlib	Visualization support	3.10.1+
tkinter	GUI framework	Built-in
Configuration
pr.py Settings
samplerate = 44100      # Audio sample rate (Hz)
blocksize = 1024        # Processing block size (samples)
channels = 1            # Mono audio
echoshield.py Settings
samplerate = 16000      # Lower for better noise handling
duration = 5            # Initial noise sample (seconds)
chunk_duration = 0.1    # 100ms chunks
Troubleshooting
"No Python at..." Error
Cause: Virtual environment pointing to missing Windows Store Python Solution: Use py pr.py instead of python pr.py

ModuleNotFoundError: No module named 'sounddevice'
Cause: Dependencies not installed Solution:

pip install -r requirements.txt
No Audio Devices Found
Cause: No default audio device configured Solution:

Run py ec.py to list devices
Use noise_canceller.py for manual device selection
Check system audio settings
GUI Window Not Appearing
Cause: Running with pythonw.exe (no console) Solution: Use py pr.py to show console and GUI

Audio Playback Issues
Cause: Output device misconfigured Solution:

Verify audio device with ec.py
Check audio levels in system settings
For virtual audio routing, install VB-Cable
Advanced Usage
Virtual Audio Routing (Windows)
For routing audio between applications:

Install VB-Cable: Download from VB-Audio website
Run noise_canceller.py
Select "CABLE Input" as output device
Other applications can now read from "CABLE Output"
Custom Device Selection
Edit pr.py to specify device indices:

device = (input_device_index, output_device_index)
with sd.Stream(device=device, ...):
    # Process audio
Performance Tuning
Increase blocksize for lower CPU usage (higher latency)
Decrease blocksize for lower latency (higher CPU usage)
Adjust samplerate (16kHz good for speech, 44.1kHz for music)
Known Limitations
Single-channel (mono) processing only
Requires pre-recorded noise sample for optimal results
Real-time processing latency ~100ms
CPU-intensive on older systems
Contributing
This project demonstrates:

Real-time audio processing in Python
GUI development with tkinter
Stream-based callback architecture
Virtual audio device routing
Feel free to extend with features like:

Multi-channel support
Advanced noise profiles
Volume level indicators
Recording/playback controls
License
Open source - feel free to use and modify.

Support
Getting Help
Check audio devices: py ec.py
Test with echo.py: py echo.py
Use noise_canceller.py for device selection
Check system audio settings and drivers
Common Issues
Crackling/Noise: Reduce blocksize or increase sample rate
No sound: Verify output device in Windows Sound settings
High CPU: Increase blocksize or reduce sample rate
EchoShield - Clean audio, on demand.
