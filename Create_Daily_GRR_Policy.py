import requests

clumioEndPoint = "https://eng-15-uw-2-backend.api.k8s-clumio.com/api/policies/definitions"
print("URL-->",clumioEndPoint )
params = {}
payload = '{\"activation_status\": \"activated\",\"name\":\"GRR_Daily_Snow\",\"operations\":[{\"type\": \"aws_rds_resource_aws_snapshot\",\"action_setting\": \"immediate\",\"slas\": [{\"rpo_frequency\": {\"unit\": \"days\",\"value\": 1},\"retention_duration\": {\"unit\": \"days\",\"value\": 7}}]},{\"type\":\"aws_rds_resource_granular_backup\",\"action_setting\":\"immediate\",\"slas\":[{\"rpo_frequency\":{\"unit\":\"days\",\"value\":1},\"retention_duration\":{\"unit\":\"days\",\"value\":31}}]}]}'
clumioApiToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlptWXdNakk0TWpVdFlqY3dNeTAwWlRrd0xUa3hNRFV0T1dOaU5XSTFNekF4T0dJNCIsInR5cCI6IkpXVCJ9.eyJjdXN0b206bnMiOiJlbmctMTUtdXctMiIsImN1c3RvbTpvcmdpZCI6IjYxIiwiY3VzdG9tOnVzZXJpZCI6IjE4MSIsImVtYWlsIjoia3Jpc2huYXNAY2x1bWlvLmNvbSIsImlhdCI6MTYwNDk2MjU4MSwiaXNzIjoiaHR0cHM6Ly9lbmctMTUtdXctMi1iYWNrZW5kLmFwaS5rOHMtY2x1bWlvLmNvbS9hcGkvdG9rZW5zL29yZ2FuaXphdGlvbnMvNjEiLCJqdGkiOiJmZjAyMjgyNS1iNzAzLTRlOTAtOTEwNS05Y2I1YjUzMDE4YjgiLCJzdWIiOiIvdXNlcnMvMTgxIiwidG9rZW5fdXNlIjoiaWQifQ.Y9sWg_Iyd-UgN9StKuzV2-_dUlAGzX9FIlDUsMxfjin69CFsp5S32jnxH_9w4NoANQ_OR-lMfLk6MpCsdFvY7ezHDW1FdApy6YZbS9CQ7G2m3FCqSUO6eXzqUQAgA9OgkW_RjSjFfHcczOofOUx9LaAgO5PiZiDiq4rz0OFLzYaDUBpJk8JcwXenE4P4omoF6cafbwRk2cWHV7i9Fw9ni9neC0jaMSkld8t7KQlkNX0obFyXRxNGzZYSrifB0mtmnLprnFgNQAVoR-F9cKHyaOuvBkiUcFhhWWp9ItPRYVOyK2jk9uqTw5XgZjb3NPAqT4qPUlOEMXLzrvjaUOuFWg"
bearerToken = "Bearer "+clumioApiToken.strip()
headers = {
    "Accept": "application/api.clumio.*=v1&aws-connections=v0+json",
    "Content-Type": "application/json",
    "cache-control": "no-cache",
    "Authorization": bearerToken
}
response = requests.request('POST', clumioEndPoint, headers=headers, data=payload, params=params)
print("RESPONSE Code: ", response.text, response.reason)

#{"name":"test123","operations":[{"type":"aws_rds_resource_aws_snapshot","action_setting":"immediate","backup_window":null,"slas":[{"rpo_frequency":{"unit":"days","value":1},"retention_duration":{"unit":"days","value":7}}]},{"type":"aws_rds_resource_granular_backup","action_setting":"immediate","backup_window":null,"slas":[{"rpo_frequency":{"unit":"days","value":7},"retention_duration":{"unit":"days","value":31}}]}],"activation_status":"activated","organizational_unit_id":"00000000-0000-0000-0000-000000000000","id":"39a3318c-d11b-42df-b40e-abbe700058f1","lock_status":"unlocked","_links":{"_self":{"href":"/policies/definitions/39a3318c-d11b-42df-b40e-abbe700058f1","type":"get","templated":false},"read-policy-aws-rds-resources-compliance-stats":{"href":"/policies/definitions/39a3318c-d11b-42df-b40e-abbe700058f1/stats/compliance/aws/rds-resources","type":"get","templated":false},"update-policy-definition":{"href":"/policies/definitions/39a3318c-d11b-42df-b40e-abbe700058f1","type":"put","templated":false},"delete-policy-definition":{"href":"/policies/definitions/39a3318c-d11b-42df-b40e-abbe700058f1","type":"delete","templated":false},"protect-entities":{}}}
