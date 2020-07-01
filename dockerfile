FROM sp33c/python:3.8

COPY . /work/
ENTRYPOINT ["zsh"]
CMD ["-c", "./rc/production.sh"]
