FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD index.html /var/www/html/index.html


CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

#docker run -d -p 80:80 nginx