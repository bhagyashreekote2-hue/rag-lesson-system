# Self-Evaluating Lesson Generator - RAG Intro

**Target:** 12th-pass India, limited English, AI career start

### Architecture
Generator (GPT) -> Evaluator (6 HARD PASS/FAIL) -> If FAIL, regenerate with feedback -> Max 2 retries
Self-Evolving: memory.json remembers failures. If same check fails 3 times, prompt sharpens automatically.

**Why PASS/FAIL not Score?**
Real teaching needs 100% correct. 7/10 is still failure for beginner. Hard gate = only perfect lesson ships.

### Files
- rubric.json - 6 checks: accuracy, simple language, example, jargon explained, key points, flow
- generator.py - Teacher prompt for simple English
- evaluator.py - Strict JSON evaluator
- main.py - Loop + memory + rejection_log.json
- final_lesson.md - Final approved lesson

### How to Run
pip install openai
export OPENAI_API_KEY=xxx
python main.py

Output: final_lesson.md + rejection_log.json

### Lesson Concept
RAG = Retrieval (finding docs) + Generation (writing answer). LLM does NOT retrain. Library / open-book analogy + refund example.

By Bhagyashreekote2-hue
