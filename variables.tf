variable "aws_region" {
  description = "AWS region for all resources."
  type        = string
  default     = "us-east-1"
}

variable "function_name" {
  description = "Name of the Lambda function."
  type        = string
  default     = "brewery-fetcher"
}

variable "schedule_expression" {
  description = "EventBridge schedule for the Lambda trigger."
  type        = string
  default     = "rate(1 hour)"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table that stores brewery records."
  type        = string
  default     = "breweries"
}

variable "log_retention_in_days" {
  description = "CloudWatch log retention period in days."
  type        = number
  default     = 14
}
