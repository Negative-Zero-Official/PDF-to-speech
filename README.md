>[!IMPORTANT]
>This README.md is AI generated.

# PDF Audio Reader

A Python-based application that converts the text from a PDF file into speech using text-to-speech (TTS) technology. The project is designed to read aloud PDF content and includes interactive features to control playback.

## Features

- **Read PDF Text**: Extracts text from PDF files and converts it into speech
- **Multiple Interface Options**:
  - Command Line Interface (CLI)
  - Graphical User Interface (GUI)
- **Playback Controls**:
  - CLI Version:
    - Press `Space` to pause/resume playback
    - Press `Q` to stop playback
  - GUI Version:
    - Click buttons to Play, Pause/Resume, and Stop
    - Easy file selection with Browse button
- **Multi-threaded Playback**: Ensures smooth and responsive playback control

## Requirements

To run this project, ensure you have the following installed:

- Python 3.6+
- Required Python packages:
  - `pyttsx3`
  - `PyPDF2`
  - `keyboard`
  - `tkinter` (usually comes with Python)

You can install the dependencies using:
```bash
pip install pyttsx3 PyPDF2 keyboard
```

## How to Use

1. Clone this repository or download the source code.
2. Run the `GUI.py` file:
   ```bash
   python GUI.py
   ```
3. Select PDF file when prompted.
4. Use the following controls during playback:
   - Press `Play` to begin the playback.
   - Press `Pause/Resume` to pause or resume the playback.
   - Press `Stop` to stop the playback completely.

## Project Structure

- `Main.py`: Core functionality and CLI interface
- `GUI.py`: Graphical user interface implementation

## How It Works

1. The script reads the PDF file using `PyPDF2`.
2. Extracted text is split into sentences for better audio playback.
3. The `pyttsx3` library is used to convert text to speech.
4. Multi-threading ensures playback controls (pause/resume and stop) are responsive.
5. Status updates are provided through console/GUI

## Limitations

- Only supports text-based PDFs (scanned PDFs are not supported).
- Requires proper formatting of the PDF for optimal text extraction.