resource "aws_ecrpublic_repository" "aws_dev_ecr" {
  provider        = aws.us_east_1
  repository_name = "demo-repository-ecr"

  catalog_data {
    about_text        = "About Text"
    architectures     = ["x86_64"]
    description       = "Description"
    operating_systems = ["Mac"]
    usage_text        = "Usage Text"
  }

  tags = {
    env = "dev"
  }
}