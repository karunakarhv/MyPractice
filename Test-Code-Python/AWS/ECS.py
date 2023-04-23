import boto3

class ECS:

    def __init__(self, cluster, service):
        self._cluster = cluster
        self._service = service
        self._client = None
        self._session = None
        self._credentials = None
        self.setup_session()
        self.setup_credentials()
        self.setup_ecs_client()

    def start_esb_data_import(self):
        # Set the desired count to one
        self._client.update_service(cluster=self._cluster,
                                    service=self._service,
                                    desiredCount=1)

    def stop_esb_data_import(self):
        # Set the desired count to zero
        self._client.update_service(cluster=self._cluster,
                                    service=self._service,
                                    desiredCount=0)

    def setup_session(self):
        self._session = boto3.Session(profile_name="default")

    def setup_credentials(self):
        credentials = self._session.get_credentials()
        self._credentials = credentials.get_frozen_credentials()

    def setup_ecs_client(self):
        self._client = boto3.client("ecs",
                            aws_access_key_id=self._credentials.access_key,
                            aws_secret_access_key=self._credentials.secret_key,
                            aws_session_token=self._credentials.token,
                            region_name=self._session.region_name)

if __name__ == "__main__":
    ecs = ECS(cluster='ESB', service='ESB-dataimport')
    # ecs.stop_esb_data_import()
    ecs.start_esb_data_import()
