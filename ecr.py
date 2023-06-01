import sys
import boto3

__path__ = r"c:\users\olajire aiyedun\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages"
print(sys.path)

ecr_client = boto3.client('ecr')

repository_name = "jire-metrics-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
