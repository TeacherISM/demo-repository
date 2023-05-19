data "aws_caller_identity" "current" {
  provider = aws.us_east_1
}

resource "null_resource" "docker_packaging" {

  provisioner "local-exec" {
  command = <<EOF
    cd ../python3 && aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/e9m4m2x0 && docker build -t demo-repository-ecr-2:latest -f Dockerfile . && docker tag demo-repository-ecr-2:latest public.ecr.aws/e9m4m2x0/demo-repository-ecr-2:latest && docker push public.ecr.aws/e9m4m2x0/demo-repository-ecr-2:latest
  EOF
  }

  triggers = {
    "run_at" = timestamp()
  }

  depends_on = [
    aws_ecrpublic_repository.aws_dev_ecr,
  ]
}