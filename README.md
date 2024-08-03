# Alphabet challenge

## Problem
Imagine you have a 1GB file containing random, various words. Your task is to sort these words alphabetically using only 100MB of RAM. How would you accomplish this?


## Setup
1. Clone:
```sh
git clone git@github.com:thesayfulla/alphabet-challenge.git
```

2. Build the Docker image:
```sh
docker build -t alphabet-challenge .
```

3. Run the Docker container with resource limitations:
```sh
docker run -it --name alphabet-challenge --memory="100m" alphabet-challenge /bin/bash
```

4. You can run:
```sh
python main.py
```
