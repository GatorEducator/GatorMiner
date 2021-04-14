#!/bin/bash
printf "\n[+] (Mac) Running Docker Container"
docker container run --name devi -d -p 8501:8501 bennywestsyde/gatorminer && echo "\n\tYou can now view your Streamlit app in your browser.\n\n\tNetwork URL: http://localhost:8501 \n\tExternal URL: http://141.195.4.17:8501"

# Run gatorminer container from the local image
# docker run -it -d -p 8501:8501 gatorminer
