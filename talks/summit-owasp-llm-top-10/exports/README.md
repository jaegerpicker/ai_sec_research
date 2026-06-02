# Talk Exports

Store generated or manually exported presentation artifacts here when they are
ready to publish.

## Expected Exports

- `slides.pdf` - public PDF export of the final deck.
- `google-slides-link.md` - link to the live Google Slides delivery copy when
  it exists.
- `llm01-baseline-output.txt` - captured fallback output for the defense-off
  demo.
- `llm01-defense-output.txt` - captured fallback output for the defense-on demo.

## Rules

- Generated exports should match the repo-native source files.
- Do not commit exports containing secrets, private data, or local machine paths
  that reveal sensitive information.
- Captured output must come from local synthetic lab targets only.
