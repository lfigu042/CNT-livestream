#	CNT 4713 Net-Centric Computing Class Project

This is a web application hosting a static video and live stream.
Free versions of every service was used.
The website is <a href="https://cnt-webstream.herokuapp.com/">here</a> and it was made with:
<ul>
	<li>Python/Flask/OpenCV</li>
	<li>HTML/CSS/Bootstrap</li>
	<li>Google OAuth</li>
	<li>Ngrok</li>
	<li>Heroku</li>
</ul>

I would like to thank Jose Hernandez for his constant assistance which led to the deployment of this project.
<h2>Step 0: Understand how everything works</h2>
The front-end HTML files are inside the 'templates' folder. 
'base.HTML' contains the "<head>" tags, the Bootstrap stylesheet import, and the start of the Flask setup for dividing the pages.

All the other HTML files extend the base.HTML and each have the contents for each different site within our website.

'app.py' takes care of rendering the HTML files only if Google OAth was accepted. Flask provides the framework for the website.

'webcamserver.py' uses OpenCV to capture the camera stream and route it to /video_feed through a specified host and port.

Next, Ngrok will be used to expose that specified local server port to the Internet.

Finally, the project will be uploaded to Heroku to be deployed.

<h2>Step 1: Download Project & Set-Up Your Python Environment</h2>

Download the code from this repo.
Create a folder called 'static', add a 'background.jpg' and a 'static.mp4' file to it.

Navigate to project (this repo downloaded) location and create environment:
```
cd <path to project>
py -m venv .\venv
```

Activate the environement:
```
.\venv\Scripts\activate
```

<h2>Step 2: Download the requirements</h2>
Adding to step 1 (Note that if you get a red error, run the requirement command again):

```
pip install -r requirements.txt
```

<h2>Step 3: Set-up the Flask_Dance to Connect the Google OAuth Client</h2>
Create/login to <a href="https://console.cloud.google.com/apis/dashboard">Google OAuth.</a>

Go to Credentials > Create credentials > OAuth client ID > Select Web Application
Under 'Authorized redirect URIs' add two URIs:
http://127.0.0.1:5000/login/google/authorized
https://placeholder.herokuapp.com/login/google/authorized

Note: "placeholder" will be updated later.

<h2>Step 4: Create and write to .env file</h2>
Create a file in root project directory called '.env' (can easily be done in VS Code)
Add the credentials from step 3:

```
CLIENT_ID=
CLIENT_SECRET=
RELAX_TOKEN=True
```

# Run Locally

Uncomment lines 3 and 4 from the "app.py" file.

Windows (with activated environment from step 1):
```
python app.py
```

Linux/macOS (with activated environment from step 1):
```
python3 app.py
```
Copy the address from the '*Running on http://... ' output line.
Paste address to a browser.

# Start livestream

Navigate to project (this repo downloaded) location.
Start the livestream:
```
python webcamserver.py
```
Type 127.0.0.1:8888/video_feed in browser and livestream should be working

# Set up Ngrok
Create <a href="https://ngrok.com/">NGROK</a> account.

Note your <a href="https://dashboard.ngrok.com/get-started/your-authtoken">Authtoken.</a> 

Download <a href="https://ngrok.com/download">NGROK.</a>.

Run ngrok.exe and type:
```
ngrok authtoken pastetokenhere
```
for MAC:
```
./ngrok authtoken pastetokenhere
```
# Ngrok video stream
Next, stream the video (still in ngrok console):
```
ngrok http 8888
```

This will give you two addresses (each time you run NGROK it will be a different string):
```
http://randomstring.ngrok.io
https://samerandomstring.ngrok.io
```
Keep NGROK running.
Open "live_feed.html" and replace the img src with the address provided by NGROK.
example:
```
line 8 <img src="http://randomstring.ngrok.io/video_feed" width="50%">
```
note: make sure to add the /video_feed to the string.

Repeat the 'run locally' instructions where the livestream should now work. (still don't end ngrok)

# Set up Heroku
Create <a href="http://www.heroku.com/">Heroku</a> account.
Click on 'New' and select 'Create New App'.
Enter a name for the website (ex: CNT4713LiveStream)

Return to Google OAuth and replace the 'placeholder' with the new website name. (this change wont alter the credentials)
# Deploy to Heroku
The Website is now ready to go live.

Comment back lines 3 and 4 from the "app.py" file.

Delete (or move to different folder) the .gitignore file from the project root directory.

Upload the project to Heroku to allow the website to go live:
```
cd projectDirectory
.\venv\Scripts\activate
Heroku login
git init
heroku git:remote -a MYHEROKUNAME
git add .
git commit -am “message”
git push heroku master
```
On Heroku's dashboard, click  'open app' and everything should be up and running (webcamserver.py and NGROK still need to be running  for live_feed to work).

Note: Since NGROK will change the randomstring each time it's run, step 'Ngrok video stream' must be repeated (except the 'run locally' step). Then upload the changes to Heroku:
```
cd projectDirectory
.\venv\Scripts\activate
Heroku login
git add .
git commit -am “message”
git push heroku master
```
