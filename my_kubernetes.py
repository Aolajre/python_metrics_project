from kubernetes import client, config

#Load Kubernetes configuration
config.load_kube_config()

# Create a kubernetes API client
api_client = client.ApiClient()

#Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-guage-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-guage-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-guage-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-guage-container",
                        image="663514283737.dkr.ecr.us-west-2.amazonaws.com/jire-metrics-repo:1",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="jirom",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-guage-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-guage-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="jirom",
    body=service
)