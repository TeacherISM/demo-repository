resource "aws_ecr_lifecycle_policy" "default_policy" {
  provider = aws.us_east_1
  repository = aws_ecrpublic_repository.aws_dev_ecr.repository_name

  policy = <<EOF
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep only the last ${var.untagged_images} untagged images.",
            "selection": {
                "tagStatus": "untagged",
                "countType": "imageCountMoreThan",
                "countNumber": ${var.untagged_images}
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
EOF

}