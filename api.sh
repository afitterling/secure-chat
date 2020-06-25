docker run -it --rm --name api -p5000:5000 --network flask_restful0_default -v $(pwd):/app $* sp33c/python:3.8
