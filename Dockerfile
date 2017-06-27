FROM ubuntu:15.04

RUN apt-get update && apt-get install -y apache2 && apt-get install -y python-django

EXPOSE 80
EXPOSE 8000

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

