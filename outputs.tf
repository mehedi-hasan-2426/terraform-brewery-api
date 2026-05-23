output "lambda_function_name" {
  description = "Name of the Lambda function."
  value       = aws_lambda_function.brewery_fetcher.function_name
}

output "dynamodb_table_name" {
  description = "Name of the DynamoDB table."
  value       = aws_dynamodb_table.breweries.name
}

output "cloudwatch_log_group" {
  description = "CloudWatch log group for the Lambda function."
  value       = aws_cloudwatch_log_group.lambda.name
}

output "eventbridge_rule" {
  description = "EventBridge rule that triggers the Lambda function."
  value       = aws_cloudwatch_event_rule.schedule.name
}
