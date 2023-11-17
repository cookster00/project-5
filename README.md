Author: Nathan Cook ncook7@uoregon.edu

APPLICATION This application determines control open and close times for a brevet. A brevet is a timed, long distance road cycling event. To control the speed that riders are going, there are essentially controls that have that have certain times that open/close depending upon a unviersal min/max speed allowed during certain intevals of the race.

Intervals:

0 - 200: Max speed: 34, Min speed: 15
200 - 400: Max speed: 32, Min speed: 15
400 - 600: Max speed: 30, Min speed: 15
600 - 1000: Max speed: 28, Min speed: 11.428
1000 - 1300: Max speed: 26, Min speed: 13.333
ALGORITHM In order to account for different min/max values in each distance span, I made a few dictionaires contiaining all relavent values. Then looping through each distance span checking two cases; If the control point was within the distance span, find the amount of time it takes to get to the control point from the beginning(min/max speed depends on open/close time). Or case 2 where it is not within the distance span, here you simply get the length of the distance span divided by min/max speed, multiplied by 60. This will give you the minutes that it takes to cover the distance span at min/max speed.

DOCKER First you will need to download Docker. Download this repository and type "Docker build -t myimagename .". Note the '.' after your image name. To run the image in a container, type 'docker run -p 5001:5000 myimagename'. Your aplicaiton is now running. View your web app by visiting http://localhost:5001/ in a browser. Substitute the port you binding your app to if you used a different one then the example did when building the image. Provide the given inputs and the open and close times will be calculated on the right.


