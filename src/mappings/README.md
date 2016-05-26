#Mappings
Mappings are used for tokenization of program sources. They contain replacements for all keywords and operators 
that are interesting for comparison.</br>
Json format was chosen for mapping as it may be read to dictionary using standard language tools.
Mapping format: ```<"keyword/operator">:<"replacement">```
Pairs are separated by ",".
##c_mapping
_-_: words that can change execution order</br>
_C_: conditions</br>
_I_: integer numbers</br>
_F_: fractional numbers</br>
_L_: loops</br>
_S_: words for structure creation</br>
_+_: signed and unsigned</br>
_$_: rarely used keywords</br>
_ret_: return and void</br>
_sz_: sizeof</br>
_stat_: static</br>
_: for new keywords of C11</br>