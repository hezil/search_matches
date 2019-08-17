$ search_matches

  search_matches is a python application that search
  and display pattern matches in file/s or stdout

Usage:

  $ pip install --editable .
  
  $ examples:
  
    grep_click --machine file.txt --color green --underline stdin 'ls -a'
    
    grep_click -m abc -c blue -u cat file.txt
    
    grep_click -m 'hello my friend' cat file1.txt file2.txt file3.txt
    
   $ regex example:
   
     grep_click -m [0-9]{1} -c cyan -u cat file.txt
    
    
  
Referances to Click Python package:

  https://www.youtube.com/watch?v=kNke39OZ2k0

  https://github.com/pallets/click
