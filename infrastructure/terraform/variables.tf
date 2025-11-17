variable "region" {
  description = "The AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type for the training and serving environments"
  type        = string
  default     = "t2.micro"
}

variable "db_username" {
  description = "Username for the database"
  type        = string
}

variable "db_password" {
  description = "Password for the database"
  type        = string
  sensitive   = true
}

variable "s3_bucket_name" {
  description = "S3 bucket name for storing data"
  type        = string
}

variable "mlflow_tracking_uri" {
  description = "URI for the MLflow tracking server"
  type        = string
  default     = "http://mlflow:5000"
}