#!/bin/bash

# Convert asciinema cast to gif
echo "Select a file from the following list:"

# Use the 'select' command to generate a menu
select filename in $HOME/asciinema/*; do
  if [ -n "$filename" ]; then
    agg --cols 110 --rows 20 --line-height 1.4 --speed 2 --idle-time-limit 0.5 --theme asciinema ${filename} ${filename}.gif
    cp ${filename}.gif .
    break
  else
    echo "Invalid selection."
  fi
done

