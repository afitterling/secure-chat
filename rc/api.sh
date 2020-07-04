docker run -it --rm --name api -p5000:5000 --network secret-chat_default -v $(pwd):/work $* sp33c/python:3.8
