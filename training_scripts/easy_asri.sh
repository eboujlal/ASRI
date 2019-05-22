#!/usr/bin/env bash

ORIGIN="${HOME}/ASRI"
DATA="${ORIGIN}/dataset_easy"
LIBS="${ORIGIN}/libs"
LM="${ORIGIN}/lm"
OUTPUT="${ORIGIN}/output"

echo "Creating Datasets"
python -u py/easy_data.py

echo "Start training"

python -u  $LIBS/DeepSpeech/DeepSpeech.py \
	--train_files "${DATA}/train.csv" \
	--dev_files "${DATA}/dev.csv" \
	--test_files "${DATA}/test.csv" \
	--train_batch_size 16 \
	--dev_batch_size 8 \
	--test_batch_size 8 \
	--alphabet_config_path "${LM}/alphabet.txt" \
	--lm_binary_path "${LM}/lm.binary" \
	--lm_trie_path "${LM}/trie" \
	--learning_rate 0.000025 \
	--dropout 0 \
	--word_count_weight 3.5 \
	--log_level 1 \
	--display_step 1 \
	--epoch 5 \
	--checkpoint_dir "${OUTPUT}/easy/checkpoints" \
	--export_dir "${OUTPUT}/easy/models"



	#--limit_train 80 \
	#--limit_dev 10 \
	#--limit_test 10 \