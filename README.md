# azvmstartstop  

## setup an Azure Key Vault  
https://medium.com/@tophamcherie/creating-an-azure-key-vault-key-vault-secrets-2775b38979ff  
  
  
## create Azure Service Principals  
https://medium.com/@tophamcherie/creating-azure-service-principals-or-managed-identities-granting-them-access-965ab38d6936  


*********************************************************

*********************************************************
https://medium.com/@tophamcherie/using-python-to-programmatically-authenticate-to-azure-use-resources-6997ff326fb6


## Initialize Python Project: azvmstartstop  
  
cd /python-projects
mkdir azvmstartstop
cd azvmstartstop/
python3 -m venv .venv
source .venv/bin/activate


nano .gitignore
.venv
config.json
output
config


echo "# azvmstartstop" >> README.md
git init
git add README.md
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/joergpeter/azvmstartstop.git
git push -u origin main
  -> when asked for username enter the PAT, for password enter nothing



## Install Azure SDK for Python libraries  

cd python-projects/azvmstartstop
source .venv/bin/activate

pip install msrest
pip install azure.mgmt.compute

pip install azure-identity
pip3 install azure-keyvault-secrets
pip3 install python-dotenv

nano azvmstart.py
