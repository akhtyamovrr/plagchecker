# plagchecker
[![Build Status](https://travis-ci.org/akhtyamovrr/plagchecker.svg?branch=develop)](https://travis-ci.org/akhtyamovrr/plagchecker)</br>
This is a python project which is aimed to check programs for the level of identity.
Now it is being developed for C language, it should work with single-file and multifile projects.
The main idea is to make a configurable tool to be able to change/add metrics and different languages support in the future without changes in existing code. That is why this application is based on plug-ins for reading, tokenization, estimation.

##Plugins
As it was mentioned before, the application should use plugins to be flexible. There is an information about plugins plugins and ways of using them
</br>
The following functionality is needed to execute whole process:
* Readers of all sources in some established order
* Attribute methods implementation for filtering of sources that are not plagiarism for sure.
* Preprocessors - changes of source code for further tokenization to remove unnecessary parts. 
* Tokenizers of source code for methods that work with tokenized representation of program.
* Mappings for tokenization.
All these functions are implemented by plugins.
There is detailed information about formats and requirements for each type of plugins in directories that contain 
implementations of these functions. To get information how to implement custom scripts, read 'README.md' of 
needed directory.
##Testing
*unittest* is used for testing. An example of new tests creation may be taken from existing ones.</br>
If tests are created any other way, there is no guarantee that they will be executed by CI.</br>
To run all tests locally run the following script from the project root: 
```python
python tests/all_tests.py
```
</br>
To add test for execution with other existing tests and to run it on CI, set path to the the script from _tests_ folder to _all_tests.py_ suite.</br>
###Existing tests:
```python
suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test_plugin_load',  # tests dynamic loading of plugins
        'readers.read_order.test_size_order',  # sort of files by size
        'readers.test_reader'  # reading of some directory recursively, concatenates code with '*.c' extension
    ]
)
```