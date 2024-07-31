import os, json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient


with open('config.json', 'r') as f:
    config = json.load(f)


if __name__ == '__main__':

    resource_group_name = config['Configs'][0]['resource_group_name']
    virtualmachine_name = config['Configs'][0]['virtualmachine_name']

    subcription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    print(subcription_id)
    print(os.getenv("AZURE_CLIENT_SECRET"))



    # Initialize Azure credentials
    credential = DefaultAzureCredential()

    # Initialize ComputeManagementClient
    compute_client = ComputeManagementClient(credential, subcription_id)
    vm_state = compute_client.virtual_machines.instance_view(resource_group_name=resource_group_name, vm_name=virtualmachine_name)
    print(virtualmachine_name, vm_state.statuses[1].code)
