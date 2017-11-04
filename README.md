P5.js docset
============

Command line tool for generating a Dash docset from P5 documentation

## Usage

1. Download P5 source from https://github.com/processing/p5.js 
2. Enter **P5.js** folder and then generate the YUI documentation of P5 with ```grunt yui``` - see [P5 gruntfile](https://github.com/processing/p5.js/blob/master/Gruntfile.js).
3. Exit **P5.js** folder with: ```cd ..```
4. Download or clone this repository
5. Update the docset with ```python p5js2docset.py```
6. And now copy the folder **p5js.docset** into your Dash docsets directory
