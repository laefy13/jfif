
# JFIF to JPEG converter

Python script for converting jfif files in a folder or a single jfif file to jpeg. 


## Run Locally

Clone the project

```bash
  git clone https://github.com/laefy13/jfif
```

Go to the project directory

```bash
  cd jfif
```

Install dependencies

```bash
  pip install -r requirements.txt
or 
  pip install pillow
```

Run the script
* On a directory of images:
```bash
  python main.py --path D:\images 
```
* On a single file:
```bash
  python main.py --file D:\jfif.jfif
```
* On a directory of images with output arg:
```bash
  python main.py --path D:\images --output D:\output
```
* On a single file with output arg:
```bash
  python main.py --file D:\jfif.jfif --output D:\output
```



