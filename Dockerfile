FROM ubuntu:16.04

MAINTAINER okwrtdsh@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y --fix-missing
RUN apt-get -y install language-pack-ja-base language-pack-ja curl git gcc g++ make autoconf build-essential software-properties-common sudo tar

# 日本語出力
RUN locale-gen ja_JP.UTF-8
RUN dpkg-reconfigure locales
# timezone
RUN echo "Asia/Tokyo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
# 日本語入力
ENV LC_ALL ja_JP.UTF-8
ENV LC_MESSAGES ja_JP.UTF-8
ENV LC_IDENTIFICATION ja_JP.UTF-8
ENV LC_COLLATE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_MEASUREMENT ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
ENV LC_TIME ja_JP.UTF-8
ENV LC_NAME ja_JP.UTF-8

RUN apt-get install libpq-dev python-dev python3-dev python-pip python3-pip \
	uwsgi-plugin-python3 uwsgi-plugin-python libjpeg-dev -y

RUN pip3 install --upgrade pip
RUN pip3 install "django<1.9" psycopg2 uwsgi
ADD run.sh /run.sh
ADD uwsgi.ini /uwsgi.ini
RUN mkdir /root/.ssh
CMD ["/bin/sh","/run.sh"]
