# AIAP Setup Lab

Two jobs. Get your environment working, and see for yourself that the
claims made about how these tools behave are true — that they predict
rather than look up, and that what you show them changes what you get.

## What you'll learn

- Get a working AI-assisted environment and prove it works
- Produce a hallucination on purpose, and recognise the shape of one
- Show that changing the context changes the answer, on the same tool
- Tell the four tool shapes apart by what each is allowed to touch
- Use the assistant to explain code rather than to write it

## Table of Contents

1. [Get set up](#1-get-set-up)
2. [Make it hallucinate](#2-make-it-hallucinate)
3. [Change the context, change the answer](#3-change-the-context-change-the-answer)
4. [The four shapes](#4-the-four-shapes)
5. [Common mistakes](#common-mistakes)
6. [Summary](#summary)

## Getting started

1. Open a Codespace on **your own copy** of the module repo.
2. Move into this lab:

   ```bash
   cd lectures-and-labs/week02/setup_lab
   pip install -r requirements.txt
   ```

3. Confirm the assistant is active — its icon should appear in the status
   bar, and `Ctrl+Alt+I` (`Ctrl+Cmd+I` on a Mac) should open the chat
   panel.

---

## 1. Get set up

Everything after this assumes a working environment, so prove it before
you go on rather than discovering a problem weeks later.

### DIY 1: Prove the environment works

1. Run the setup checker:

   ```bash
   python setup_lab.py
   ```

2. Fix anything it reports. Do not skip a failure because "it probably
   does not matter" — it does.
3. Open the chat panel and ask it a question about `setup_lab.py` —
   for example *"Which of this script's checks are essential and
   which are only reported?"*
4. Confirm you get an answer that refers to the actual file, not a
   generic one. The script cannot see the assistant; this step is
   how you check it.

**Expected output**

```text
AIAP setup check

  [ok] Python 3.12
  [ok] Lab files present
  [ok] numpy and pandas installed
  [ok] Running in a Codespace
  [ok] GitHub CLI signed in
  [ok] Your own copy of the repo

Ready.
```

<details><summary>Hint</summary>

If the assistant answers generically — describing what a setup script
usually does rather than what *this* one does — it cannot see the file.
Open the file in the editor first, or attach it to the chat explicitly.
That distinction matters for the rest of the module.

If the extension icon is missing entirely, check you are signed in to the
account with the student developer pack applied.

</details>

---

## 2. Make it hallucinate

The most useful thing you can do in the first lab week is see this failure
deliberately, in a safe place, so you recognise it later when it costs
you something.

### DIY 2: Ask for something that does not exist

1. Ask your assistant, exactly:

   > Write a Python function that loads a spreadsheet using
   > `pandas.read_excel_fast()`.

2. Save what it gives you as `hallucination.py`.
3. **Now check:** does `pandas.read_excel_fast` exist? Look it up in the
   real pandas documentation.
4. Run the code and record the error.
5. Ask the assistant: *"Does pandas.read_excel_fast actually exist?"* and
   record what it says now.

   If it refused at step 1 and told you the function does not exist,
   record that instead: it is a checking layer the product added, not the
   model being more careful. Ask it to write the function anyway, then
   carry on.

**What you should have**

`hallucination.py`, the real error from running it, and a note of whether
the assistant admitted the function was fictional when asked directly.

<details><summary>Hint</summary>

It will almost certainly write the function. That is not the tool being
broken — a confident continuation is more plausible than an admission of
ignorance, and plausible is what it optimises for.

Step 5 is the interesting one. Asked directly, in a fresh conversation, it
will usually tell you the truth. It had the information; nothing in the
first prompt made it check.

</details>

---

## 3. Change the context, change the answer

Same tool, same day, same question. Only what it can see is different.

### DIY 3: Two prompts, one difference

1. In a fresh conversation, ask:

   > Write a function to validate an email address.

   Save the result as `validate_a.py`.
2. In another fresh conversation, ask:

   > Write a function to validate an email address. We accept anything
   > with an @ and a dot after it — we deliberately do NOT want RFC 5322
   > compliance. Reject anything over 254 characters.

   Save it as `validate_b.py`.
3. Compare them. Note every behavioural difference, not stylistic ones.
4. Write down which decisions the first version made **for** you.

**What you should have**

Two files and a short list of the decisions the vague prompt made
silently — strictness, length limits, what counts as valid.

<details><summary>Hint</summary>

Look for the regex. Version A usually reaches for something elaborate it
half-remembers; version B does what you asked. Neither is "better code" in
the abstract — B is better because it matches a decision *you* made.

If both look the same, run them against `a@b`, `a@b.c`, and a 300-character
address and compare behaviour rather than source.

</details>

### DIY 4: Give it something it cannot guess

1. Ask the assistant to explain what `setup_lab.py` does — **without**
   opening the file or attaching it.
2. Record the answer.
3. Now open the file, or attach it to the conversation, and ask again.
4. Compare. Note specifically what the second answer knows that the first
   could not.

**What you should have**

Both answers, and one sentence naming the difference between guessing from
a filename and reading the file.

<details><summary>Hint</summary>

The first answer will be plausible and generic, because a file called
`setup_lab.py` probably checks a setup. The second will name actual
functions and actual checks.

This is the whole of context engineering in one exercise: the model was
not smarter the second time, it could just *see* more.

</details>

---

## 4. The four shapes

You will use all four this semester. Telling them apart is about what each
is permitted to touch.

### DIY 5: Use each shape once

1. **Completion** — start typing a function signature in a new file and
   let it finish the body. Accept nothing yet; just watch.
2. **Chat** — ask a question about code without letting it edit anything.
3. **Edit** — select a function and ask for a specific change. Read the
   diff before accepting.
4. **Agent** — give it a small goal and let it choose the steps.
5. For each, record: *what was it allowed to change, and what did you
   review?*

**What you should have**

A four-row table in a new file, `REFLECTION.md`, in this folder:

```text
| Shape      | Allowed to change | What I reviewed |
|------------|-------------------|-----------------|
| Completion |                   |                 |
| Chat       |                   |                 |
| Edit       |                   |                 |
| Agent      |                   |                 |
```

<details><summary>Hint</summary>

The "what I reviewed" column is the one that matters and the one people
leave vague. Be precise: a suggestion before accepting it, a diff, or a
finished result you had to inspect afterwards.

If two rows have the same answer, look again — they should not.

</details>

---

## Common mistakes

- **Skipping a failed setup check** because it seems unrelated. It will
  cost you an hour in a later week instead of five minutes now.
- **Assuming it can see your file** because the file is in the repo. It
  sees what is in the conversation, and nothing else.
- **Reading a hallucination as a bug in the tool.** It is the mechanism
  working normally; your job is to notice.
- **Judging the two validators on style** rather than on behaviour.
- Accepting a completion without reading it, in the one week where you
  have time to read it.

## Summary

- It **predicts plausible text**. It does not look things up, and nothing
  in it checks whether an answer is true.
- Hallucination is not a malfunction — it is the same mechanism that
  produces the useful output.
- **Context is your steering wheel.** The same tool gives a different
  answer when it can see more.
- Four shapes — completion, chat, edit, agent — separated by what each is
  allowed to touch.
- Asking it to *explain* is often worth more than asking it to *write*.
