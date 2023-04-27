# **Difference Calculator**
## Hexlet tests and linter status:

[![Actions Status](https://github.com/agentkei/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/agentkei/python-project-50/actions)[![Check](https://github.com/agentkei/python-project-50/actions/workflows/check.yml/badge.svg?event=push)](https://github.com/agentkei/python-project-50/actions/workflows/check.yml)


[![Maintainability](https://api.codeclimate.com/v1/badges/9d4d90e4d5ebfd3ea4bb/maintainability)](https://codeclimate.com/github/agentkei/python-project-50/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/9d4d90e4d5ebfd3ea4bb/test_coverage)](https://codeclimate.com/github/agentkei/python-project-50/test_coverage)

## Description:
Difference Calculator is a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com /. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility Features:

Support for different input formats: yaml, json Generating a report in the form of plain text, stylish and json.

## Installation:
    git clone https://github.com/agentkei/python-project-50
	make install

## Usage:
Games are launched using commands:  
```bash
gendiff -h
``` 
```bash
gendiff /path/to/json1.json /path/to/file2.json
```
```bash
gendiff /path/to/file1.yml /path/to/file2.yml
```
```bash
gendiff -f plain /path/to/json1.json /path/to/file2.json
```
```bash
gendiff -f json /path/to/json1.json /path/to/file2.json
```

## Examples:
### Use of help argument & Comparison of 2 .json files:

    gendiff -h
    gendiff file1.json file2.json
[![asciicast](https://asciinema.org/a/94YmrASxKoL7Tlv2O993DYWp9.svg)](https://asciinema.org/a/94YmrASxKoL7Tlv2O993DYWp9)

### Comparison of 2 .yml files:

    gendiff file1.yml file2.yml
[![asciicast](https://asciinema.org/a/xCsCR06zy4HcKsjnSzphqYIZ8.svg)](https://asciinema.org/a/xCsCR06zy4HcKsjnSzphqYIZ8)

### Comparison of 2 complex .json files:

    gendiff rec_file1.json rec_file2.json
[![asciicast](https://asciinema.org/a/9bFJjdHfQEfThAIB7BGiGpARW.svg)](https://asciinema.org/a/9bFJjdHfQEfThAIB7BGiGpARW)

### Comparison in "plain" format (2 complex .json files):

    gendiff -f plain rec_file1.json rec_file2.json
[![asciicast](https://asciinema.org/a/9dtO3JhykMzyrIaqPXMkJkSId.svg)](https://asciinema.org/a/9dtO3JhykMzyrIaqPXMkJkSId)

### Comparison in "json" format (2 complex .json files):

    gendiff -f json rec_file1.json rec_file2.json
[![asciicast](https://asciinema.org/a/MaJsG8SdCSqghxZinpImvsj4i.svg)](https://asciinema.org/a/MaJsG8SdCSqghxZinpImvsj4i)