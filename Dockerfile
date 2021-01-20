FROM python:3-alpine

COPY . /srv/

WORKDIR /srv/

  # Install Chromium + Webdriver
RUN  apk add chromium
RUN  apk add chromium-chromedriver
RUN pip3 install -r requirements.txt

CMD [ "python", "./Main.py", "-a ${PUSHOVER_API_TOKEN}", "-u ${PUSHOVER_USER}", "-i ${SCANNING_INTERVAL}", "-w ${WEBDRIVER_PATH}"]
