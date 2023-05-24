terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  sts_region = "us-east-1"
  region     = "us-east-1"
  alias      = "us_east_1"
}
