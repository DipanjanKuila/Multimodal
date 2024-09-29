import PIL.Image
import gradio as gr
import base64
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
import base64


# Azure OpenAI Credentials
GPT_DEPLOYMENT_NAME = "gpt-4o"
os.environ["AZURE_OPENAI_API_KEY"] = "your api key"
os.environ["AZURE_OPENAI_ENDPOINT"] = "your endpoint"
os.environ["OPENAI_API_VERSION"] = "api_version"

# Initialize Azure GPT-4o Model
gpt_4_vision = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_version=os.environ["OPENAI_API_VERSION"],
    model="gpt-4o",
    azure_deployment=GPT_DEPLOYMENT_NAME,
)

# Image to Base 64 Converter
def image_to_base64(image_path):
    with open(image_path, 'rb') as img:
        encoded_string = base64.b64encode(img.read())
    return encoded_string.decode('utf-8')

# Function that takes User Inputs and displays it on ChatUI
def query_message(history, txt, img):
    if not img:
        history += [(txt, None)]
        return history
    base64_img = image_to_base64(img)
    data_url = f"data:image/jpeg;base64,{base64_img}"
    history += [(f"{txt} ![]({data_url})", None)]
    return history
# Function that takes User Inputs, generates Response, and displays on Chat UI
def llm_response(history, text, img):
    if not img:
        # Handle the case where there is no image
        messages = [HumanMessage(content=[{"type": "text", "text": text}])]
        response = gpt_4_vision.invoke(messages)
        history += [(None, response.content)]
        return history

    else:
        # Convert the image to base64
        img_base64 = image_to_base64(img)

        # Construct the message with image URL and text
        messages = [
            HumanMessage(
                content=[
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{img_base64}",
                        },
                    },
                    {"type": "text", "text": text},
                ]
            )
        ]

        # Invoke the GPT-4o model
        response = gpt_4_vision.invoke(messages)
        history += [(None, response.content)]
        return history


# Interface Code
with gr.Blocks() as app:
    with gr.Row():
        image_box = gr.Image(type="filepath")
    
        chatbot = gr.Chatbot(
            scale=2,
            height=750
        )
    text_box = gr.Textbox(
        placeholder="Enter text and press enter, or upload an image",
        container=False,
    )

    btn = gr.Button("Submit")
    clicked = btn.click(query_message,
                        [chatbot, text_box, image_box],
                        chatbot
                        ).then(llm_response,
                               [chatbot, text_box, image_box],
                               chatbot
                               )
app.queue()
app.launch(debug=True)