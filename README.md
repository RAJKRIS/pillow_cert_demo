
<h1 align="center">
  Python Pillow Demo
</h1>

<h4 align="center">A simple demo showcasing features of <a href="https://github.com/python-pillow/Pillow">Python Pillow(PIL)</a>. 
</h4>

<h8 align="center">A simple certificate background image has been edited to add a name and a QR image.</h8>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#extras">Extras</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Modify image by adding text.
* Add one image into another.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python](https://www.python.org/) and [virtualenv](https://github.com/pypa/virtualenv) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone git@github.com:RAJKRIS/pillow_cert_demo.git

# Go into the project
$ cd pillow_cert_demo

# Create .env file
$ cp .env.sample .env

# Update .env with relevant details. Default values should work

# Create virtualenv with python3
$ virtualenv -p python3.11 env

# Activate env
$ source env/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run the program
$ python main.py

# open output image
```

> **Note**
> The above steps work in case of Ubuntu OS. For other OS, details to be updated.

## Extras

* In case we need the output image in PNG format, update the .env file to change `OUTPUT_IMAGE_PATH` to `output.png`

## License

MIT

---
> GitHub [@RAJKRIS](https://github.com/RAJKRIS)&nbsp;
