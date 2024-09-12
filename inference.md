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
We have a python Script for Post-Processing
This is used to add punctuation to the TextGrid alignments by replacing <eps> with appropriate punctuation marks.

The steps to run the script are in 
`
IndicMFA/TextGrids Post Processing/
`

## Analyze the TextGrids
Use Praat software to visualize the aligned audio and text.
Load the .wav and corresponding .TextGrid files to check the alignment.

## Final Notes
Ensure that the alignment and post-processing steps are correctly followed to achieve the desired accuracy in text-to-speech alignment.

These files should provide a comprehensive guide to the project, covering the essential steps and commands for both training and inference. Let me know if you need any further adjustments or additions!



