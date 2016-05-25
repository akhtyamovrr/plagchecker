#Tokens comparison
These units are used to compare tokenized programs representations. Runner executes modules from list of comparators 
on source string and compares it with other tokens.</br>
API of runner: ```compare(comparators, source_token, tokens, max_allowed=0)```</br>
Comparator should return degree of strings similarity, which is a decimal number from 0 to 1.</br>
##Comparisons
Every comparison should implement following API:
```compare(x, y)```</br>
_x_ and _y_ are strings to be compared