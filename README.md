# chatbot
Building a Chatbot using Amazon Bedrock

pre-requisite:
1. VS code - add amazon Q.
2. install python version 3.12.4st
3. Install AWS Cli : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  3a. aws --version
  3b. Extension - AWS Toolkit and AWS Boto3
4. Configure IAM Rol for VSCode - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure.files.html
    4a. Create IAM Role - goto aws , search IAM, and create user, and attach the policy. then goto security restriction 
    4b. aws configure
    4c. Provide credentials
    4d. aws s3 ls
5. Anaconda navigator Download
     ### after installing the anaconda - source ~/anaconda3/bin/activate
     after that, launch anaconda navigator - anaconda-navigator
7. open vs code from anaconda navigator - very important
8. install boto3 - pip install boto3 == 1.37.11
9. install langchain - pip install langchain == 0.3.0
10. install langchain-AWS Module - pip install langchain-aws = 0.2.15
11. install strealit - pip install streamlit == 1.43.1
12. install transformer - pip install transformers
13. install PyYAML - pip install PyYAML
14. pip install -U langchain-aws
   
