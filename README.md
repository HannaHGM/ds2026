# Intermediate Data Science 2026 — your course folder

EDIT This folder is where you do all your work for the module. It comes with an AI
tutor already set up: when you open it in VS Code, the AI assistant coaches you
towards answers instead of handing them over.

Follow the steps in order. You start using the terminal in session 1.1.

---

## Before week 1

1. **Create a GitHub account** at [github.com](https://github.com) if you don't
   have one. Pick a username you're happy for tutors to see.
2. **Apply for GitHub Education** (recommended, free) at
   [github.com/education](https://github.com/education). It gives you the full
   version of GitHub Copilot. **Verification can take several days and is
   re-checked from time to time, so apply now, not in week 1.** If you aren't
   verified, you still get Copilot Free — see [If Copilot isn't
   working](#if-copilot-isnt-working).
3. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com).
4. **Install Git.**
   - Windows: download from [git-scm.com](https://git-scm.com) and accept the
     default options.
   - Mac: open the Terminal app, type `git --version`, press Enter, and accept
     the offer to install the developer tools.
5. **Install Python** from [python.org/downloads](https://www.python.org/downloads/).
   The 1.1 Prep page on Canvas shows how to check it worked.

## Week 1 — set up your course folder

1. **Download** `ds2026.zip` from the 1.1 Prep page on Canvas.
2. **Unzip it in the place you chose for this course.** We suggest
   `Documents/LIS`, so the folder ends up at `Documents/LIS/ds2026`.
3. In VS Code: **File → Open Folder…** and choose `ds2026`.
4. VS Code asks *"Do you trust the authors of the files in this folder?"* —
   click **Yes, I trust the authors**. If you don't, the AI tutor stays off.
5. A message in the bottom-right corner offers to install **recommended
   extensions** (Python and Jupyter) — click **Install**.
6. Click the **Accounts** icon (the person, bottom-left) → **Sign in with
   GitHub** to use Copilot, and follow the prompts.
7. **Check it works:** open the chat (**View → Chat**). In the dropdown at the
   bottom of the chat box, choose **Tutor**. Ask it something from this week.
   It should ask for your best guess before explaining.

## How this folder works

```
ds2026/               your course folder, and from week 2 your GitHub repository
├── week1/ … week9/   your lab notebooks and notes
├── project/          your assessed project, with its own README
├── requirements.txt  the packages you need (you create it in week 1)
├── .venv/            your virtual environment (you create it; never uploaded)
└── (hidden files)    the AI tutor setup: don't delete them
```

- **Always open `ds2026` itself.** Don't open `project/` or a week folder on its
  own: the tutor and Git are set up for the whole folder.
- **Hidden files.** `.github`, `.vscode` and `AGENTS.md` hold the tutor setup.
  `.gitignore` keeps them, `.venv/`, your data and downloaded slides out of
  your repository.

## Using the AI tutor

- **Pick "Tutor" in the chat dropdown.** It explains, makes you try first, and
  tests you. It can read your files but can't change them — by design.
- **Autocomplete is switched off in this folder.** VS Code won't write code for
  you as you type. That's deliberate: code you didn't think through doesn't
  stick, and you'll need it in the presentation Q&A.
- **Want a straight answer?** Say *"just give me the answer"* and you'll get
  one, no lecture, for a concept or a setup problem. It never writes your code:
  code always comes as a skeleton for you to finish.
- **AI is for learning and troubleshooting, not for writing your code.** Use it
  to explain concepts, give you examples and exercises, and fix setup problems.
  The code, analysis and text you submit must be your own. Declare any AI use
  in your project README: the template in `project/README.md` shows how. The
  full rules are on the AI policy page on Canvas.

## Week 2 — put your project on GitHub

You'll do this in lab 2.3.

Your whole `ds2026` folder becomes one repository: your project and your lab
notebooks, so your work across the term is in one place.

1. Open `ds2026` in VS Code, as always.
2. Open the **Source Control** panel (the branching icon on the left) and click
   **Initialize Repository**.
3. Type a message such as `Start course repository` and click **Commit**.
4. Click **Publish Branch** → **Publish to GitHub** → choose **private**.
5. On GitHub, open your repository → **Settings** → **Collaborators** and invite
   the module staff (their GitHub usernames are on Canvas).
6. The same commit-and-push steps in the terminal (**Terminal → New Terminal**):

   ```bash
   git status
   git add project/README.md
   git commit -m "Describe the research question"
   git push
   ```

Your repository's GitHub link is what you submit for Assessments #2 and #3.
Put your student ID and the repository name (for example
`M5006-ds2026-studentnumber`) in `project/README.md`.

## If Copilot isn't working

- **Not verified yet?** Copilot Free still works, with a monthly limit on chat
  and suggestions. Everything in this folder still applies.
- **Out of Copilot chats?** The allowance resets each month. Until then, keep
  working without the assistant: the course materials, the Data Dojo and office
  hours are there for exactly this.
- **Can't sign in to Copilot?** Check you are signed in to GitHub in VS Code
  (Accounts icon, bottom-left). If it still fails, tell us in class or on the
  forum.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Tutor** isn't in the chat dropdown | You opened a week folder, or didn't trust the folder. Reopen `ds2026` and click **Yes, I trust the authors**. |
| Source Control shows no repository, or GitStudio shows nothing | You opened `project/` or a week folder on its own. Reopen `ds2026`. |
| You accidentally created a second repository inside `project/` | Delete the hidden `.git` folder inside `project/` (Mac Finder: **Cmd+Shift+.** shows hidden files; Windows Explorer: **View → Show → Hidden items**). Your `ds2026` repository is unaffected. |
| The hidden folders are missing | Unzip the download again and move the whole `ds2026` folder, not the files inside it. |
