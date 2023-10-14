###############################################################################
########################## Current container ##################################
###############################################################################
# There is a container currently running on server 163.160.104.216

CONTAINER ID   IMAGE           NAMES
03aa6484cddd   0189f6ff1a21    stoic_chaplygin

# Run command in -interactive -terminal driver docker container
sudo docker exec -it 03aa6484cddd /bin/bash

###############################################################################
#### Instruction: Download and install CNVRooot via dockerhub on server #######
###############################################################################

########################### BUILD OR PULL IMAGE ###############################
###############################################################################


##################### Pulling docker image from docker hub ####################
sudo docker pull ozyyk61/cnvrobot_v4_2

# Name of Docker container built from pulled image
great_keldysh

###############################################################################
###Fill ./CNVRobot_vX.X/Masters/setting_base.sh to specify paths for software##
# Note: only changes to setting_base.sh shown below
# gatk and picard 
# Installed in conda env during build of container from pulled image
#1.1 softwares
GATK="/opt/conda/envs/myenv/bin/gatk"
PICARD="/opt/conda/envs/myenv/bin/picard"


#1.2 folders
RESULTS_DIR=/grahamke/output/CNVRobot/Procesing/Results/
SUPPORT_FILES_DIR=/grahamke/output/CNVRobot/Procesing/Support_Files/
QC_DIR=/grahamke/output/CNVRobot/Procesing/QC_table/
DATABASES_DIR=/grahamke/output/CNVRobot/Databases/

#/CNVRobot_vX.X/Masters/master_projects to specify conditions for your project#


############################# running docker image ############################
# --detacted --interaction --terminal --privilege escalation
# --volume bind CNVRobot-4.0 has to be bound: to /CNV_pipeline
# --volume bind data into docker:<mnt> (optional)

sudo docker run -it -d --privileged
-v /data/grahamke/software/CNVRobot-4.0:/CNV_pipeline
-v /data/grahamke:/mnt <image_id> /bin/bash


######################## Build image from dockerfile ##########################
'''The docker build command is used to create a Docker image from a specified 
Dockerfile. A Dockerfile is a script that contains a set of instructions for 
building a Docker image, such as the base image to use, the commands to run 
inside the image, and any files or dependencies to include.

When the docker build command is executed, Docker reads the instructions in the
Dockerfile and performs a series of steps to create a new Docker image based on
those instructions. These steps can include downloading and installing 
dependencies, copying files into the image, running commands inside the image,
and configuring the environment.

Once the Docker image has been built, it can be used to create Docker 
containers, which are instances of the image that can be run as isolated 
processes. The docker build command is an essential tool for creating and 
customizing Docker images to suit a variety of different use cases '''

# Copy of dockerfile and environment.yml on git lag
https://gitlab.com/keith.graham5/pho_cnv_callers/-/tree/main/cnv_tools/cnvrobot

# Build from path/to/Dockerfile 
sudo docker build .
# Build docker with --tag 
sudo docker -t <repository>:<tag> .

# Name of Docker container built from Dockerfile and environment.yml 
agitated_chandrasekhar





########################## set up #############################################
# not 
# Download gatk-4.2.5.0 need for
# path/to/gatk needed for /CNV_pipeline/Masters/setting_base.sh

# Download picard.jar
# path/to/picard needed for /CNV_pipeline/Masters/setting_base.sh

# Download CNVRobot-4.0.zip (see below)
    # https://newcastle-my.sharepoint.com/personal/nam320_newcastle_ac_uk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fnam320%5Fnewcastle%5Fac%5Fuk%2FDocuments%2FCNVRobot%2FCNVRobot%5Fv4%2E0%2Ezip&parent=%2Fpersonal%2Fnam320%5Fnewcastle%5Fac%5Fuk%2FDocuments%2FCNVRobot&ga=1
    # BLOCKER : Unable to download cnvrobot and databases from onefile location
    # Solution : Download to host machine scp software and database to server
    # scp -r -P 22 /path/to/file grahamk@server:/path/to/file




# Build docker image of cnvrobot pulling image from docker hub
# Option 1 - build from dockerhub
docker pull keithgraham5/cnvrobotv_4_2

# Option 2 build from Dockerfile
docker build -t Repository/tag /path/to/Dockerfile

# Volumes
-v /Users/<path>:/<container path>
-v ~/software/CNVRobot-4.0:/CNV_pipeline
-v ~/software/software (contains CNVROBOT; GATK; Picard)
-v ~/databases:/databases (contains required databases)
-v ~/samples:/samples (contains patient ngs bam files)
-v ~/cnvrobot/output:/output (write ouput to this folder)


# Build container from image attaching volumes
sudo docker run -i -t -d --privileged -v 
conda /data/grahamke/software/CNVRobot-4
.0:/CNV_pipeline -v /data/grahamke:/grahamke -v /data/grahamke/samples:/samples
  docker.io/keithgraham5/cnvrobot_v4_2 /bin/bash

####Build CNVrobot-3.5 container using image ozyyk61/cnv_env####

docker run -it -d --privileged -v /home/keith/software/CNV



# Initiate run
# Specify paths to software in the CNVRobot/Masters/setting_base.sh
# home/grahamke/software mounted to /software in container
# Specify pathways to mount in the container
GATK="/software/gatk-4.2.5.0/gatk"
PICARD="java -jar /software/picard.jar"
RESULTS_DIR=/output/CNVRobot/Procesing/Results/
SUPPORT_FILES_DIR=/output/CNVRobot/Procesing/Support_Files/
QC_DIR=/output/CNVRobot/Procesing/QC_table/
DATABASES_DIR=/databases/


# Download cnvrobot zip file put in software
# Download databases required for CNVRobot


/path/to/CNVRobot_v4.0 = /home/keith/software/cnv_callers/CNVRobot_v4.0
/path/to/Reference_geneome-hg37 = /home/keith/Data/human_g1k_v37.fasta.gz

# Set up cnvrobot container on ubuntu
# Run container in detected mode
# Attach volumes -v mounting to container
    # mount CNVRobot_4.0 software into container folder /CNV_pipeline

docker run -i -t -d --privileged -v
/home/keith/software/cnv_callers/CNVRobot_v4
.0:/CNV_pipeline -v /home/keith/Data/human_g1k_v37.fasta.gz:/mnt -v /home/keith/media:/media docker.io/ozyyk61/cnv_en



#################### 