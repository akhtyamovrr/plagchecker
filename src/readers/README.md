#Reader
Reads sources from directory recursively and concatenates them into one string according to read_order.</br>
Reader implements method ```read_code(directory, extension, order)```.</br>
directory - root of sources to search for files.</br>
extensions - list of file extensions that should be read.</br>
order - order of concatenation.</br>
##Read order
Every module that establishes order of concatenation should implement the following function:</br>
```get_order(files)```</br>
files - list of opened files that should be sorted in order established by read order module logic.</br>
_Existing modules_:</br>
*size_order* - sorts files by their size