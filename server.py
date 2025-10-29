from fastapi import FastAPI
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Cho phép mọi domain (để website Hostinger có thể gọi)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Khởi tạo OpenAI client
openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.post("/api/chatkit/session")
def create_chatkit_session():
    # Tạo session ChatKit mới
    session = openai.chatkit.sessions.create({
        "workflow_id": "wf_68f5d9e22bc881908eb75de2c117dab60616f00edcb41e00"  # thay bằng Workflow ID trong Agent Builder
    })
    return {"client_secret": session.client_secret}
