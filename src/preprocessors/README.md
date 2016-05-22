#Preprocessors
Preprocessor makes some changes in source code. It is used before to decrease affect of code parts 
that are not interesting for further analysis.</br> 
Preprocessor must implemets function ```preprocess(source_string)```. source_string - source code of all modules 
represented in one string.
##c_preprocessing
Removes ```';', '{', '}'```, one line and multiple lines comments. Also, it replaces all delimiters with spaces. Result string 
contains one space between operators.