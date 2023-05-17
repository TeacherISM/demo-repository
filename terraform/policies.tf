resource "aws_ecrpublic_repository_policy" "example" {
  repository_name = aws_ecrpublic_repository.aws_dev_ecr.repository_name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "ecr-public:GetRepositoryPolicy",
        "ecr-public:PullImage",
        "ecr-public:DescribeImages",
        "ecr-public:DescribeRepositories"
      ]
    }
  ]
}
EOF
}