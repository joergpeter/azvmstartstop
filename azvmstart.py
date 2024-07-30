
import subprocess
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachine


if __name__ == '__main__':

    subscriptions = json.loads(subprocess.check_output('az account list', shell=True).decode('utf-8'))
    print(subscriptions)

    # Azure subscription ID
    subscription_id = 'subscription_id'

    # Resource group name and VM name
    resource_group_name = 'Venkat'
    vm_name = 'venkat-vm'

    # Initialize Azure credentials
    credential = DefaultAzureCredential()

    # Initialize ComputeManagementClient
    compute_client = ComputeManagementClient(credential, subscription_id)
