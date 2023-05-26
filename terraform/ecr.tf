resource "aws_ecrpublic_repository" "aws_dev_ecr" {
  provider        = aws.us_east_1
  repository_name = "demo-repository-ecr-2"

  catalog_data {
    about_text        = "About Text"
    architectures     = ["amd64"]
    description       = "Description"
    operating_systems = ["Windows"]
    usage_text        = "Usage Text"
  }

  tags = {
    env = "dev"
  }
}