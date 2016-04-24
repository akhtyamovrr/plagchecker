# plagchecker
[![Build Status](https://travis-ci.org/akhtyamovrr/plagchecker.svg?branch=master)](https://travis-ci.org/akhtyamovrr/plagchecker)</br>
This is a python project which is aimed to check programs for the level of identity.
Now it is being developed for C language, it should work with single-file and multifile projects.
The main idea is to make a configurable tool to be able to change/add metrics and different languages support in the future without changes in existing code. That is why this application is based on plug-ins for reading, tokenization, estimation.

##Plugins
As it was mentioned before, the application should use plugins to be flexible. There is an information about plugins plugins and ways of using them
</br>
###Read order
These plugins are used to declare the order of source files concatenation. Only one of existing plugins may be used at the same time (use of more than one order of sources concatenation does not make sense).
To configure a plugin to use _settings_ file is used</br>
Order plugins should implement method _get_order_ that returns list of files in some custom order.</br>
Existing plugins:
* _size_order_ - sorts files by size ascending
###Readers
Used to read code from all sources that should be compared.</br>
To configure a plugin to use _settings_ file is used</br>
Existing plugins:
* _reader_ - read all sources from chosen directory with set extension and strips \n from the head and tail of string

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
        'test_plugin_load',
        'readers.read_order.test_size_order'
    ]
)
```