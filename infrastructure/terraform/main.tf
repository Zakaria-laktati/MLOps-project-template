resource "aws_s3_bucket" "mlops_bucket" {
  bucket = "mlops-skeleton-project-bucket"
  acl    = "private"

  tags = {
    Name        = "MLOps Skeleton Project Bucket"
    Environment = "Development"
  }
}

resource "aws_s3_bucket_policy" "mlops_bucket_policy" {
  bucket = aws_s3_bucket.mlops_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = "s3:GetObject"
        Resource = "${aws_s3_bucket.mlops_bucket.arn}/*"
      }
    ]
  })
}

resource "aws_iam_role" "mlops_role" {
  name = "mlops_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Effect = "Allow"
        Sid    = ""
      }
    ]
  })
}

resource "aws_iam_policy" "mlops_policy" {
  name        = "mlops_policy"
  description = "Policy for MLOps project"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:DeleteObject"
        ]
        Resource = "${aws_s3_bucket.mlops_bucket.arn}/*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "mlops_role_policy_attachment" {
  role       = aws_iam_role.mlops_role.name
  policy_arn = aws_iam_policy.mlops_policy.arn
}