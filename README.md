# MFA Implementation: Aligning a Language from Scratch

## Overview
This project outlines the process of aligning a speech corpus with corresponding text transcripts from scratch, focusing on letter-wise alignment rather than the more common word-wise alignment. The approach replaces the traditional Grapheme-to-Phoneme (G2P) process with a Grapheme-to-Grapheme (G2G) process.

### Project Components
- **Speech Corpus**: Contains audio files and corresponding text transcripts.
- **Pronunciation Dictionary**: Custom dictionary mapping each grapheme to itself.
- **Acoustic Model**: A model trained using the Speech Corpus and G2G Pronunciation Dictionary.

### Directory Structure

#### Speech Corpus
+-- speech_corpus_directory <br/>
| +-- speaker1 <br/>
| --- recording1.wav <br/>
| --- recording1.lab <br/>
| --- recording2.wav <br/>
| --- recording2.lab <br/>
| +-- speaker2 <br/>
| --- recording3.wav <br/>
| --- recording3.lab <br/>
| --- ...


#### Pronunciation Dictionary
[Letter 1]-[space]-[space]-[Letter 1] <br/>
[Letter 2]-[space]-[space]-[Letter 2] <br/>
...


#### Acoustic Model
+-- acoustic_model_directory <br/>
| --- final.alimdl <br/>
| --- final.mdl <br/>
| --- lda.mat <br/>
| --- meta.json <br/>
| --- phone_lm.fst <br/>
| --- phone_pdf.counts <br/>
| --- phones.txt <br/>
| --- rules.yaml <br/>
| --- Tree


### Workflow Summary
1. **Prepare the Speech Corpus**: Preprocess the text transcripts by splitting words into individual letters.
2. **Create the G2G Pronunciation Dictionary**: Map each letter to itself in the dictionary.
3. **Train the Acoustic Model**: Use the Speech Corpus and the G2G Pronunciation Dictionary to train the model.
4. **Align the Corpus**: Use the trained Acoustic Model to align the text to the speech.
5. **Post-Processing**: Adjust the TextGrid alignments to include necessary punctuation marks.

### Tools and Dependencies
- **Python**: For preprocessing scripts.
- **Montreal Forced Aligner (MFA)**: For validation, training, and alignment.
- **Praat**: For analyzing TextGrid files.

### References
- **MFA Documentation**: https://github.com/MontrealCorpusTools/mfa-models
- **Praat Software**: https://www.fon.hum.uva.nl/praat/

For more detailed instructions, refer to `training.md` and `inference.md`.
