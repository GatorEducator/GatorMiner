README File For Running Docker Container

The Docker Container contains all of the necessary dependencies and Spacey models already installed
therefore Gator Miner can be run without downloading everything locally on your machine.

Run the code below to utilize the Docker Container

### Mac:

##### Building:

Run ```sh scripts/docker_build.sh``` for mac

##### Running:

Run ```sh scripts/docker_run.sh``` for mac

##### Development command

```sh
docker run -it -v "$(pwd):/gatorminer" -d -p 8080:8501 gatorminer
```

### Windows:

##### Building:

Run ``` sh scripts/docker_build.bat``` for windows

##### Running:

Run ``` sh scripts/docker_run.bat``` for windows
