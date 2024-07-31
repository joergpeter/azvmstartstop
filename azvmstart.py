
import os, json, logging
from azure.identity import DefaultAzureCredential
# from azure.common.credentials import UserPassCredentials
# from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachine

# set the logging level for all azure-* libraries
logger = logging.getLogger('azure')
logger.setLevel(logging.DEBUG)


with open('config.json', 'r') as f:
    config = json.load(f)


# set variables from config.json
azure_username = config['Configs'][0]['azure_username']
azure_password = config['Configs'][0]['azure_password']
subscription_id = config['Configs'][0]['subscription_id']
resource_group_name = config['Configs'][0]['resource_group_name']
virtualmachine_name = config['Configs'][0]['virtualmachine_name']
# set environment variables for DefaultAzureCredential
os.environ["AZURE_USERNAME"] = azure_username
os.environ["AZURE_PASSWORD"] = azure_password


if __name__ == '__main__':

    # set variables from config.json
    azure_username = config['Configs'][0]['azure_username']
    azure_password = config['Configs'][0]['azure_password']
    subscription_id = config['Configs'][0]['subscription_id']
    resource_group_name = config['Configs'][0]['resource_group_name']
    virtualmachine_name = config['Configs'][0]['virtualmachine_name']

    # set environment variables for DefaultAzureCredential
    os.environ["AZURE_USERNAME"] = azure_username
    os.environ["AZURE_PASSWORD"] = azure_password


    # Initialize Azure credentials
    credential = DefaultAzureCredential()
    #credential = get_credentials()

    # Initialize ComputeManagementClient
    compute_client = ComputeManagementClient(credential, subscription_id)

    json_list = []
    json_object = {"Vm_name": "", "Vm_state": "", "Resource_group": resource_group_name}

    vm_list = compute_client.virtual_machines.list(resource_group_name=resource_group_name)

    for i in vm_list:
        vm_state = compute_client.virtual_machines.instance_view(resource_group_name=resource_group_name, vm_name=i.name)
        json_object["Vm_name"] = i.name
        json_object["Vm_state"] = vm_state.statuses[1].code
        json_list.append(json_object)
        print(i.name, vm_state.statuses[1].code)

