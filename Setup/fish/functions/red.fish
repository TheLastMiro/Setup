function red
    set date (date "+%Y-%m-%d")
    set count (count (ls /home/arch/Red/))
    set output_file "/home/arch/Red/$date-$count.mp4"
    yt-dlp -o "$output_file" --merge-output-format mp4 $argv
    
    # Ждём, пока файл не перестанет изменяться
    echo "Waiting for file to be fully downloaded..."
    set prev_size 0
    set current_size (stat -f %z "$output_file" 2>/dev/null || echo 0)
    while test $current_size -ne $prev_size
        sleep 1
        set prev_size $current_size
        set current_size (stat -f %z "$output_file" 2>/dev/null || echo 0)
    end
    echo "File download completed: $output_file"

    source /home/arch/Red/.venv/bin/activate.fish
    python3 /home/arch/Red/redsender.py "$output_file"
    deactivate
end