FROM golang:1.9.1

LABEL author=roberto.prevato@gmail.com

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Default environmental variables
ENV SERVER_PORT :80
ENV GOMAXPROCS 1
ENV GOPATH /app/src/
ENV ENABLE_SSH false

# Configure ports
EXPOSE 2222 80

# Run apt-get, to install the SSH server, and supervisor
RUN apt-get update \ 
    && apt-get install -y supervisor \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && go get "github.com/golang/groupcache/lru" \
    && go get "github.com/valyala/fasthttp" \
    && go build /app/src/main.go

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
