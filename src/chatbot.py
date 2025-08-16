# chatbot.py
# Entry point for chatbot logic
# import the ConversationSummaryBufferMemory, ConversationChain, ChatBedrock,
#  ChatBedrockConverse Langchain modules
#2  write a function for invoking model client connection with Bedrock with profile mode_id and inference 
#parameters - model kwargs
#3. Test out LLM with invoke method
#4. Create a function for ConversationBufferMemory (llm and max tokens limit    )
#5. Create a function for ConversationChain input text + Memory
#6. Chat response using invoke (prompt template) and return response
# links https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html
#https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html
#https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse

def demo_chatbot(messages):
    # Initialize the Bedrock client with profile mode_id and inference parameters
  
    demo_llm = ChatBedrockConverse(
        credentials_profile_name="default",  # Specify your AWS profile name
        model = "us.deepseek.r1-v1:0",
        temperature=0.1,
        max_tokens=1000,
    )
    return demo_llm.invoke(messages)

messages = [
    {
        "role": "user", 
        "content": [{"text":"who is best tennis player."}]
    }
]   

response = demo_chatbot(messages)
print(response)

if __name__ == "__main__":
    print("Chatbot module initialized.")
