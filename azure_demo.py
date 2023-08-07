#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Note: The openai-python library support for Azure OpenAI is in preview.

import os
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

# engine = "gpt-35-turbo"
engine = "gpt-35-turbo-16k"
messages = [
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "Azure OpenAI 是否支持客户管理的密钥？"},
        {"role": "assistant", "content": "是的，Azure OpenAI 支持客户管理的密钥。"},
        {"role": "user", "content": "其他 Azure AI 服务是否也支持此功能？"}
    ]
response = openai.ChatCompletion.create(
    engine=engine,
    messages=messages
)

# print(response)
print(response['choices'][0]['message']['content'])