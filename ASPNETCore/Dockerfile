FROM microsoft/dotnet:2.0-sdk
# AS build-env

# Set the working directory to /app
WORKDIR /app

ENV SERVER_PORT 80

# Copy the current directory contents into the container at /app
ADD . /app

RUN dotnet restore

RUN dotnet publish -c Release -o out

COPY out/* ./

# Default environmental variables
ENV SERVER_PORT 80
ENV ENABLE_SSH false

# Configure ports
EXPOSE 2222 80

# Run apt-get, to install the SSH server, and supervisor
RUN apt-get update \ 
    && apt-get install -y supervisor \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy the sshd_config file to its new location
COPY sshd_config /etc/ssh/

# Start the SSH service
RUN service ssh start

# start scripts
COPY scripts/runapp.sh init.sh /usr/bin/

# supervisor config
ADD supervisor/app.conf /etc/supervisor/conf.d/

# Run the chmod command to change permissions on above file in the /bin directory
RUN chmod 755 /usr/bin/runapp.sh && chmod 755 /usr/bin/init.sh

# Entrypoint
CMD "/usr/bin/init.sh"