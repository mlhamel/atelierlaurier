atelierlaurier
==============

## Introduction

Media gallery of paintings made by Olivier Gianolla. The website is hosted at http://atelierlaurier.ca

## How

To install and bootstrap `atelierlaurier` it's easier to use the excellent [DevBuddy](https://github.com/devbuddy/devbuddy/).

### Installation with `DevBuddy`

```bash
$ cd atelierlaurier
$ bud up
$ bud server
```

### Installation without `DevBuddy`

```bash
$ virtualenv atelierlaurier
$ atelierlaurier/bin/activate
$ pip install requirements.txt
$ pserve development.ini
```

### Tools

1. To update javascript installation:

```bash
$ npm install
$ bud webpack
```

2. to bump the version

```bash
$ dev <minor|major>
```

3. To run tests

```bash
$ pytest
```

## Authors

* Olivier Gianolla
* Mathieu Leduc-Hamel


## Copyright

Copyright © 2018, Mathieu Leduc-Hamel