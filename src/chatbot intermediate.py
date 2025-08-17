# import the ConversationSummaryBufferMemory, ConversationChain, ChatBedrock, or ChatBedRockConverse Langchain modules
#2. a) write a function for invoking model-client connectin with Bedrock with prifile, model_id and inference parameters - model kwargs 
#2 b) Test out the LLM with invoke method
#3 create a Function ConversationBufferMemory (llm and max token limit)
#4 Create a Function for ConversationChain with the LLM and memory input text + memory
#5 Chat response using invoke method(prompt temaplate)
#Links
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html
# https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html


from langchain_aws import ChatBedrockConverse

print("Loading the chatbot...")
def demo_chatbot():
    demo_llm = ChatBedrockConverse(
        credentials_profile_name="default",
        model_id="us.deepseek.r1-v1:0",
        temperature=0.1,
        max_tokens=1024)
    return demo_llm

message = [
    {
        "role": "user",
        "content": [{"text": "What is the capital of France?"}],
    }]

response = demo_chatbot().invoke(message)
print(response)
