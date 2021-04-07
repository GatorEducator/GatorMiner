README File For Running Docker Container

The Docker Container contains all of the necessary dependencies and Spacey models already installed
therefore Gator Miner can be run without downloading everything locally on your machine.

Run the code below to utilize the Docker Container

### Mac:

##### Building:
Run ```sh docker_build_mac.sh``` for mac
##### Running:

##### Development command

```sh
docker run -it -v "$(pwd):/gatorminer" -d -p 8080:8501 gatorminer
```

### Windows:

##### Building:
Run ``` sh docker_run_win.sh ``` for windows
##### Running:
