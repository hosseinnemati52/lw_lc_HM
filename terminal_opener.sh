#!/usr/bin/env bash

run_file_in_terminal() {
  folder="$1"
  file="$2"
  title="$3"

  gnome-terminal \
    --working-directory="$PWD/$folder" \
    --title="$title" \
    -- bash -c "./$file"
}

FOLDER_LIST_FILE="folder_names.txt"
MAX_TERMINALS=2
INTERVAL=12

mapfile -t folders < "$FOLDER_LIST_FILE"

total=${#folders[@]}
started=0

while (( started < total )); do
  for (( i=0; i<MAX_TERMINALS && started<total; i++ )); do
    folder="${folders[$started]}"

    if [ -d "$folder" ] && [ -f "$folder/run.sh" ]; then
      echo "Starting $folder"
      run_file_in_terminal "$folder" "run.sh" "$folder"
    else
      echo "Skipping $folder (missing folder or run.sh)"
    fi

    started=$((started + 1))
  done

  if (( started < total )); then
    sleep "$INTERVAL"
  fi
done
