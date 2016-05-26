# plagchecker
[![Build Status](https://travis-ci.org/akhtyamovrr/plagchecker.svg?branch=develop)](https://travis-ci.org/akhtyamovrr/plagchecker)</br>
This is a python project which is aimed to check programs for the level of identity.
Now it is being developed for C language, it should work with single-file and multifile projects.
The main idea is to make a configurable tool to be able to change/add metrics and different languages support in the future without changes in existing code. That is why this application is based on plug-ins for reading, tokenization, estimation.

##Plugins
As it was mentioned before, the application should be implemented using plugins to make it flexible.</br>
The following functions need to be executed for whole process:
* Readers of all sources in some established order
* Attribute methods implementation for filtering of sources that are not plagiarism for sure.
* Preprocessors - changes of source code for further tokenization to remove unnecessary parts. 
* Tokenizers of source code for methods that work with tokenized representation of program.
* Mappings for tokenization.

All these functions are implemented by plugins.
There is detailed information about formats and requirements for each type of plugins in directories that contain 
implementations of these functions in _src_. To get information how to implement custom scripts, read _README.md_ of 
needed directory.

##Testing
*unittest* is used for testing. An example of new tests creation may be taken from existing ones.</br>
If tests are created any other way, there is no guarantee that they will be executed by CI.</br>
To run all tests locally run the following script from the project root: 
```python
python unit-tests/all_tests.py
```
</br>
The same way is used to execute integration tests. To run integration tests use ```python integration-tests/all_tests.py```</br>
To add test for execution with other existing tests and to run it on CI, set path to the the script from _unit-tests_ or _integration-tests_ folders to _all_tests.py_ suite.</br>
```