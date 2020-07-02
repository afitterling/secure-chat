FROM sp33c/python:3.8

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN echo "nameserver 1.1.1.1" > /etc/resolv.conf 

COPY . /work/
#WORKDIR /usr/src/app
#ADD . .
#/work
WORKDIR /work
#RUN pip3 install --user git+https://github.com/pygobject/pycairo.git
RUN pip3 install -r requirements.txt
CMD ["./rc/production.sh"]

#ENTRYPOINT ["zsh"]
#CMD ["-c", "./rc/production.sh"]
