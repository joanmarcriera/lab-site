---
title: "Shipping a Mac App Store release through an API, not a human"
date: 2026-09-05
tags: [macos, app-store, ci-cd]
draft: true
---

App Store review has a way of being invisible right up until it isn't. You sign a build, upload
it, wait, and then either it's fine or you're staring at a rejection with no warning it was coming.
I wanted that entire cycle — sign, export, upload, submit — to run unattended from CI, not from me
clicking through Xcode or Transporter by hand each time, so a release is a merge and a wait rather
than an afternoon.

Getting there took a long tail of small, hard-won fixes, each one a commit of its own: a missing
provisioning profile that Apple flags as warning ITMS-90889 rather than a hard failure, so it's
easy to miss until a human reviewer catches it instead; a code-signing identity that conflicted
with itself once the export step was fully automated; certificates and profiles that needed to be
imported and referenced explicitly rather than picked up implicitly the way Xcode does it locally.
None of these were surprising in isolation, but there's no way to discover the full list except by
running the pipeline for real and fixing whatever breaks next.

The pipeline earned its keep almost immediately. Version 1.9.0 was rejected — not for anything
structural, but because a custom microphone permission dialog used the label "Request Access,"
and Apple's guidance is for that kind of pre-permission prompt to use neutral wording like
"Continue" instead. A small, specific, entirely reasonable ask. The fix was equally small: reword
the dialog, bump to version 1.9.1 build 11, and let the same pipeline that built 1.9.0 build and
submit its replacement.

That's where the automation's own caution became the interesting part of the story. The submission
script deliberately stops and refuses to act whenever App Store Connect reports a submission as
having unresolved issues — a sensible default, because guessing what to do with someone else's
rejected review item is exactly the kind of thing that should require a human's judgement rather
than a script's assumption. But it meant the actual resubmission of the fixed build needed two
manual clicks in the App Store Connect UI — "Update Review," then "Resubmit to App Review" — before
the automation's own upload step could hand it back to Apple. The upload itself succeeded cleanly;
the CI run for that release still shows red, because the tool did exactly what it was built to do
and stopped rather than guess.

**What I'd do differently:** I'd extend the tool to recognise the specific, narrow case of
"unresolved issues plus a new build already attached" and treat that as a safe, well-defined path
to resubmit automatically, rather than treating every unresolved-issues state as a blanket stop.
The current behaviour isn't wrong — refusing to guess is the right default — but there's a
meaningful difference between "I don't know what happened here" and "a human already fixed the
thing Apple flagged and reattached a new build," and only the first of those actually needs a
person in the loop.

## Sources

- [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi)
