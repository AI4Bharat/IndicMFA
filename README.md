# IndicMFA: Forced Aligners for Indian Languages

## Overview
We align speech corpora with corresponding text transcripts from scratch, focusing on letter-wise alignment rather than the more common word-wise alignment. In our approach, we replace the traditional Grapheme-to-Phoneme (G2P) process with a Grapheme-to-Grapheme (G2G) process.

### Release
We release the following components -
- **Pronunciation Dictionary**: Custom dictionary mapping each grapheme to itself. Contains all the letters of the language
- **Acoustic Model**: A model trained using the Speech Corpus and G2G Pronunciation Dictionary that extracts features and predicts phonemes.

Additionally, you will need a **speech corpus**: which contains audio files and corresponding text transcripts[processed].

Find the releases of all 22 Indian Languages at : https://github.com/AI4Bharat/IndicMFA/releases

### Use MFA
In order to install and use the MFA software. Follow the steps at : https://montreal-forced-aligner.readthedocs.io/en/latest/index.html 

### Tools and Dependencies
- **Python**: For preprocessing scripts.
- **Montreal Forced Aligner (MFA)**: For validation, training, and alignment.
- **Praat**: For analyzing TextGrid files.

### References
- **MFA Documentation**: https://github.com/MontrealCorpusTools/mfa-models
- **Praat Software**: https://www.fon.hum.uva.nl/praat/

  
In Order to get details on how to install MFA and more, go to `Montreal-Forced-Aligner-Docs/README.md` <br/>
For more detailed instruction on implementation, refer to `training.md` and `inference.md`.
