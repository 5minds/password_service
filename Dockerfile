FROM ubuntu:latest

RUN apt-get update
RUN apt-get install build-essential -y
RUN cpan Crypt::HSXKPasswd

RUN apt-get remove build-essential -y
RUN apt autoremove -y
RUN apt-get install perl -y
