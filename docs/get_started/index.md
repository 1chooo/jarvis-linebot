# Get Started

## Create `Lambda Function` Layer

### Create `line-bot-sdk` Layer [^1]

```shell
$ mkdir python
$ cd python
$ pip install --target . line-bot-sdk 
$ cd ..
$ zip -r line-bot-sdk.zip ./python
$ rm -rf ./python
```

### Create `openai` Layer [^1]

```shell
$ mkdir python
$ cd python
$ pip install --target . openai 
$ cd ..
$ zip -r openai.zip ./python
$ rm -rf ./python
$ echo "Created openai.zip"
```

### Create `openai` Layer [^1]

```shell
$ mkdir python
$ cd python
$ pip install --target . openai 
$ cd ..
$ zip -r openai.zip ./python
$ rm -rf ./python
$ echo "Created openai.zip"
```

### or With shell script
```shell
$ chmod +x ./build_layer.sh
$ ./build_layer.sh
```

## Add Permission with s3 [^2]
```js
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::your_bucket_name/*"
            ]
        }
    ]
}
```

[^1]: [使用 .zip 封存檔部署 Python Lambda 函數](https://docs.aws.amazon.com/zh_tw/lambda/latest/dg/python-package.html)
[^2]: [Policies and Permissions in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html?icmpid=docs_amazons3_console)
