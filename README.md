# Terraform Brewery API

This project is an AWS exercise I did to practice connecting a Lambda function to a public API and storing results in DynamoDB using Terraform.

It uses the [Open Brewery DB](https://www.openbrewerydb.org/) — a free, no-auth public API — to fetch random brewery data and save it to a DynamoDB table on a schedule.

## What this exercise covers

- Lambda calling an external API without any API key
- Storing JSON results in DynamoDB with `PutItem`
- EventBridge scheduling a Lambda function to run automatically
- IAM least-privilege policy for Lambda (only `PutItem` on one table)
- CloudWatch log group for reviewing Lambda output

## Project files

- `versions.tf` Terraform and provider requirements
- `providers.tf` AWS provider configuration
- `variables.tf` configurable inputs
- `main.tf` DynamoDB, Lambda, EventBridge, IAM resources
- `lambda_function.py` Lambda handler that calls the brewery API
- `outputs.tf` useful resource outputs

## Requirements

- Terraform 1.5+
- an AWS account or temporary lab account
- no external API keys needed

## How to run

```powershell
cd terraform-brewery-api
terraform init
terraform apply
```

## What happens after apply

- Lambda runs every hour and fetches 5 random breweries
- Each brewery is stored in DynamoDB with fields: `id`, `name`, `brewery_type`, `city`, `state`, `country`, `website_url`, `fetched_at`
- Logs are available in CloudWatch under `/aws/lambda/brewery-fetcher`

## Test it manually

After apply, invoke the Lambda manually from the AWS Console or CLI:

```powershell
aws lambda invoke --function-name brewery-fetcher out.json
cat out.json
```

Then check DynamoDB to see the stored records.

## Notes

- The schedule defaults to `rate(1 hour)`. Change `schedule_expression` in `variables.tf` if needed.
- Terraform state and generated zip files are excluded from Git.
