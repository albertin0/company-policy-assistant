# company-policy-assistant
The Employee AI Assistant is a smart, conversational tool that streamlines work by automating routine queries and tasks. It supports employees with policy details, task tracking, HR queries, and document searches. Integrated with company systems, it provides fast, accurate, and context-aware responses, boosting efficiency and teamwork.


Running steps:
1. Run Docker Desktop
2. Start Qdrant (local): docker run -p 6333:6333 qdrant/qdrant
3. Install dependencies: pip install -r requirements.txt
4. Run FastAPI: uvicorn app.main:app --reload
5. Open your browser and go to: http://127.0.0.1:8000/docs
6. You’ll see the Swagger UI interface:
    Click the POST /ask endpoint.
    Click “Try it out”.
    In the request body, type: {
                                    "question": "What is the company leave policy for new employees?"
                                }
7. You’ll see the response appear directly below: {
  "answer": "[Groq LLM Response]\n\nUse the following company policy information..."
}