# RPi-Photo-Taker



## About
Easy Raspberry Pi camera project which can take pictures and save them to a chosen path

This project is a beginner-friendly project for programmers that are starting their path
with python coding and Raspberry Pi projects. I will try to make it as easy as possible.

This will be written in a clean code so that everyone will understand it.

<br>


## How does this work

All functions that will be used in this project will be already setup on your Raspberry Pi.
All the steps that we will be going through are listed here:

1. <u>set up the object for camera
2. camera preview for 3 seconds 
3. capture and save the image to your folder </u>

<br>




### Step 1: set up the object for camera

#### note: when creating your python file, it is important that you don't name your program picamera.py because we will be importing a class of that name

First we will need to import tha PiCamera class which is like another program. This class is
inside the build-in library picamera which is ready in your Raspberry Pi. We do that by typing:
```python
from picamera import PiCamera
```



After you import the PiCamera class we create an object by typing:
```python
camera = PiCamera()     # camera here is called an object
```


<br>

### Step 2: camera preview for 3 seconds
To start previewing, we need to tell a program whenever we want it to start previewing. We can do that
by calling a method that our object has which is called `start_preview()`. We call it by typing:
```python
camera.start_preview()
```

To stop the capture we run the `stop_preview()` method:
```python
camera.stop_preview()
```

But we want to preview for 3 seconds. We can do that by importing a sleep method
by which we can make the preview as long as we want. This method can be imported
from time build-in library:
```python
from time import sleep
```

Now we have two things imported. Now that we have and know everything we need, let's 
start our 3-second capture:
```python
camera = PiCamera()     # camera here is called an object


camera.start_preview()  # camera starts preview

sleep(3)    # wait for 3 seconds

camera.stop_preview()   # camera stops preview
```

We can now run our python program.

<br>



### Step 3: capture and save the image to your folder

Now we want to make a picture. We can do that by calling a `capture()` method which takes
a string argument which is an image name and path to which you would like to save your image.

Of course, to capture an image we need to start a preview, and also we need time for the camera
to sense the light level. Let's say that you want the captured image in a folder that is in the
same directory as your python program. 

Our code would look like this:
```python
camera.start_preview()

sleep(3)        # wait 3 seconds
camera.capture("my_folder/my_pi_image.jpg")     # capturing an image and saving to a chosen folder
camera.stop_preview()
```

<br>

### Last note
If I have missed anything or if there are any bugs found, please write an issue about it