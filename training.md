# Training the Acoustic Model

## Step 1: Prepare the Speech Corpus

### Audio Files
- Ensure all audio files are in `.wav` format, preferably at 16kHz.
- Preprocess the corresponding text transcripts by splitting the words into individual letters.

### Example:
Original Text:
அதற்குத் தகுந்தபடி, ஏதாவது கொஞ்சம் பேசி, வேஷம் போட்டால் போகிறது

Preprocessed Text:
அ த ற ் க ு த ் த க ு ந ் த ப ட ி , ஏ த ா வ த ு க ொ ஞ ் ச ம ் ப ே ச ி , வ ே ஷ ம ் ப ோ ட ் ட ா ல ் ப ோ க ி ற த ு .

## Step 2: Prepare the Pronunciation Dictionary
Create a G2G Pronunciation Dictionary where each letter maps to itself.

### Example:
அ  அ
ஆ  ஆ
இ  இ
...  ...

## Step 3: Validate the Corpus and Train the Acoustic Model

### Validation Syntax:
mfa validate [path_to_speech_corpus] [path_to_dictionary_file]

### Training Syntax:
mfa train [path_to_speech_corpus] [path_to_dictionary_file] [output_path]

### Example:
mfa train --clean --phone_set UNKNOWN --use_mp -j 16 --single_speaker ~/path/to/speech_corpus ~/path/to/Tamil_Dictionary_g2g.txt ~/path/to/Tamil_Acoustic_Model.zip

#### Options:
--clean: Clears the cache of previous runs.<br/>
--phone_set UNKNOWN: Since phonemes are defined as graphemes.<br/>
--use_mp: Enables multi-processing.<br/>
-j 16: Specifies the number of cores to use. Here, it is 16.<br/>
--single_speaker: Indicates that the corpus is from a single speaker.
