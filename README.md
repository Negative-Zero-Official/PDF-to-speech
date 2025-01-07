>[!IMPORTANT]
>This README.md is AI generated.

# PDF Audio Reader

A Python-based application that converts the text from a PDF file into speech using text-to-speech (TTS) technology. The project is designed to read aloud PDF content and includes interactive features to control playback.

## Features

- **Read PDF Text**: Extracts text from PDF files and converts it into speech.
- **Playback Control**:
  - Press `Space` to pause/resume playback.
  - Press `Q` to stop playback.
- **Multi-threaded Playback**: Ensures smooth and responsive playback control.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.6+
- Required Python packages:
  - `pyttsx3`
  - `PyPDF2`
  - `keyboard`

You can install the dependencies using:
```bash
pip install pyttsx3 PyPDF2 keyboard
```

## How to Use

1. Clone this repository or download the source code.
2. Run the `Main.py` file:
   ```bash
   python Main.py
   ```
3. Enter the path to the PDF file when prompted.
4. Use the following controls during playback:
   - Press `Space` to pause or resume the playback.
   - Press `Q` to stop the playback completely.

## Project Structure

- `Main.py`: The main script that handles PDF reading and playback control.

## How It Works

1. The script reads the PDF file using `PyPDF2`.
2. Extracted text is split into sentences for better audio playback.
3. The `pyttsx3` library is used to convert text to speech.
4. Multi-threading ensures playback controls (pause/resume and stop) are responsive.

## Limitations

- Only supports text-based PDFs (scanned PDFs are not supported).
- Requires proper formatting of the PDF for optimal text extraction.

## Future Enhancements

- Implement a graphical user interface (GUI).
