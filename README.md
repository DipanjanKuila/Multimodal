# Multimodal GPT-4o Model Integration with Gradio

This project demonstrates how to integrate **Azure OpenAI's GPT-4o model** with a **Gradio-based user interface**. The application allows users to interact with the model by inputting both **text and images** and receiving multimodal responses from the GPT-4o model.

## Project Overview

This Python script provides a simple yet powerful demonstration of multimodal AI interaction using **LangChain**, **Gradio**, and **Azure OpenAI GPT-4o**. It enables users to input text and images and generates intelligent responses based on both inputs. The project uses Gradio to create a web-based interface, making it easy for users to interact with the model.

### Features:
- **Multimodal Input Processing**: Accepts both text and images as input and generates appropriate responses based on the GPT-4o model's understanding.
- **Image-to-Base64 Encoding**: Converts user-uploaded images into base64 format, allowing easy embedding and transmission over the web.
- **Azure GPT-4o Model Integration**: The script integrates with Azure OpenAI’s GPT-4o, capable of processing multimodal (text and image) inputs.

### How It Works

1. **Environment Configuration**:
   The script uses environment variables to configure the Azure OpenAI connection:
   - `AZURE_OPENAI_API_KEY`: Your API key for authenticating requests.
   - `AZURE_OPENAI_ENDPOINT`: The endpoint for Azure OpenAI services.
   - `OPENAI_API_VERSION`: Version of the OpenAI API being used .
   
  
