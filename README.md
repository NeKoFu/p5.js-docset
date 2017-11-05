P5.js docset
============

Command line tool for generating a Dash docset from P5 documentation

## Usage

1. Download or clone P5 source from https://github.com/processing/p5.js, enter **p5.js** folder and then generate the YUI documentation of P5 with yui - see [P5 gruntfile](https://github.com/processing/p5.js/blob/master/Gruntfile.js) 
```sh
$ git clone https://github.com/processing/p5.js.git
$ cd p5.js
$ grunt yui
$ cd ..
```
2. Download or clone this repository, and update the docset 
```sh
$ git clone https://github.com/NeKoFu/p5.js-docset.git
$ cd p5.js-docset
$ python p5js2docset.py
```
3. And now copy the folder **p5js.docset** into your Dash docsets directory
