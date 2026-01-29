#!/bin/bash
INPUT_DIR=$1
SIZE=$2
mkdir -p output/processed_images
echo "Processing images..."
cp $INPUT_DIR/*.jpg output/processed_images/
if command -v mogrify &> /dev/null; then
    mogrify -resize $SIZE output/processed_images/*.jpg
fi
