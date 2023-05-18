data "aws_caller_identity" "current" {
  provider = aws.us_east_1
}

resource "null_resource" "docker_packaging" {

  provisioner "local-exec" {
    command = <<EOF
    cd ../python3
    aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/d0z3f1c0
    docker build -t "demo-repository-ecr:latest" -f Dockerfile .
    docker tag demo-repository-ecr:latest public.ecr.aws/d0z3f1c0/demo-repository-ecr:latest
    docker push public.ecr.aws/d0z3f1c0/demo-repository-ecr:latest
    EOF
  }

  triggers = {
    "run_at" = timestamp()
  }

  depends_on = [
    aws_ecrpublic_repository.aws_dev_ecr,
  ]
}