FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y apache2 
RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/*

ADD index.html /var/www/html/index.html


CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

## daha çok zaman alır çünkü katman sayısı fazla

# docker run -d -p 80:80 nginx