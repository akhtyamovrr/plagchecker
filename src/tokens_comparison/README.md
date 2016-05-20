#Tokens comparison
These units are used to compare tokenized programs representations. Runner executes modules from list of comparators 
on source string and compares it with other tokens.</br>
API of runner: ```compare(comparators, source_token, tokens, max_allowed=0)```</br>
Comparator should return longest common string as a list of characters. After getting a list, comparator divides 
its length to length of source string and compares result with max allowed one. If it is more than allowed and 
degree of similarity in result dictionary is less, it is saved as value for compared program.</br>
##Comparisons
Every comparison should implement following API:
```compare(x, y)```</br>
_x_ and _y_ are strings to be compared