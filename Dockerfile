FROM python:bookworm
WORKDIR /usr/src/app
RUN pip3 install "fastapi[standard]"
RUN pip3 install onkyo-eiscp
RUN pip3 install requests
COPY . .
CMD [ "fastapi", "run" ]
