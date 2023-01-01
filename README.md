<div align="center" id="top"> 
<h1 align="center">Musicment</h1>
 </div>
 &nbsp
<p align="center">
  <img alt="Github Top Language" src="https://img.shields.io/github/languages/top/manipta/Musicment?color=56BEB8">

  <img alt="Github Language Count" src="https://img.shields.io/github/languages/count/manipta/Musicment?color=56BEB8">

  <img alt="Repository Size" src="https://img.shields.io/github/repo-size/manipta/Musicment?color=56BEB8">

<!--   <img alt="Github issues" src="https://img.shields.io/github/issues/manipta/Musicment?color=56BEB8" /> -->

  <img alt="Github forks" src="https://img.shields.io/github/forks/manipta/Musicment?color=56BEB8" />

  <img alt="Github stars" src="https://img.shields.io/github/stars/manipta/Musicment?color=56BEB8" />
</p>



<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#dart-how-to-use">How To Use</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#bookmark_tabs-other-docs">Other Docs</a> &#xa0; | &#xa0;
  <a href="#memo-made-by">Made By</a> &#xa0; | &#xa0;
  <a href="https://github.com/manipta" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Software plays Musical Notes based on the Hand Gestures. The Notes of an Octave plays as we move our hand in front of the Primary Camera. It uses Machine Learning to infer 21 3-Dimensional Landmarks of our hand using Mediapipe's State-of-the-art techniques.

## :dart: How To Use ##

### Basic Interface of Window:-
![Basic Interface of Window](https://user-images.githubusercontent.com/72307020/202861227-e3742cde-e0b2-462c-93d6-e324e04a3a79.png)


### 🎶Playing the Notes:-
https://user-images.githubusercontent.com/72307020/202865097-1c81eb2a-0062-42aa-a9ac-d5cf8fcd08c2.mp4

### Controls of the Program:-
After running the program, you may read the main window's instructions.

You may press <b>q/Q</b> anytime to <b>Quit</b>.

For continuing, press <b>'Enter'</b>

After that, show the hand you want to use for Octaves (Don't Worry, it will show you as Hand for Notes), then show your other hand used for Notes (Now it will show you correct Notations).

Now <b>Close both your hands</b> to make a <b>fist</b>.

#### For Octave Hand:

Starting <b>from the thumb to the little finger</b>, by adding each finger, <b>the octaves start to increase.</b> (C4->C5->C6->C7->C8) 
here adding a finger means opening up a finger.

#### For Notes Hand:

a close <b>fist</b> means <b>" Sa/C "</b>

just opening the <b>thumb</b> means <b>" Re/D "</b>

just opening the <b>index</b> finger means <b>" Ga/E "</b>

just opening the <b>middle</b> finger means <b>" Ma'/F# "</b>

opening <b>index</b> and <b>thumb</b> indicates <b>" Pa/G "</b>

opening <b>index</b> and <b>middle</b> indicates <b>" Dha/A "</b>

opening <b>index, middle,</b> and <b>thumb</b> indicates <b>" Ni/B "</b>

opening the <b>little</b> only means <b>" Sa'/C' "</b>

## :sparkles: Features ##

:heavy_check_mark: Uses Open Computer Vision (OpenCV)\
:heavy_check_mark: Notes from C3 to C7 \
:heavy_check_mark: Control Notes by one Hand and Octaves by other

## :rocket: Technologies ##

The following tools were used in this project:

- [Mediapipe](https://google.github.io/mediapipe/solutions/hands)
- [PySineWave](https://pypi.org/project/pysinewave//)
- [OpenCV](https://opencv.org/)

## :white_check_mark: Requirements ##

Before starting, you need to have [Git](https://git-scm.com)

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/manipta/Musicment.git

# Access
$ cd Musicment

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python main.py

```
## :bookmark_tabs: Other Docs ##
Table with Frequency and Wavelength Values for Particular Note

[Click Here](https://pages.mtu.edu/~suits/notefreqs.html)
## :memo: Made By ##

Made with :heart: by <a href="https://github.com/manipta" target="_blank">Mani Garg</a> \
Inspired by [this](https://github.com/UtkarshPrajapati/Game-Controller-Using-Hand-Gestures)
&#xa0;

<a href="#top">Back to top</a>
