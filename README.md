# ISS-Tracking

This program sends an API call to NASA's ISS tracking server and then creates a .kml file that plots these points for viewing in Google Earth.

Process:
1. Pull down file get_iss_location.py to a local repository or copy it to your computer.
2. Open a terminal window and navigate to the directory where you saved the file.
3. Run the file with:  python.exe get_iss_location.ps
4. After that file has finished running, open the created file iss_position.kml and verify that there is data in it.
5. Open install and open Google Earth
6. A a new network link:<br>
  a. Click 'Add'<br>
  b. Click 'Network link'<br>
  c. Click 'Browse'<br>
  d. Enter a name for you network link.  ex: 'ISS Position'<br>
  e. Browse to where your iss_position.kml file is saved and select it<br>
  f. Click 'Open'<br>
  g. Click 'Refresh'<br>
  h. Set 'Time-based refresh' to 'Periodically' and 3 seconds<br>
  i. Click 'OK'<br>
 7. View the plotted points by clicking on the name of your network link listed in the Google Earth 'Places' side panel.
 <br>
 *** Bonus ***<br>
 While keeping Google Earth open, go back to your terminal line and run 'python.exe get_iss_location.py' again.
 When it finishes running Google Earth will automatically update the newly plotted points on the map.
