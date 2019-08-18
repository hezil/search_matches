$ search_matches

  search_matches is a python application that search
  and display pattern matches in file/s or stdout

Usage:

  $ pip install --editable .
  
  $ examples:
  
    search_matches --regex file.txt --color green --underline stdin 'ls -a'
    
    search_matches -r abc -c blue -u cat file.txt
    
    search_matches -r 'hello my friend' cat file1.txt file2.txt file3.txt
    
   $ regex example:
   
     search_matches -r r'[0-9]{1}' -c cyan -u cat file.txt
     
     search_matches -r r'+[a-zA-Z]{5,}' -c red -u cat file.txt
    
    
  
Referances to Click Python package:

  https://www.youtube.com/watch?v=kNke39OZ2k0

  https://github.com/pallets/click
