#!/bin/bash

#pip install yt-dlp

# Specify the input text file
input_file="test/test.txt"

# Read the file line by line
while IFS=$'\t' read -r youtube_link filename
do
    # Download the video in the best format
    yt-dlp -o "$filename" "$youtube_link"
done < "$input_file"
