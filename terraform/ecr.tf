resource "aws_ecrpublic_repository" "aws_dev_ecr" {
  repository_name = "diegos-repo"

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
