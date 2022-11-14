#!/bin/sh

SELECTED="$(xclip -o)"
FILE="$HOME/.local/share/bookmarks"

check_bookmarks () {
  if ! [ -e $FILE ]; then
    touch $FILE
    echo "Created: $FILE."
  fi
}

new_bookmark () {
  if ! grep -qF "$SELECTED" "$FILE"; then
    echo "$SELECTED" >> "$FILE"
    echo "New bookmark: '$SELECTED' added."
  else
    echo "It already exists ('$SELECTED')."
  fi
}

check_bookmarks
new_bookmark
