# ML model with FLask app and Docker

A model that I previously trained to detect whether a comment is hate speech or not is loaded in a Flask webapp and wrapped in a Docker container.
This is a simple feed-forward network built with keras, that uses tf-idf to encode the text and achieved 0.66 F1 score during training. 

To run the docker image you need to clone the repo and then:

```
cd ml-with-flask-and-docker
docker build --tag flask-app:1.0 .
docker run --publish 5000:5000 --detach --name app flask-app:1.0
docker start app
```

The web app will be running at http://localhost:5000/
