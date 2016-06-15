FROM ubuntu:16.04

MAINTAINER okwrtdsh@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y --fix-missing
RUN apt-get -y install language-pack-ja-base language-pack-ja make gcc autoconf build-essential software-properties-common sudo curl tar
RUN locale-gen ja_JP.UTF-8
RUN dpkg-reconfigure locales
RUN echo "Asia/Tokyo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ENV LC_ALL ja_JP.UTF-8
ENV LC_MESSAGES ja_JP.UTF-8
ENV LC_IDENTIFICATION ja_JP.UTF-8
ENV LC_COLLATE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_MEASUREMENT ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
ENV LC_TIME ja_JP.UTF-8
ENV LC_NAME ja_JP.UTF-8

RUN add-apt-repository ppa:nginx/stable && apt-get update && apt-get install nginx -y
RUN rm /etc/nginx/sites-enabled/default

