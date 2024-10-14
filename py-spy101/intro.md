## Learning Outcomes
This executable tutorial aims to show how you can use py-spy to be able to profile and monitor your codebase. This will allow you to identify problematic code quicker, and get a better overview of where your code is spending most of its time.

We hope that you will be able to use py-spy in your DevOps work, and hopefully be able to utilize it after this tutorial.

## Prerequisites
Basic Python Knowledge
Some Basic Knowledge about using a terminal (UNIX commands, we will be using Ubuntu here)

## Motivation
Py-spy is crucial for DevOps as it provides real-time, low-overhead profiling of Python applications in both development and production. It enables teams to diagnose performance issues on live systems without requiring restarts or code changes, ensuring minimal disruption. Py-spy’s ability to attach to running processes helps quickly identify bottlenecks, supporting rapid debugging and optimization. This makes it ideal for maintaining performance and reliability throughout the CI/CD pipeline, aligning perfectly with DevOps goals of speed, automation, and continuous improvement.

Quick and easy identification of problematic code during development fits the ethos of DevOps as it enables teams to quicker get code to production, without sacrificing quality. While in production, py-spy can monitor the program due to its low overhead which allows teams to catch problems quicker.

## Overview

1. Install py-spy and Introduction
2. Top subcommand
3. Record subcommand
4. Dump subcommand
5. Additonal options
6. Using py-spy in development
7. Using py-spy in production
