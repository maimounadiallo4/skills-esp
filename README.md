# skills-esp

A small collection of GitHub Copilot skills and productivity scripts designed to help with academic writing, note-taking, content organization, and automatic transcription workflows.

## Overview

This repository brings together a set of custom skills and utilities for common workflows such as:

- formatting academic documents
- generating visual banners for Notion pages
- capturing and structuring notes for Notion
- recording and organizing session notes
- transcribing audio or video files with Whisper

## Repository contents

- `dgi-academic-formatter.skill` — a skill for formatting academic content in a cleaner, more structured style.
- `notion-banner-creator.skill` — a skill to generate themed banner content for Notion pages.
- `notion-note-taker.skill` — a skill for collecting and organizing notes in Notion.
- `obs-note-taker.skill` — a skill for capturing notes from OBS-related workflows.
- `transcription.py` — a Python script that transcribes media files using OpenAI Whisper.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/maimounadiallo4/skills-esp.git
cd skills-esp
```

### 2. Use the skills

The `.skill` files are intended to be used with GitHub Copilot skills or custom agent workflows. Copy them into your configured skill directory or use them in a GitHub Copilot environment that supports custom skills.

### 3. Run the transcription script

Install the required dependency:

```bash
pip install git+https://github.com/openai/whisper.git
```

Then update the file path in `transcription.py` and run:

```bash
python transcription.py
```

If you are using Google Colab, the script also includes a Drive-mount example for loading files from Google Drive.

## Example workflow

1. Record a lecture or meeting.
2. Transcribe the audio/video using Whisper.
3. Review or clean the generated transcript.
4. Use a skill to organize the content in Notion or create a formatted academic version.
5. Publish or share the final material in your preferred format.

## Notes

- This project is oriented toward productivity and automation workflows.
- Some files are tailored for French academic and note-taking use cases.
- The transcription script is especially useful for lecture capture and documentation tasks.

## License

This project does not currently declare a license. If you plan to share or reuse it publicly, consider adding an appropriate license file such as MIT or Apache 2.0.

## Future improvements

Potential additions include:

- a dedicated `requirements.txt` for Python dependencies
- usage examples for each skill
- screenshots or sample outputs
- a troubleshooting section
- localization for English/French documentation

