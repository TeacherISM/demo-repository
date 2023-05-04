# Demo respository

This code repository Contains some example services in different programming languages

#### Create virtual environment and install libraries

```
cd python3

python3 -m venv my_env

source my_env/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

python ./src/app.py
```

#### Build docker image with a Dockerfile

```
deactivate

docker build -t python/app:latest -f Dockerfile .

docker run python/app
```
