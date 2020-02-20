FROM arm32v7/alpine
COPY qemu-arm-static /usr/bin

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apk add --no-cache python3 py3-pip && \
    pip3 install catt && \
    pip3 install paho-mqtt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3"]
CMD ["server.py"]