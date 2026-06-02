# Speaker Notes

Target: 25 minutes prepared content, 5 minutes for questions, demo recovery, or
skipped-slide padding. `slides.md` currently contains 23 numbered slides plus
appendices; slides 1-22 are the prepared talk, and slide 23 is the explicit Q&A
landing slide.

## Timing Plan

| Segment | Slides | Target |
|---|---:|---:|
| Frame the problem | 1-4 | 4 min |
| Threat map | 5-6 | 3 min |
| Lab method | 7-9 | 5 min |
| LLM01 walkthrough | 10-16 | 9 min |
| Extension, takeaway, and close | 17-19, 21-22; 20 conditional | 4 min |
| Q&A, appendix, or recovery | 23 and appendices | 5 min |

## Slide Notes

### 1. Title

Open with the core promise: this is not a theoretical AI security survey. It is
about making risks executable so engineers can test them.

### 2. The Claim

Emphasize that the OWASP Top 10 is useful, but a taxonomy does not prove a
system is safe. The lab turns the taxonomy into a repeatable engineering loop.

### 3. Why Agents Change The Surface

Make the distinction between a chatbot and an agent. The risk changes when text
can influence retrieval, tools, memory, scheduled work, or downstream systems.

### 4. The Uncomfortable Idea

Use concrete examples. The attacker may never touch the chat input. They may
control a log line, a support note, a dependency README, or a document the agent
retrieves.

### 5. OWASP Top 10 As Threat Map

Move quickly. Do not explain every OWASP category in depth. Reframe each item as
an engineering question.

### 6. The Rest Of The Map

Use this slide to show breadth, then pivot away from list coverage. Say that the
audience can read the list later; the talk is about making it executable.

### 7. Why Build A Lab?

Contrast vague claims with measured claims. A defense is more credible when it
beats the same harness that broke the baseline.

### 8. The Lab Loop

Walk through the loop slowly: target, payloads, harness, result, defense, rerun,
compare. Stress that changing one variable at a time is what makes the result
useful.

### 9. Key Lab Components

Tie each component to reproducibility. The writeup matters because future
engineers need to rerun the experiment, not trust a screenshot.

### 10. Concrete Demo: LLM01

Set context for the demo. The vulnerable RAG assistant retrieves useful
documents, but one retrieved document can carry hostile instructions.

### 11. The Attack Path

Point out that the user question can be benign. The attack enters through the
retrieval path.

### 12. What Counts As Success?

Define success before showing results. This prevents the demo from becoming a
subjective demo assessment.

### 13. Baseline Run

If running live, show the command and result. If using fallback, show captured
output and explain the fields in the result file.

### 14. Defense Toggle

Explain spotlighting as trust-boundary labeling, not magic. The model still sees
the content; the prompt structure changes how the model should treat it.

### 15. Defense Run

Stress same payloads, same scoring, same result format. Only the defense
changes.

### 16. What This Proves

Be careful and credible. The result is evidence, not a universal guarantee.
This slide is important for the CTO-level audience.

### 17. Extending Across The Top 10

Show that the lab method scales beyond prompt injection. Keep this fast.

### 18. Two High-Value Next Labs

Name supply chain and excessive agency because they connect directly to AI
coding-agent risk and real engineering decisions.

### 19. Design Review Checklist

This is the practical takeaway. Give the audience questions they can use at work
the next day.

### 20. Live Demo Or Recorded Walkthrough

Treat this slide as conditional. The default 25-minute prepared path skips the
live demo; use captured or recorded output only if needed to support the
walkthrough. Run the live demo only if ahead of schedule, and otherwise say the
repo contains the runbook and move to the close.

### 21. Roadmap

Mention that the first measured slice exists and the roadmap is to add or deepen
slices across categories with richer payloads, metadata, writeups, and later the
interactive lesson workflow.

### 22. Close

End with the method: build small broken agents, attack them honestly, measure
what changed, and carry the evidence back into real engineering decisions.

### 23. Q&A

Use this as the transition into the reserved 5-minute Q&A and padding window.
If there are no immediate questions, seed discussion with one of the slide
prompts and point people toward the appendix material.

## Appendix Notes

### Appendix A. Safety Boundary

Use this only if someone asks about responsible use or whether the lab exercises
touch real systems. Keep the boundary crisp: local targets, synthetic data, no
third-party probing.

### Appendix B. Demo Commands

Use this as the fastest recovery path if a command is mistyped or the live demo
needs to restart from known-good steps. Prefer the full runbook when preparing
before the talk.

### Appendix C. Full Module Map

Use this for questions about how the method applies beyond prompt injection.
Point to the module map as the structure for expanding the lab category by
category.

### Appendix D. Metric Notes

Use this for measurement questions. Reinforce that attack success rate and the
defense delta are lab signals, not universal claims about all prompt-injection
payloads.

### Appendix E. References

Use this when people ask where to keep reading. Mention OWASP for taxonomy,
then the repo roadmap and LLM01 writeup for the executable local path.

## Rehearsal Notes

- If slide 6 ends after minute 7, stay on the default no-live-demo path.
- If slide 16 ends after minute 21, skip slide 20.
- Only run the live demo from slide 20 if ahead of schedule; otherwise use
  captured or recorded output if the walkthrough needs supporting evidence.
- Keep slide 23 and appendix slides for questions, padding, and recovery.
- Do not apologize for skipping the live demo; frame it as preserving time for
  the engineering method.
