# Pollster - Mini Project Report

## Title
Pollster: Voting System using Django

## Objective
To develop a web-based voting application where users can answer multiple-choice questions and view the updated results.

## Problem Statement
Collecting opinions manually can be slow and difficult to summarize. The proposed application provides a simple digital platform for creating polls, collecting votes, and displaying results automatically.

## Proposed Solution
The application uses Django to handle URLs, views, database operations and templates. SQLite stores questions, choices and vote counts. Django Admin is used to manage the poll data.

## Modules
1. Poll listing module
2. Voting module
3. Results module
4. Admin management module

## Database Design
- Question: question_text, pub_date
- Choice: choice_text, votes, question (foreign key)

One Question can have many Choices.

## Future Scope
- User authentication
- One-vote-per-user restriction
- Poll expiry dates
- Charts and analytics
- Deployment to a cloud platform
