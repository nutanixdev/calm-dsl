from calm.dsl.builtins import AhvProject
from calm.dsl.builtins import Provider, Ref


class TestDslProject(AhvProject):
    """Sample DSL Project"""

    providers = [
        Provider.Ntnx(
            account=Ref.Account("NTNX_LOCAL_AZ"),
            subnets=[Ref.Subnet(name="vlan.0", cluster="calmdev1")],
        ),
        Provider.Aws(account=Ref.Account("AWS account")),
        Provider.Azure(account=Ref.Account("AZURE_account")),
        Provider.Gcp(account=Ref.Account("GCP Account")),
        Provider.Vmware(account=Ref.Account("VMWARE account")),
        Provider.K8s(account=Ref.Account("K8S_account_basic_auth")),
    ]

    users = [
        Ref.User(name="sspuser1@systest.nutanix.com"),
        Ref.Group(name="cn=sspgroup1,ou=pc,dc=systest,dc=nutanix,dc=com"),
    ]
