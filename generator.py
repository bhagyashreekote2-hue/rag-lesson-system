from openai import OpenAI
client = OpenAI()

GENERATOR_PROMPT = """
You are a teacher for 12th-pass Indian students. Limited English. Non-English medium, wants AI career.
Topic: {topic}

Goal: Write standalone beginner lesson, zero background can understand.

Rules:
- Very simple English, short sentences. Hinglish ok if helps.
- Structure: Hook -> What is RAG -> Why needed -> How it works (3 steps) -> Real-life analogy (library / open-book exam) -> Full Example Q->Retrieval->Answer -> Where used -> Recap -> Next step
- If you use technical word like LLM, vector, embedding, database - MUST explain in brackets same sentence like LLM (AI that writes text)
- MUST include library analogy, MUST include refund policy example

Previous feedback if any: {feedback}
Memory of past failures: {memory}

Write lesson in Markdown.
"""

def generate_lesson(topic, feedback="", memory=""):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": GENERATOR_PROMPT.format(topic=topic, feedback=feedback, memory=memory)}],
        temperature=0.7
    )
    return resp.choices[0].message.content
