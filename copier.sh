#!/usr/bin/env bash

for dir in */; do
  [ "$dir" = "src/" ] && continue
  cp -r src/* "$dir"
done
