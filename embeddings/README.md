https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb

Although fine-tuning can feel like the more natural option—training on data is how GPT learned all of its other knowledge, after all—we generally do not recommend it as a way to teach the model knowledge. Fine-tuning is better suited to teaching specialized tasks or styles, and is less reliable for factual recall.

As an analogy, model weights are like long-term memory. When you fine-tune a model, it's like studying for an exam a week away. When the exam arrives, the model may forget details, or misremember facts it never read.

In contrast, message inputs are like short-term memory. When you insert knowledge into a message, it's like taking an exam with open notes. With notes in hand, the model is more likely to arrive at correct answers.

One downside of text search relative to fine-tuning is that each model is limited by a maximum amount of text it can read at once.

Continuing the analogy, you can think of the model like a student who can only look at a few pages of notes at a time, despite potentially having shelves of textbooks to draw upon.

Therefore, to build a system capable of drawing upon large quantities of text to answer questions, we recommend using a Search-Ask approach.

1. Fine-Tuning :
    - Pros :
        - Can be used to teach specialized tasks or styles
    - Cons :
        - Less reliable for factual recall

2. Message Passing :
    - Pros :
        - Can be used to teach general knowledge
        - Can be used to teach factual recall
    - Cons :
        - Can't be used to teach large quantities of text to answer questions

3. Search-Ask :
    - Pros :
        - Can be used to teach general knowledge
        - Can be used to teach large quantities of text to answer questions
          """