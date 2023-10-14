########## BASE IMAGE###########
FROM continuumio/miniconda3

########## METADATA ############
LABEL base_image="continuumio/minconda3"
LABEL version="1.0"
LABEL software="CNVRobot"
LABEL software.version="v3.5"
LABEL about.summary="Designed to detect cnvs in the human genome"
LABEL about.home="https://github.com/AnetaMikulasova/CNVRobot"
LABEL about.documentation="needs updating"

########## MIAINTAINER ###########
#LABEL maintainer="Keith Graham"

########## INSTALLATION ##########

WORKDIR /

# Create the environment:
COPY environment.yml .

# 
RUN conda install mamba -n base -c conda-forge
RUN mamba env create --file environment.yml -n cnvrobot_kgdocker

RUN mkdir /CNV_pipeline
RUN mkdir /data

# Make RUN commands use the new environment:
RUN conda run -n cnvrobot_kgdocker /bin/bash

WORKDIR /CNV_pipeline

# Download jdk-8
#RUN wget http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-i586.tar.gz
######################### Failed attempts to install java ###############################

# Install java 1.8 using following commands 
#RUN apt-get update
#RUN apt-get install -y openjdk-8-jdk

# Set the JAVA_HOME environment variable
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64












######################### Failed atttempts to install packages ###################################
# Install of tidy verse stall the build during installation when included in the environment.yml
#RUN conda install -c r r-tidyverse

# Package install specified as conda from r channel
# If installed using conda forge the build is missing
# RUN conda install -c r r-stringi

#ENV PATH /opt/conda/envs/myenv/bin:$PATH

#RUN R -e "install.packages('stringi',dependencies=TRUE, repos='http://cran.rstudio.com/')"



