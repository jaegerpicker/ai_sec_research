# Talk Rehearsal

Use this worksheet for full delivery runs before the June 20, 2026 polish
deadline. The default path is a 25-minute prepared talk without a live demo,
followed by 5 minutes for questions.

## Delivery Rule

The talk must work without terminal interaction. Use the live demo only when
slide 20 is reached by minute 18 and the lab is already in a known-good state.
Otherwise, use the captured result on slides 13-16 and preserve the Q&A window.

## Timing Checkpoints

| Elapsed | Slides | Goal | Cut if behind |
|---:|---:|---|---|
| 0:00-4:00 | 1-4 | Frame agent-specific risk and the untrusted-text problem. | Shorten examples on slide 4. |
| 4:00-7:00 | 5-6 | Present the Top 10 as an engineering map. | Read only the category names and questions. |
| 7:00-12:00 | 7-9 | Explain the repeatable lab loop and safety boundary. | Compress the component inventory on slide 9. |
| 12:00-15:00 | 10-12 | Establish the LLM01 target, attack path, and success metric. | Keep only the benign-user-input point on slide 11. |
| 15:00-21:00 | 13-16 | Compare baseline, defense, rerun, and measured claim. | Show the captured summary fields without narrating each payload. |
| 21:00-23:00 | 17-19 | Generalize the method and deliver the review checklist. | Skip slide 18 and name the two modules verbally. |
| 23:00-25:00 | 21-22 | Give the roadmap and close. | Reduce slide 21 to one sentence; do not cut the closing line. |
| 25:00-30:00 | 23 | Questions, padding, or recovery. | Stop prepared content at minute 25. |

Slide 20 is conditional and is not part of the default timing path.

## Live-Demo Branch

Take this branch only when all conditions are true:

- Slide 16 ends by minute 16:30.
- Slide 20 is reached by minute 18:00.
- The comparison command passed during preflight.
- The terminal is readable from the back of the room.
- At least 7 minutes remain before the Q&A boundary.

Hard limits:

- Stop the demo after 5 minutes even if a command is still running.
- Use the captured output after the first environmental failure.
- Compress slide 21, but keep slide 22 and begin Q&A by minute 25.

## Preflight

### Day Before

- [ ] Open the Google Slides delivery deck and verify presenter access.
- [ ] Confirm `exports/slides.pdf` opens as the offline deck.
- [ ] Run the measured comparison from `demo-runbook.md`.
- [ ] Confirm both captured output files are available locally.
- [ ] Charge the presentation laptop and pack the required display adapter.
- [ ] Disable notifications, sleep, and automatic updates for the talk window.

### In The Room

- [ ] Verify the first and last slides fit the projector.
- [ ] Check that cyan, amber, and body text remain distinguishable.
- [ ] Test the clicker and presenter-view display arrangement.
- [ ] Increase terminal font size and hide unrelated windows.
- [ ] Put the PDF, demo runbook, and captured output in the same local folder.
- [ ] Start a visible 30-minute timer.

## Full-Run Log

Copy this section for each rehearsal.

```text
Date:
Delivery deck version or commit:
Path: default / live demo

Slide 4 checkpoint:
Slide 6 checkpoint:
Slide 9 checkpoint:
Slide 12 checkpoint:
Slide 16 checkpoint:
Slide 19 checkpoint:
Slide 22 checkpoint:
Q&A start:

Demo result:
Words or sections that caused hesitation:
Slides that felt crowded:
Audience questions or reviewer feedback:
Cuts for the next run:
Keep unchanged:
```

## Pass Criteria

A full run passes when:

- slide 22 finishes at or before minute 25,
- the main claim, lab loop, measured result, limitation, and checklist all land,
- the talk remains coherent when slide 20 is skipped,
- no recovery step requires network access,
- Q&A begins with at least 5 minutes remaining.

