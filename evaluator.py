from openai import OpenAI
import json
client = OpenAI()

def evaluate_lesson(lesson, rubric):
    prompt = f"""
    You are a STRICT evaluator.
    Rubric (HARD PASS/FAIL): {json.dumps(rubric, indent=2)}
    Lesson to check: {lesson}
    
    For each check, give pass=true/false and reason in 1 line.
    overall_pass = true ONLY if ALL checks pass.
    Return ONLY valid JSON like: {{"checks":[{{"id": "...", "pass": true, "reason": "..."}}], "overall_pass": true}}
    Be very strict. No partial pass.
    """
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt}],
        response_format={"type": "json_object"}
    )
    return json.loads(r.choices[0].message.content)
