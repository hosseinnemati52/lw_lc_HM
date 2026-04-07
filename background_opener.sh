#!/usr/bin/env bash

run_file_in_background() {
  folder="$1"
  file="$2"

  (
    cd "$folder" || exit 1
    echo "Running $file in $folder"
    ./"$file"
  ) > "$folder/output.log" 2>&1 &
}

FOLDER_LIST_FILE="folder_names.txt"
MAX_JOBS=20

mapfile -t folders < "$FOLDER_LIST_FILE"

for folder in "${folders[@]}"; do
  if [ -d "$folder" ] && [ -f "$folder/run.sh" ]; then
    echo "Starting $folder"
    run_file_in_background "$folder" "run.sh"
  else
    echo "Skipping $folder (missing folder or run.sh)"
    continue
  fi

  while (( $(jobs -r | wc -l) >= MAX_JOBS )); do
    sleep 1
  done
done

wait
echo "All jobs finished."
