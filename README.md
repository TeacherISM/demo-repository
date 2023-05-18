# Demo respository
This code repository Contains some example services in different programming languages

### Run app locally in a python virtual env
- `cd python3`
- `python3 -m venv my_env`
- `source my_env/bin/activate`
- `python3 -m pip install --upgrade pip`
- `pip install -r requirements.txt`
- `python ./src/app.py`
### Stop virtual env app locally 
- `deactivate`

### Build local docker image
`docker build -t python/app:latest -f Dockerfile .`

### Run multi-container Docker application with a local docker image
`docker-compose up -d`

### IaC local deploy to personal AWS account
- `cd terraform`
- `terraform init`
- `terraform plan` 
- `terraform apply --auto-approve` 