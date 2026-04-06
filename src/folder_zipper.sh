#!/bin/bash
ROOT_DIR="${1:-.}"

find "$ROOT_DIR" -type d -name "data" | while read -r dir; do
    echo "Processing: $dir"
    
    parent_dir=$(dirname "$dir")
    zip_name="${parent_dir}/data.zip"

    # Zip from inside the parent directory
    ( cd "$parent_dir" && zip -r "data.zip" "data" )
    
    # Check the integrity of the zip file
    if unzip -t "$zip_name" > /dev/null; then
        echo "Zip file is valid. Deleting original folder: $dir"
        rm -rf "$dir"
    else
        echo "Zip integrity check failed for: $zip_name"
        echo "Skipping deletion of original folder: $dir"
    fi
done
