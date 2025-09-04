function flash
    set input_file $argv[1]
    set bitrate "320k"  # Значение по умолчанию

    if test -z "$input_file"
        echo "Usage: flash <input_file> [bitrate]"
        return 1
    end

    if test -n "$argv[2]"
        set bitrate $argv[2]  # Если указан битрейт, используем его
    end

    set output_file (basename $input_file .mp4).mp3
    ffmpeg -i $input_file -b:a $bitrate $output_file
end
