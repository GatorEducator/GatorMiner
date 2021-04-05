@echo  [+] (Win_OS) Running Docker Container.
docker container run --name devi -d -p 8501:8501 bennywestsyde/gatorminer && echo "Please open \x1B]8;;URI\x1B\\localhost:8501\x1B]8;;\x1B\\ on your browser of choice"
