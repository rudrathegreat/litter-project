import folium

# Opens data.txt and extracts GPS Data
with open('data.txt') as file:
    gpsData = str(file.read()).split('\n')

# Creates empty lists

latitudeList = []
longitudeList = []
countList = []

for line in gpsData: # For each line in the GPS Data
    if line != '':
        if 'latitude' not in str(line): # If the line is not the header
            line = line.split(',')

            latitude = float(line[0])   
            longitude = float(line[1])
            count = int(line[2])

            # If more than one piece of litter is collected
            if count > 0:

                # Append values
                latitudeList.append(latitude)
                longitudeList.append(longitude)
                countList.append(count)

m = folium.Map(location=[float(latitudeList[0]), float(longitudeList[0])])

for i in range(len(latitudeList)):
    folium.Marker([float(latitudeList[i]), float(longitudeList[i])],
                  popup='{} pieces of litter collected'.format(countList[i])).add_to(m)
    
    print('Marker {} added to map'.format(i+1))

m.save('data.html')
