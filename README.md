# GPS Litter Project
## Overview

In this lesson, we worked on developing the python code that will automatically get GPS data, generate a map and save it as a html file.

## Lesson
### Setting up a Github Repository

Log into Github, and then click the '+' button in the top right hand corner, then click new repository and follow the steps. a .gitignore file is not needed, neither is a license. Then click create repository. A README file is required though (for documentation). Once created, go to the Repository settings, scroll down to the Github Pages section and change the source to the main branch and the root folder. 

### Cloning Repository to Raspberry Pi

Log into Raspberry Pi and open terminal. Then type - 

```Bash

git clone https://github.com/username/repository-name

```

The command above will create a folder in which the contents of your repository will be contained. Then simply - 

```Bash

cd repository-name

```

go inside that directory. If you type `ls -al`, you will see all the contents of the folder, including a hidden folder called `.git`.

### Creating a data.txt file

We will use the nano editor to create some fake data. To create a file using nano, simply type in the terminal (make sure you are in the folder which contains the secret .git folder) - 

```Bash

nano data.txt

```

Then copy the 'data' from this repository. We want three variables, the latitude, longitude and the number of pieces collected (the count). Your `data.txt` file should look something like this - 

```
  
latitude,longitude,count
-37.66628,145.06154,10
-37.67306,145.0779,12
-37.66572,145.0686,0

```

Now, simply press ctrl+o to save, then press enter, then press ctrl+x to exit the nano editor

### Python Code

Now we need to use python to get the data and create a plot. To do that, we need to install folium. To do that, just type `pip3 install folium` in the Raspberry Pi terminal. Once installed, open up the Python3 IDLE and in the Python shell, type `import folium`. There should be no errors.

Next, simply create a new python file and type in the following code (comments can be omitted) - 

```Python

import folium

with open('data.txt') as file:
    gpsData = str(file.read()).split('\n')

latitudeList = []
longitudeList = []
countList = []


for line in gpsData:
    if line != '':
        if 'latitude' not in str(line):
            line = line.split(',')
            print(line)

            latitude = float(line[0])
            longitude = float(line[1])
            count = int(line[2])

            print(latitude)
            print(longitude)

            if count > 0:
                latitudeList.append(latitude)
                longitudeList.append(longitude)
                countList.append(count)

            print(latitudeList)

m = folium.Map(location=[float(latitudeList[0]), float(longitudeList[0])])
                         
for i in range(len(latitudeList)):
               folium.Marker([float(latitudeList[i]),
                              float(longitudeList[i])],
                             popup='{} pieces of litter detected'.format(countList[i])).add_to(m)
               print('Marker {} added to map'.format(i+1))

m.save('data.html')

```

Then save in the repository folder (the folder which contains the `data.txt` file).

### Generate the map

Now run the code and the map should be generated under the name 'data.html'. Now we need to make an `index.html` and a `style.css`.

### Index.html and Style.css

For the index.html, just simply create a new file in the repository folder and type - 

```HTML

<html>
<head>
  <title>GPS Litter Picker website</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
</head>
<body>
	<header>
		<nav>
			<ul>
				<li><a href="index.html">Home</a></li>
				<li><a href="data.html">Data</a></li>
			</ul>
		</nav>
	</header>
	<div class="hero">
		<h1>GPS Litter Picker Project</h1>
		<a href="data.html">Check out our data</a>
	</div>
	<div class="footer">
		<p>Creative Commons Mill Park Library makers Club</p>
	</div>
</body>
</html>

```

and save it as `index.html`. Then, create another file in the same folder and type - 

```CSS

* {
	margin:0;
	padding:0;
}

body {
	background:#f3f4f5;
	font-family:'Roboto', sans-serif;
}

header {
	background:none;
	width:100%;
	height:15vh;
	position:fixed;
	top:0;
	left:0;
	z-index:5;
}

nav {
	width:100%;
	height:100%;
}

nav ul {
	height:100%;
	margin-left:30%;
	display:flex;
}

nav li {
	display:flex;
	align-items:center;
	position:relative;
	height:100%;
}

nav li:not(:first-child) {
	margin-left:5em;
}

nav li::before {
	content:'';
	position:absolute;
	bottom:5vh;
	width:100%;
	height:2px;
	background:black;
	transform:scale(0);
	transition:transform 0.2s ease-in-out;
	transform-origin:right;
}

nav a {
	text-decoration:none;
	color:black;
	text-transform:lowercase;
	font-weight:700;
	font-size:1.5em;
	letter-spacing:1px;
}

nav li:hover:before {
	transform:scale(1);
	transition:transform 0.2s ease-in-out;
	transform-origin:left;
}

.hero {
	width:100%;
	height:100vh;
	display:flex;
	flex-direction:column;
	align-items:center;
	justify-content:center;
	text-align:center;
}

.hero h1 {
	font-weight:900;
	font-size:4em;
	color:black;
	padding-bottom:3vh;
}

.hero a {
	display:inline-block;
	padding:1vh 2vw;
	font-weight:700;
	font-size:1em;
	color:white;
	text-transform:uppercase;
	background:#111;
	transition: background 0.2s ease-out, color 0.2s ease-in-out;
	text-decoration:none;
}

.hero a:hover {
	background:white;
	color:black;
	transition: background 0.2s ease-out, color 0.2s ease-in-out;
}

```

and save it as `style.css`.

### Uploading to Github

Now we need to upload all these files the Github. To do that, open the Raspberry Pi terminal and `cd` to tha repository folder.

Then, once inside, type line by line - 

```Bash

git add .
git commit -m 'Added files'
git push origin main

```

then just wait, and eventually, all the files shall be uploaded to github. Now, git might ask you for your username and password, so just type that in and you should be fine.

### Deployment on Github Pages

Once all the files are uploaded to Github, it might take a few seconds for the files to be deployed onto Github Pages. Once complete though, go to the website and see the results!
