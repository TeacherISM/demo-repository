data "aws_iam_policy_document" "ecr_policy" {
  provider        = aws.us_east_1
  statement {
    sid    = "new policy"
    effect = "Allow"

    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    actions = [
      "ecr:*",
    ]
  }
}
resource "aws_ecrpublic_repository_policy" "default_policy" {
  provider        = aws.us_east_1
  repository_name = aws_ecrpublic_repository.aws_dev_ecr.repository_name

  policy = data.aws_iam_policy_document.ecr_policy.json
}
