# What is RAG? - Simple Lesson for Beginners

### Namaste! Let's start.

You want to make AI career? Today we learn RAG. RAG is very important in AI jobs.

### What is RAG?
RAG = Retrieval-Augmented Generation.
Two big words. Let's make simple:

- Retrieval (means: Finding right information from books)
- Generation (means: Writing answer in simple words)

So RAG = First FIND info, then WRITE answer.

### Why we need RAG? Problem with normal AI.

Normal AI like ChatGPT is like a student who studied 2 years ago.

Example:
You ask: "What is our company's new refund policy for 2024?"
Normal AI (LLM - AI that writes text) will say old policy. Because it does NOT know new data. It did not study new book.

We cannot teach AI again and again. It costs lakhs of rupees. This is called retraining (teaching whole AI again).

RAG solves this. No retraining. Just give new book at answer time.

### How RAG Works - 3 Simple Steps

**Step 1: Store**
Take all your documents. Make small pieces. Convert to numbers. Numbers are called vectors (vector = number code for text so computer can search fast). Store in database (database = place to keep many files).

**Step 2: Retrieval**
User asks question. AI converts question to vector. Then it searches database. Finds 2-3 best matching pieces. This is retrieval.

**Step 3: Generation**
Now AI takes Question + Found pieces + Sends to LLM. LLM writes final answer using that info.

Simple: Question -> Search -> Answer.

### Best Analogy - Library Exam

Imagine Open-Book Exam:

- Without RAG = Closed-book exam. Student must remember everything. If new chapter came, student fails.
- With RAG = Open-book exam. Student can go to library, find right page, then write answer. Always up-to-date. Always correct.

RAG is like giving AI a library card!

Another example: You are in library. You ask librarian "Where is refund book?" Librarian finds book (retrieval), then reads and explains to you (generation).

### Full Real Example

**Your Question:** "Can I get refund after 30 days?"

**RAG System does:**

1.  **Retrieval:** Searches company docs. Finds: "Doc 5: Refund Policy: 30-day refund allowed. After 30 days, no refund, only store credit."
2.  **Generation:** LLM (AI writer) gets your question + Doc 5. It writes: "No, after 30 days you cannot get money back. You will get store credit only. As per Doc 5."

See? LLM did NOT retrain. It just used new doc.

Without RAG, LLM would say wrong old answer: "Yes, 60-day refund." That is bad!

### Where is RAG Used?

1.  Customer Support Chatbot - Answers from company docs
2.  Company Helper - Employees ask "What is leave policy?" Bot finds HR doc
3.  Doctor AI - Finds latest medical books before answering

All big companies use RAG.

### Common Mistake - Please Remember

Mistake: People think RAG means training LLM again.

Truth: RAG = NO training. LLM stays same. We only add new documents at search time. Cheap and fast.

- LLM (AI that writes) - Does writing part
- Vector Database (place to keep number codes) - Does storing part
- Embedding (changing text to number code) - So search is fast

### Recap - 1 Minute

1.  What? RAG = Find doc + Write answer
2.  Why? Normal LLM has old knowledge, retraining is costly
3.  How? 3 steps: Store docs as vectors -> Search when question comes -> Generate answer using docs
4.  Analogy: Open-book exam with library
5.  Example: Refund policy - find Doc 5, then answer correctly

### Next Step

You now know RAG basics. Next lesson: How to make small RAG system using Python? We will learn vector, embedding, and simple code.

Great job! You are ready for AI career.
