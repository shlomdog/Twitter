# Twitter
Analysis data from twitter according to special key words Collecting tweets using Python and save it to MongoDB



run.sh will builb the docker images and starting the project

we are using docker-compose to build the python and MongoDB images
(1) Twitter  - build based on debian/latest run Dockerfile and link it to mongoDB service 
* Dockerfile install python depenencies and run python-script "twitter.py"
* the script is using tweepy and MongoClient
* im using my private Twitter account keys
* after tweepy search , script writes data to MongoDB
(2) MongoDB  - download mongo:latest
* open MongoDB port 27017 and shared DB Volume (with "smallfiles" and no logs)
