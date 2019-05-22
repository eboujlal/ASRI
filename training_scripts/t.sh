#!/usr/bin/env bash


# DATA config
DATA="${HOME}/ASRI/dataset"
DEV="$DATA/dev.csv"
TRAIN="$DATA/train.csv"
TEST="$DATA/test.csv"
VALIDATED="$DATA/validated.csv"
INVALIDATED="$DATA/invalidated.csv"

# Deep Speech config
DEEPSPEECH_PATH="${HOME}/ASRI/libs/DeepSpeech"

# Language Models paths
KENLM="${HOME}/ASRI/libs/kenlm/build/bin"
LM_DIR="${HOME}/ASRI/lm"
OUTPUT_ALPHABETS="${LM_DIR}/alphabet.txt"
LM_TEXT="$LM_DIR/lm_text.txt"
LM_ARPA="$LM_DIR/lm.arpa"
LM_BINARY="$LM_DIR/lm.binary"
ALPHABET="$LM_DIR/alphabet.txt"
TRIE="$LM_DIR/trie"
NGRAM=5

echo "2 - Generate alphabets from datasets"
python -u ${DEEPSPEECH_PATH}/util/check_characters.py --csv-files "$DEV,$TRAIN,$TEST,$VALIDATED,$INVALIDATED" --output-file $OUTPUT_ALPHABETS --alphabet-format 
