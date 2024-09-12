# How To Post-Process TextGrids
We post-process TextGrids because MFA removes all the punctuations from the final alignment in training. In order to add back the punctuations to the TextGrids, we can do so by following the steps given below.

## Sample Directory Structure
```
textgrid-postprocessing/
│
├── process_textgrids.py        # The main script file
├── example_data/               # Sample directories for TextGrid and transcription files
│   ├── textgrids/              # TextGrid files (.TextGrid)
│   └── transcriptions/         # Transcription files (.txt)
├── output/                     # Output directory where processed TextGrids will be saved
└── README.md                   # Documentation (optional but recommended)
```

## Prerequisites
Make sure you have the following installed:
- `tgt` library (for reading and writing TextGrid files)
  
You can install the required library with:
`pip install tgt`

## Usage
- Place your .TextGrid files in the textgrids folder.
- Place the corresponding transcription .txt files in the transcriptions folder. Make sure the transcription files have the same name as their respective TextGrid files.
- To run the script, use the following command:
`
python process_textgrids.py
`

Example:
```
python process_textgrids.py \
  --textgrid_directory=example_data/textgrids \
  --transcription_directory=example_data/transcriptions \
  --output_directory=output
```

The processed TextGrids with punctuation will be saved in the output folder.


