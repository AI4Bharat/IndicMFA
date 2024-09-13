# IndicMFA: Forced Aligners for Indian Languages

## Overview
We align speech corpora with corresponding text transcripts from scratch, focusing on letter-wise alignment rather than the more common word-wise alignment. In our approach, we replace the traditional Grapheme-to-Phoneme (G2P) process with a Grapheme-to-Grapheme (G2G) process.

### Release
We release the following components -
- **Pronunciation Dictionary**: Custom dictionary mapping each grapheme to itself. Contains all the letters of the language
- **Acoustic Model**: A model trained using the Speech Corpus and G2G Pronunciation Dictionary that extracts features and predicts phonemes.

Additionally, you will need a **speech corpus**: which contains audio files and corresponding text transcripts[processed].

Find the releases of all 22 Indian Languages at : https://github.com/AI4Bharat/IndicMFA/releases

The Training Details for all the languages in the release can be found in the table below:

| Language   | Hours of data | IndicTTS | IndicVoices-R | Limmits | GoogleCrowdSourced | Rasa |
|------------|---------------|----------|---------------|---------|--------------------|------|
| Assamese   | 302.86        | Y        | Y             |         |                    | Y    |
| Bengali    | 313.32        | Y        | Y             | Y       |                    | Y    |
| Bodo       | 222.53        | Y        | Y             |         |                    | Y    |
| Dogri      | 91.52         |          | Y             |         |                    | Y    |
| Gujarati   | 42.9          | Y        | Y             |         |                    |      |
| Hindi      | 255.33        | Y        | Y             | Y       |                    |      |
| Kannada    | 193.81        | Y        | Y             | Y       | Y                  | Y    |
| Kashmiri   | 90.53         |          | Y             |         |                    |      |
| Konkani    | 85.69         |          | Y             |         |                    |      |
| Maithili   | 200.81        |          | Y             |         |                    |      |
| Malayalam  | 197.08        | Y        | Y             |         |                    | Y    |
| Manipuri   | 55.19         | Y        | Y             |         |                    |      |
| Marathi    | 212.58        | Y        | Y             | Y       |                    | Y    |
| Nepali     | 217.04        |          | Y             |         |                    | Y    |
| Odia       | 131.72        | Y        | Y             |         |                    |      |
| Punjabi    | 123.62        | Y        | Y             |         |                    |      |
| Sanskrit   | 76.36         |          | Y             |         |                    |      |
| Santali    | 121.84        |          | Y             |         |                    |      |
| Tamil      | 300.48        | Y        | Y             |         |                    | Y    |
| Telugu     | 261.77        | Y        | Y             | Y       | Y                  |      |
| Urdu       | 101.79        |          | Y             |         |                    |      |
| Sindhi     | 10.31         |          | Y             |         |                    |      |


### Use MFA
To install and use the MFA software. Follow the steps at : https://montreal-forced-aligner.readthedocs.io/en/latest/index.html 
In Order to get details on how to install MFA and more, go to `Montreal-Forced-Aligner-Docs/README.md` <br/>
For more detailed instruction on implementation, refer to `training.md` and `inference.md`.

### Tools and Dependencies
- **Python**: For preprocessing scripts.
- **Montreal Forced Aligner (MFA)**: For validation, training, and alignment.
- **Praat**: For analyzing TextGrid files.

### References
- **MFA Documentation**: https://github.com/MontrealCorpusTools/mfa-models
- **Praat Software**: https://www.fon.hum.uva.nl/praat/

  
