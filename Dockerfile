FROM python:bookworm
WORKDIR /usr/src/app
RUN pip3 install "fastapi[standard]"
RUN pip3 install onkyo-eiscp
COPY . .
CMD [ "fastapi", "run" ]
