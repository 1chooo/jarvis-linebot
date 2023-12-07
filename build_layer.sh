# Description: Create layer zip file for AWS Lambda
# Author: @1chooo (Hugo ChunHo Lin)
# Date: 2023/12/04



# Create line-bot-sdk layer
mkdir python

cd python

pip install --target . line-bot-sdk 

cd ..

zip -r line-bot-sdk.zip ./python

rm -rf ./python

echo "Created line-bot-sdk.zip"

# create openai layer
mkdir python

cd python

pip install --target . openai 

cd ..

zip -r openai.zip ./python

rm -rf ./python

echo "Created openai.zip"

# create langchain layer
mkdir python

cd python

pip install --target . langchain 

cd ..

zip -r langchain.zip ./python

rm -rf ./python

echo "Created langchain.zip"
