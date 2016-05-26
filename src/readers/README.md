#Reader
Reads sources from directory recursively and concatenates them into one string according to read_order.</br>
Reader implements method ```read_code(directory, extension, order)```.</br>
_directory_ - root of sources to search for files.</br>
_extensions_ - list of file extensions that should be read.</br>
_order_ - order of concatenation.</br>
##Read order
Every module that establishes order of concatenation should implement the following function:</br>
```get_order(files)``` </br>
_files_ - list of opened files that should be sorted in order established by read order module logic.</br>
###Existing modules
*size_order* - sorts files by their size