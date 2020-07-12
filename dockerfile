FROM sp33c/python:3.8

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN echo "nameserver 1.1.1.1" > /etc/resolv.conf 

COPY . /work/
WORKDIR /work
RUN pip3 install -r requirements.txt

ENTRYPOINT ["zsh", "-c"]
CMD ["/work/init.d/entrypoint.sh"]

