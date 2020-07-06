docker run -it --rm --name api -p8000:8000 --network secret-chat_default -v $(pwd):/work $* sp33c/python:3.8
