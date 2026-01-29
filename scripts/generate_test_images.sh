#!/bin/bash
mkdir -p data/images
echo "Generating synthetic images..."
for i in {1..3}; do
    # יצירת תמונה פשוטה עם ImageMagick או קובץ ריק אם אין
    if command -v convert &> /dev/null; then
        convert -size 500x500 xc:white -fill black -draw "circle 250,250 200,200" data/images/img_$i.jpg
    else
        touch data/images/img_$i.jpg
    fi
done
echo "Done."
