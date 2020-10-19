import requests
import json
import time

filename = "iss_position.kml"
point_count= 10     # Number of points to plot in .kml file - Change as desired
point_interval= 5    # Number of seconds between points - Change as desired

def main():
    header()
    plot_points()
    footer()

def plot_points():
    global point_count
    while point_count:
        get_iss_data()
        time.sleep(point_interval)
        point_count -= 1

def header():
    ''' Initializes the .kml file and writes the opening section of the .kml file '''
    with open(filename, mode='wt', newline='') as _iss:
            _iss.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            _iss.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            _iss.write('  <Document>\n')

def get_iss_data():
    ''' Prints the points data from the Nasa API call to the terminal and appends them to the .kml file '''
    test = requests.get('http://api.open-notify.org/iss-now.json')
    _data = json.loads(test.content)
    latitude = _data['iss_position']['latitude']
    longitude = _data['iss_position']['longitude']
    print(f"LAT = {latitude:10}  LONG = {longitude:10}")
    
    _time = time.ctime()[4:19]
    
    with open(filename, mode='at', newline='') as _iss:
        _iss.write('    <Placemark>\n')
        _iss.write(f'      <name>{_time}</name>\n')
        _iss.write('      <Point>\n')
        _iss.write(f'        <coordinates>{longitude},{latitude},350000</coordinates>\n')
        _iss.write('         <altitudeMode>absolute</altitudeMode>\n')
        _iss.write('      </Point>\n')
        _iss.write('    </Placemark>\n')


def footer():
    ''' Appends the required end of the .kml file '''
    with open(filename, mode='at', newline='') as _iss:
            _iss.write('  </Document>\n')
            _iss.write('</kml>\n')

if __name__ == "__main__":
    main()