docker run -it --rm --name api -p5000:5000 --network python-api_default -v $(pwd):/work $* sp33c/python:3.8
