# PRGuard
Ensures quality in code production

I am creating a project that ensures good code quality with GitHub ensuring ur code of lines is meaningful and if not, ensuring it is explained in the pull review and also assessing duration of the code and double confirming before merging the review if too little time of review or no comments.

## Project Context

PRGuard is an AI-driven GitHub App that enhances the pull request (PR) code review process by using intelligent multi-agent AI systems. It evaluates code changes for meaningfulness, enforces explanatory comments on flagged code, monitors reviewer interaction quality and time spent, and controls merges with an AI-verified approval process.

## Project Aim

To build a robust, full stack tool integrating with GitHub via webhooks, employing AI agents powered by large language models (LLMs) to automatically analyze PRs, guide reviewers, and ensure high-quality code contributions.

## Project Goals

- Receive and parse GitHub webhook PR events.

- Analyze code diffs with an AI agent to detect redundant or low-quality code.

- Track reviewer activity to flag insufficient review duration or missing comments.

- Enforce mandatory reviewer explanations on flagged changes using an AI-powered comment bot.

- Require a second confirmation step before merging PRs with inadequate reviews.

- Provide a React dashboard showing agent insights, PR statuses, and review metrics.

## Execution Overview

- Backend uses FastAPI for webhook endpoints, agent orchestration, and communication with GitHub APIs.

- Multi-agent architecture with dedicated agents for code analysis, review monitoring, and merge control.

- Agents use OpenAI GPT or LLaMA APIs for code and language understanding.

- Frontend dashboard built with React to display AI review statuses and interactive controls.

- Secure environment configurations for API keys and GitHub app secrets.
