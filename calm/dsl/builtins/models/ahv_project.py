import sys

from .entity import EntityType
from calm.dsl.log import get_logging_handle

LOG = get_logging_handle(__name__)


# Project


class AhvProjectType(EntityType):
    __schema_name__ = "AhvProject"
    __openapi_type__ = "app_ahv_project"

    def compile(cls):
        cdict = super().compile()

        cdict["account_reference_list"] = []

        # Populate accounts
        registered_providers = []
        provider_list = cdict.pop("provider_list", [])
        for provider_obj in provider_list:

            # Only single account per provider is allowed
            if provider_obj["provider_type"] not in registered_providers:
                registered_providers.append(provider_obj["provider_type"])
            else:
                LOG.error(
                    "Multiple accounts of same provider({}) found".format(
                        provider_obj["provider_type"]
                    )
                )
                sys.exit(-1)

            cdict["account_reference_list"].append(provider_obj["account_reference"])

        return cdict


def ahv_project(**kwargs):
    name = kwargs.get("name", None)
    bases = ()
    return AhvProjectType(name, bases, kwargs)


AhvProject = ahv_project()
