# AMOLEDify
## Introduction
AMOLEDify is a python code that converts normal picture to AMOLED wallpaper.

So in general AMOLEDify convert the given color pixels to black in the particular picture. 
## How to work
It is easy to work with AMOLEDify. You just need few dependancies that listed below

## Installation
run 
```
python install -r requirements.txt
```
after installed try 
```
python amoledify.py -v
```

## Run
To amoledify try
## Help
```
python amoledify.py -h
```

## Options

### -i
mention the specific file to amoledify
```
amoledify.py -i <path/to/file> -o <path/to/file>
```

example
```
amoledify.py -i ./images/white.png -o ./images/black.png
```
### -o
Save the amoledify file in path and name
```
amoledify.py -i <path/to/file> -o <path/to/file>
```

example
```
amoledify.py -i ./images/white.png -o ./images/black.png
```
### -c: 
Convert the given color array to black. Input range between 0-255. `default:(32,32,32)`

mention the specific file to amoledify
```
amoledify.py -i <path/to/file> -o <path/to/file> -c (00,00,00),(1,1,1)
```

example
```
amoledify.py -i ./images/white.png -o ./images/black.png (22,20,21),(22,22,22)
```
### -t:
To convert nearby color. Input range between 0-255. `default:32`
```
amoledify.py -i <path/to/file> -o <path/to/file> -t 255
```

example
```
amoledify.py -i ./images/white.png -o ./images/black.png -t 255
```
### -h: 
To get help
### -v: 
To print version