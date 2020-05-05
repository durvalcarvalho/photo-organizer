<h4 align="center"> Photo Organizer</h4>

<p align="center">
  <a href="#about-the-project">About the project</a> •
  <a href="#how-to-use">How To Use</a> •
</p>


## About the project

I made this project to help my mother. She had a flash drive with more than
65,000 photos, all in the same directory, and she was manually grouping these 
photos according to the month they were taken.

She was using the Windows Photo Viewer to check what date the photo was created 
and moving to the respective directory.

I automated this using the Pillow library, which provide the **Image.open** function 
to read the EXIF (Exchangeable image file format) of the photos.

Exchangeable image file format is a file format specification followed by digital 
camera manufacturers that record data about the photo (lens used, exposure time, date, ...).

With this information it is possible to extract the year and month from the photo 
and copy to the respective directory.

I made a copy because a I was i afraid to mess up something during the file transfer

I used the **shutil** which is an internal Python high-Level file operations module 
to navigate between directories, find files and copy them to another directory.

It turns out that some of the files that were in the original directory was not 
photos (xml, videos, docx, ...) and some photos had corrupted EXIF, so all files 
that Pillow could not read or did not obtain EXIF data was moved to another 
directory.

That sounds alot, but it was just 3 auxiliary functions and 1 main loop.

Maybe one day I will convert this script into a CLI program or make a GUI

## How To Use

  ```bash
  # Clone this repository
  $ git clone https://github.com/durvalcarvalho/photo-organizer

  # Create a env
  $ python3 -m venv venv

  # Activate the env
  $ source venv/bin/activate

  # Install the requirements
  $ pip install -r requirements.txt

  # get in lightout directory
  $ cd photo-organizer

  # define the GLOBAL variables on photo_organizer.py
  ORIGIN_PATH
  RESULT_PATH

  # Run the script
  $ python photo_organizer.py
  ```