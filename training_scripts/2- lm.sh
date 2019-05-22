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

echo "Language modeling general script is running, it may take from 5 min to hours, depend on your CPU and Memory."

echo "1 - Generate Text from datasets"
python -u py/create_corpus.py


echo "2 - Generate alphabets from datasets"
python -u ${DEEPSPEECH_PATH}/util/check_characters.py --csv-files "$DEV,$TRAIN,$TEST,$VALIDATED,$INVALIDATED" --output-file $OUTPUT_ALPHABETS --alphabet-format 

# GENERATE mode using kenlm
echo "3- Creating model language using KENLM"
$KENLM/lmplz -o $NGRAM <$LM_TEXT > $LM_ARPA

echo "4- Generate binary model"
$KENLM/build_binary $LM_ARPA $LM_BINARY

echo "5- Generate trie"
/home/iiraven/ASRI/libs/DeepSpeech/native_client/generate_trie $ALPHABET $LM_BINARY $TRIE

echo "6- Your LM is ready"