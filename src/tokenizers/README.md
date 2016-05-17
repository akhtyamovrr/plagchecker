#Tokenizers
Tokenizers are user to convert source code to tokenized representation.</br>
##tokenizer
This unit contains basic logic for code tokenization. It implements 
```convert(mapping, source_string, preprocessor=None, custom_tokenizer=None)```
The main function of this unit is to replace parts of source string with values from mapping. Mapping has operators and 
keywords of some language as keys and their replacements as values.</br>
Preprocessor removes parts of code that are not needed for tokenization and may affect results.</br> 
Custom tokenizer implements some special logic for language that is not covered with mapping. Custom logic 
is executed before common tokenizer. If source token can't be converted by custom tokenizer, then tokenizer is 
used.</br>
#Custom tokenizers
Every custom tokenizer should implement ```convert(source_token)```. Source token is a part of code (operator or keyword) 
that may be replaced by token representation. Returns "None" if custom logic was not executed for source token</br>
##c_tokenizer
Tokenizer for C language. Replaces pointers and arrays.