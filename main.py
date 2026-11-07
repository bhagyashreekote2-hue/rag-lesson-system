import json
import time
from generator import generate_lesson
from evaluator import evaluate_lesson

# Load configs
rubric = json.load(open("rubric.json"))
try:
    memory = json.load(open("memory.json"))
except:
    memory = {"failures": []}

topic = "Introduction to RAG (Retrieval-Augmented Generation)"
rejection_log = []
feedback = ""

print(f"Starting Self-Evaluating Lesson System for: {topic}")

for attempt in range(1, 4):  # Max 3 attempts (1 + 2 retries)
    print(f"\n--- Attempt {attempt} ---")
    lesson = generate_lesson(topic, feedback, str(memory["failures"][-5:]))

    result = evaluate_lesson(lesson, rubric)
    print(f"Result: {result}")

    if result.get("overall_pass"):
        print("✅ PASSED! Saving final lesson.")
        with open("final_lesson.md", "w", encoding="utf-8") as f:
            f.write(lesson)
        # Update memory with success
        memory["failures"].append({"topic": topic, "success_attempt": attempt})
        json.dump(memory, open("memory.json","w"), indent=2)
        break
    else:
        fails = [c for c in result["checks"] if not c["pass"]]
        rejection_log.append({"attempt": attempt, "fails": fails, "lesson_preview": lesson[:300]})
        json.dump(rejection_log, open("rejection_log.json","w"), indent=2)

        # Build feedback for next loop - Self-evolving logic
        feedback = "You FAILED last time on: " + "; ".join([f"{x['id']} - {x['reason']}" for x in fails])
        
        # Self-evolving: If same check fails 3 times historically, sharpen prompt
        if len(memory["failures"]) >= 3:
            memory["failures"].append({"failed_checks": fails})

        if attempt == 3:
            print("❌ Failed after 3 attempts. Check rejection_log.json")
