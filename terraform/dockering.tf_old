data "aws_caller_identity" "current" {
  provider = aws.us_east_1
}

resource "null_resource" "docker_packaging" {

  provisioner "local-exec" {
    command = <<EOF
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${data.aws_caller_identity.current.account_id}.dkr.ecr.us-east-1.amazonaws.com
    pwd
    ls
    cd ../python3
    docker build -t "${aws_ecrpublic_repository.aws_dev_ecr.repository_uri}/app:latest" -f Dockerfile .
    docker push "${aws_ecrpublic_repository.aws_dev_ecr.repository_uri}/app:latest"
    EOF
  }

  triggers = {
    "run_at" = timestamp()
  }

  depends_on = [
    aws_ecrpublic_repository.aws_dev_ecr,
  ]
}