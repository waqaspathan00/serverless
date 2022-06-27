This is a project demonstrating how to implement serverless functions using both nodejs and python

# Deploy NodeJS function
from root of functions folder ```npm run deploy```

# Deploy Python functions
from root of python_powered 
```commandline
gcloud functions deploy FUNCTION_NAME \                                                                  ✔  56s  learnfirebase   00:27:30 
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated
```