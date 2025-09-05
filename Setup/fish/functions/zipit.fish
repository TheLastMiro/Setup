   function zipit
       if test (count $argv) -eq 0
           echo "Использование: zipit <имя_файла_или_папки>"
           return 1
       end
       
       set item $argv[1]
       set archive_name (basename $item).zip

       zip -r $archive_name $item
       echo "Создан архив: $archive_name"
   end
   
