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