Alphabet challenge

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