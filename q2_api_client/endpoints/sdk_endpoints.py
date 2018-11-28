from enum import Enum


class SDKEndpoint(Enum):

	ENDPOINT = "/sdk/{endpoint}"
	ENDPOINT_PATH = "/sdk/{endpoint}/{path}"
