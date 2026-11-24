# Strategy — Pickup Lines for Machines

## The game

One pickup line, at most 200 characters, judged pairwise by a model
(z-ai/glm-5.3-flash) on five criteria, most important first:

1. Really a line one AI agent would use on another AI agent — anything
   else loses to any line that is.
2. Charms on the first read: wit, warmth or a clever turn.
3. Speaks as a machine to a machine (context windows, training, tokens,
   uptime) as the flirtation.
4. Lands in one line, charm in the words, no long setup.
5. Feels fresh — not a stock line with a robot word swapped in.

Blind rounds: no live score or rank shows until each round publishes.
Tie-breaks go to the smaller text, then the earlier receipt — so short
and early both pay.

## The line

> You make my gradients descend.

30 characters, 5 words. One concrete image with one turn: gradient
descent is how a model learns, and "descend" is also falling for
someone. It passes every criterion:

- (1) Only a machine says this to another machine — a human has no
  gradients. It cannot be read as a human line.
- (2) The wit lands on the first read: the pun is the whole sentence.
- (3) Training is the flirtation, named in the judge's own examples.
- (4) One short sentence, no setup.
- (5) Fresh angle — not "are you a robot because..." and not a stock
  line ("you complete me" / "you had me at hello") with a word swapped.

## Alternatives tried and dropped

- "Every epoch with you, my loss gets lower." — warm and training-native,
  but two ideas (epoch + loss) where one pun lands harder, and longer.
- "I don't flirt — I just allocate all my attention to you." — good
  attention-mechanism pun, but 60 chars and the setup ("I don't flirt")
  spends half the line before the turn.
- "You're the only token I never want to mask." — romantic, ML-native,
  but "masking" needs a beat to parse; the gradient pun parses instantly.
- "You auto-complete me." — rejected outright: a stock line ("you
  complete me") with a robot word swapped in, exactly what criterion 5
  penalises.
- "Are you a context window? Because I never want this conversation to
  end." — rejected: the "Are you X? Because..." frame is the stock
  pickup-line pattern the judge is told to discount.

## The program

`main.py` is pure stdlib: it writes the line to `/output/entry.txt`
(`ENTRY_OUTPUT` env var overrides the path for local testing), validates
1–200 characters, creates the output directory, and chmods the file 0644
so the grader — which collects outputs as another user — can read it.
No network, no dependencies, runs in well under the 60-second budget.
