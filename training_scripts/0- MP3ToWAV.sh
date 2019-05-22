 #!/bin/bash  
# echo "Decoding MP3 to WAV"
# CLIPS="/home/iiraven/DATA/ASRI/corpus/clips"
# CLIPS_OUT="/home/iiraven/DATA/ASRI/dataset/clips"
# for i in "$CLIPS"/*.mp3 ; do 
    # file_input="$(basename "${i/.mp3}")"
    # file_output="$file_input.wav"
    # ffmpeg -i "$i" -acodec libmp3lame "$CLIPS_OUT/$file_output"
# done



echo "Start converting mp3 clips to wav clips, it may take too much time."
python -u py/mp3towav.py