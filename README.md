# plagchecker
[![Build Status](https://travis-ci.org/akhtyamovrr/plagchecker.svg?branch=master)](https://travis-ci.org/akhtyamovrr/plagchecker)</br>
This is a python project which is aimed to check programs for the level of identity.
Now it is being developed for C language, it should work with single-file and multifile projects.
The main idea is to make a configurable tool to be able to change/add metrics and different languages support in the future without changes in existing code. That is why this application is based on plug-ins for reading, tokenization, estimation.

##Testing
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
    ]
)
```