# Training the Acoustic Model

## Workflow Summary
1. **Prepare the Speech Corpus**: Preprocess the text transcripts by splitting words into individual letters.
2. **Create the G2G Pronunciation Dictionary**: Map each letter to itself in the dictionary.
3. **Train the Acoustic Model**: Use the Speech Corpus and the G2G Pronunciation Dictionary to train the model.
4. **Align the Corpus**: Use the trained Acoustic Model to align the text to the speech.
5. **Post-Processing**: Adjust the TextGrid alignments to include necessary punctuation marks.

## Step 1: Prepare the Speech Corpus

### Speech Corpus Directory Structure
```
speech_corpus_directory/
│
├── speaker1/
│   ├── recording1.wav
│   ├── recording1.lab
│   ├── recording2.wav
│   └── recording2.lab
│
├── speaker2/
│   ├── recording3.wav
│   └── recording3.lab
│   ...

```

### Audio Files
- Ensure all audio files are in `.wav` format, preferably at 16kHz.
- Preprocess the corresponding text transcripts by splitting the words into individual letters.

### Example:
Original Text:
```
அதற்குத் தகுந்தபடி, ஏதாவது கொஞ்சம் பேசி, வேஷம் போட்டால் போகிறது
```

Preprocessed Text:
```
அ த ற ் க ு த ் த க ு ந ் த ப ட ி , ஏ த ா வ த ு க ொ ஞ ் ச ம ் ப ே ச ி , வ ே ஷ ம ் ப ோ ட ் ட ா ல ் ப ோ க ி ற த ு .
```

## Step 2: Prepare the Pronunciation Dictionary
Create a G2G Pronunciation Dictionary where each letter maps to itself.

### Pronunciation Dictionary File Structure
```
[Letter 1]-[space]-[space]-[Letter 1] 
[Letter 2]-[space]-[space]-[Letter 2] 
```

### Example:
```
அ  அ
ஆ  ஆ
இ  இ
...  ...
```
## Step 3: Validate the Corpus and Train the Acoustic Model

### Validation Syntax:
```
mfa validate [path_to_speech_corpus] [path_to_dictionary_file]
```
### Training Syntax:
```
mfa train [path_to_speech_corpus] [path_to_dictionary_file] [output_path]
```

### Example:
```
mfa train --clean --phone_set UNKNOWN --use_mp -j 16 --single_speaker ~/path/to/speech_corpus ~/path/to/Tamil_Dictionary_g2g.txt ~/path/to/Tamil_Acoustic_Model.zip
```
#### Options:
--clean: Clears the cache of previous runs.<br/>
--phone_set UNKNOWN: Since phonemes are defined as graphemes.<br/>
--use_mp: Enables multi-processing.<br/>
-j 16: Specifies the number of cores to use. Here, it is 16.<br/>
--single_speaker: Indicates that the corpus is from a single speaker.

### Acoustic Model Directory Structure
```
acoustic_model_directory/
│
├── final.alimdl        # Alignment model file
├── final.mdl           # Final model file
├── lda.mat             # Linear Discriminant Analysis matrix
├── meta.json           # Metadata file containing model information
├── phone_lm.fst        # Phone-level language model in FST format
├── phone_pdf.counts    # Phone PDF counts file
├── phones.txt          # Phone list
├── rules.yaml          # Rules file
└── Tree                # Decision tree file

```
