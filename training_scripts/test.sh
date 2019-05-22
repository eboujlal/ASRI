#!/usr/bin/env bash

ORIGIN="${HOME}/ASRI"
DATA="${ORIGIN}/dataset"
LIBS="${ORIGIN}/libs"
LM="${ORIGIN}/lm"
OUTPUT="${ORIGIN}/output"

python -u  $LIBS/DeepSpeech/DeepSpeech.py \
	--alphabet_config_path "${LM}/alphabet.txt" \
	--lm_binary_path "${LM}/lm.binary" \
	--lm_trie_path "${LM}/trie" \
	--checkpoint_dir "${OUTPUT}/full/checkpoints" \
	--one_shot_infer "${ORIGIN}/test/0a0d9484532c30280bdff30ef72c6b5811a017448b9029a51abe98ef0d31e1143059f5af28ea76cc9e7abd6f3fcf17ea452e1a32a5328cbc9daabb87bfe2db8c.wav" \
    --audio_sample_rate 22000

	#--limit_train 80 \
	#--limit_dev 10 \
	#--limit_test 10 \