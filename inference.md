# Inference: Aligning Text to Speech

## Align the Corpus

### Syntax:
```
mfa align [path_to_speech_corpus] [path_to_dictionary] [newly_trained_acoustic_model] [output_path]
```
### Example:
```
mfa align --clean -j 16 --use_mp --single_speaker --no_textgrid_cleanup ~/path/to/speech_corpus ~/path/to/Tamil_Dictionary_g2g.txt ~/path/to/Tamil_Acoustic_Model.zip ~/path/to/output_textgrids
```

### Options:
--clean: Clears the cache of previous runs.<br/>
--phone_set UNKNOWN: Since phonemes are defined as graphemes.<br/>
--use_mp: Enables multi-processing.<br/>
-j 16: Specifies the number of cores to use.<br/>
--single_speaker: Indicates that the corpus is from a single speaker.<br/>
--no_textgrid_cleanup: Turns off post-processing of TextGrids to retain spacing.<br/>

## Post-Processing TextGrids
Python Script for Post-Processing
This script adds punctuation to the TextGrid alignments by replacing <eps> with appropriate punctuation marks.

```
import os
import tgt

def read_transcription(transcription_path):
    with open(transcription_path, 'r', encoding='utf-8') as file:
        transcription = file.read().strip()
    return transcription

def tokenize_transcription(transcription):
    return transcription.split()

def find_punctuation_positions(tokens):
    positions = []
    for i, token in enumerate(tokens):
        if token in [',', '.']:
            positions.append((i, token))
    return positions

def replace_eps_with_punctuation(textgrid_path, tokens, punct_positions, output_path):
    tg = tgt.io.read_textgrid(textgrid_path)
    
    words_tier = None
    for tier in tg.tiers:
        if tier.name.lower() == "words":
            words_tier = tier
            break
    
    if not words_tier:
        raise ValueError("No 'words' tier found in the TextGrid.")
    
    interval_texts = [interval.text for interval in words_tier.intervals]
    
    for i, interval in enumerate(words_tier.intervals):
        if interval.text == '<eps>':
            for pos, punct in punct_positions:
                before_punct = tokens[max(0, pos-2):pos]
                after_punct = tokens[pos+1:min(len(tokens), pos+3)]
                
                before_eps = interval_texts[max(0, i-2):i]
                after_eps = interval_texts[i+1:min(len(interval_texts), i+3)]
                
                if before_punct == before_eps and after_punct == after_eps:
                    interval.text = punct
                    break
    
    tgt.io.write_to_file(tg, output_path, format='long')

def process_textgrids(textgrid_directory, transcription_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(textgrid_directory):
        if filename.endswith('.TextGrid'):
            textgrid_path = os.path.join(textgrid_directory, filename)
            transcription_filename = filename.replace('.TextGrid', '.txt')
            transcription_path = os.path.join(transcription_directory, transcription_filename)
            
            if os.path.exists(transcription_path):
                transcription = read_transcription(transcription_path)
                tokens = tokenize_transcription(transcription)
                punct_positions = find_punctuation_positions(tokens)
                
                output_path = os.path.join(output_directory, filename)
                try:
                    replace_eps_with_punctuation(textgrid_path, tokens, punct_positions, output_path)
                except Exception as e:
                    print(f"Error processing TextGrid '{textgrid_path}': {e}")
            else:
                print(f"Transcription file '{transcription_path}' not found for TextGrid '{textgrid_path}'")

# Example usage:
textgrid_directory = r"path_to_textgrid_directory"
transcription_directory = r"path_to_transcription_directory"
output_directory = r"path_to_output_directory"

process_textgrids(textgrid_directory, transcription_directory, output_directory)
```

## Analyze the TextGrids
Use Praat software to visualize the aligned audio and text.
Load the .wav and corresponding .TextGrid files to check the alignment.

## Final Notes
Ensure that the alignment and post-processing steps are correctly followed to achieve the desired accuracy in text-to-speech alignment.

These files should provide a comprehensive guide to the project, covering the essential steps and commands for both training and inference. Let me know if you need any further adjustments or additions!



