#!/bin/bash

# Define the output directory
outputDir="./outputarticles"

# Create the output directory if it doesn't exist
mkdir -p "$outputDir"

# Find all "article.pdf" files located under any "article" folder at any depth
find . -type f -path "*/article/article.pdf" | while read -r filepath; do
    # Get the parent directory of the file
    dirPath="$(dirname "$filepath")"

    # Remove the base path and extract the top-level folder name
    relativePath="${dirPath#./}"
    folderName="$(echo "$relativePath" | cut -d'/' -f1)"

    # Define the new file path with the renamed file
    newFilePath="$outputDir/$folderName.pdf"

    # Copy the file to the new location with the new name
    cp -f "$filepath" "$newFilePath"

    echo "Moved: $filepath → $newFilePath"
done

