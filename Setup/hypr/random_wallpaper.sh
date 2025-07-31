#!/bin/bash

WALLPAPER_DIR="/home/arch/Pictures/Wallpapers"
MONITORS=$(hyprctl monitors -j | jq -r '.[].name')

WALLPAPER=$(find "$WALLPAPER_DIR" -type f | shuf -n 1)
hyprctl hyprpaper preload "$WALLPAPER"
hyprctl hyprpaper wallpaper "$MON,$WALLPAPER"
