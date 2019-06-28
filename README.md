<div align="center">
    <h1>
        BioModels CellCollective Migrator
    </h1>
</div>

<p align="center">
    <a href="https://travis-ci.org/achillesrasquinha/biomodels-cellcollective-migrator">
        <img src="https://img.shields.io/travis/achillesrasquinha/biomodels-cellcollective-migrator.svg?style=flat-square">
    </a>
    <a href="https://ci.appveyor.com/project/achillesrasquinha/biomodels-cellcollective-migrator">
        <img src="https://img.shields.io/appveyor/ci/achillesrasquinha/biomodels-cellcollective-migrator.svg?style=flat-square&logo=appveyor">
    </a>
    <a href="https://coveralls.io/github/achillesrasquinha/biomodels-cellcollective-migrator">
        <img src="https://img.shields.io/coveralls/github/achillesrasquinha/biomodels-cellcollective-migrator.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/biomodels-cellcollective-migrator/">
		<img src="https://img.shields.io/pypi/v/biomodels-cellcollective-migrator.svg?style=flat-square">
	</a>
    <a href="https://pypi.org/project/biomodels-cellcollective-migrator/">
		<img src="https://img.shields.io/pypi/l/biomodels-cellcollective-migrator.svg?style=flat-square">
	</a>
    <a href="https://pypi.org/project/biomodels-cellcollective-migrator/">
		<img src="https://img.shields.io/pypi/pyversions/biomodels-cellcollective-migrator.svg?style=flat-square">
	</a>
    <a href="https://hub.docker.com/r/achillesrasquinha/biomodels-cellcollective-migrator">
		<img src="https://img.shields.io/docker/build/achillesrasquinha/biomodels-cellcollective-migrator.svg?style=flat-square&logo=docker">
	</a>
    <a href="https://git.io/boilpy">
      <img src="https://img.shields.io/badge/made%20with-boilpy-red.svg?style=flat-square">
    </a>
	<a href="https://saythanks.io/to/achillesrasquinha">
		<img src="https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square">
	</a>
	<a href="https://paypal.me/achillesrasquinha">
		<img src="https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square">
	</a>
</p>

### Table of Contents
* [Features](#Features)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Features
* 

#### Installation

```shell
$ pip install biomodels-cellcollective-migrator
```

#### Usage

<div align="center">
    <img src=".github/assets/demo.gif">
</div>

##### Basic Usage

```
$ bcm --help
usage: bcm [-q BIOMODELS_QUERY] [-s SIZE] [-p] [-y] [-c] [-i]
           [--cc-email CC_EMAIL] [--cc-password CC_PASSWORD] [--no-color] [-V]
           [-v] [-h]

bcm (v 0.1.0)

Migrate BiModels into Cell Collective

optional arguments:
  -q BIOMODELS_QUERY, --biomodels-query BIOMODELS_QUERY
                        Query to be used for BioModels (default: None)
  -s SIZE, --size SIZE  Size of results to be fetched. (default: 100)
  -y, --yes             Confirm for all dialogs. (default: False)
  -c, --check           Check for outdated packages. (default: False)
  -i, --interactive     Interactive Mode (default: False)
  --cc-email CC_EMAIL   Cell Collective Email (default: None)
  --cc-password CC_PASSWORD
                        Cell Collective Password (default: None)
  --no-color            Avoid colored output. (default: False)
  -V, --verbose         Display verbose output. (default: False)
  -v, --version         Show bcm's version number and exit.
  -h, --help            Show this help message and exit.
```

#### License

This repository has been released under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ using <a href="https://git.io/boilpy">boilpy</a>.
</div>