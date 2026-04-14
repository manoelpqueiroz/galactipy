{% raw -%}
---
tags:
  - For Your Information
  - Workflows
---

{% endraw -%}
# Contributing by Helping Other People

[![RFSs][1]][2]

Inspired by [Typer's][3] welcoming community
and their positive outlook
on the effect of [collective intelligence][4],
we are committed to enabling an environment
in which such exponential interactions
can take place.
As such,
one of the best ways people can
contribute to {{ cookiecutter.project_name }}
is by helping others,
either users like you
who have reached the members of the project
with questions and requests
or the development team itself.

The most direct way
you can provide your help to others
is to look for open [Requests for Support][2]
and try to answer other users' questions.
In many cases
you might already know the answer to them!

Just remember,
the most important point is:
**try to be kind**.
People come with their frustrations
and in many cases don't ask
in the best way,
but try as best as you can
to be kind.
As mentioned earlier,
we want this community
to the welcoming.

At the same time,
don't accept bullying
or disrespectful behaviour
towards others.
We have to take care of each other.
See the [Code of Conduct][5]
for more details
on how we deal with these cases.

## Orientation for Effectively Helping Others

Here is a general guide
on how to help other users
with their requests:

1. Understand the request:
   - Check if you can understand
     what is the **purpose**
     and use case
     of the person asking;
   - Then check if the request is **clear**;
   - In many cases the question asked
     is about an imaginary solution
     from the user,
     but there might be a **better** one.
     If you can understand
     the problem and use case
     better,
     you might be able
     to suggest a better **alternative solution**;
   - If you can't understand the question,
     ask for more details;
2. Reproduce the problem:
   for most of the cases
   relating to issues and questions
   in general,
   most likely
   there's something
   related to the person's original code.
   In many cases
   they will only copy a fragment of the code,
   but that's not enough
   to reproduce the problem;
   - You can ask them
     to provide a [minimal, reproducible example][6],
     that you can copy-paste
     and run locally
     to see the same error or behavior
     they are seeing,
     or to understand
     their use case better;
   - If you are feeling too generous,
     you can try
     to create an example like that
     yourself,
     just based
     on the description of the problem.
     Just have in mind that
     this might take a lot of time
     and it might be better
     to ask them
     to clarify the problem first;
3. Suggest solutions:
   - After being able to
     understand the question,
     you can give them
     a possible answer;
   - In many cases,
     it's better to understand
     their **underlying problem**
     or use case,
     because there might be a better way
     to solve it
     than what they are trying to do.

!!! tip "Tip: When Things are Difficult"

    When things are great,
    everything is easier,
    so that doesn't need much instructions.
    When things are difficult,
    here are some guidelines.

    Try to find the good side.
    In general,
    if people are not being unfriendly,
    try to thank their effort and interest,
    even if you disagree
    with the main subject,
    just thank them
    for being interested in the project,
    or for having dedicated some time
    to try to do something.

    It's difficult to
    convey emotion in text,
    use emoji to help.
    :wink:

    In many requests
    people bring their frustration
    and show it without filter,
    which can be displayed through
    exaggerating,
    complaining,
    being entitled
    etc.
    That's really not nice,
    and when it happens,
    it lowers our priority
    to solve their problems.
    Still,
    try to breathe,
    and be gentle with your answers.

    Try to avoid
    using bitter sarcasm
    or potentially passive-aggressive comments.
    If something is wrong,
    it's better to be direct
    (try to be gentle)
    than sarcastic.

    Try to be
    as specific and objective
    as possible,
    avoid generalisations.

## Commitment to Help

What consumes
most of the time of the development team
is actually answering questions
and solving problems.
We end up not being able
to add new features,
fix bugs
and review {{ cookiecutter.__mr_term }}s
as fast as we wanted
because too much of the time
is spent handling user requests.

Also, this is
on top of all the help
provided by several community members
that dedicate a lot of their time
to come here
and aid others.

If more {{ cookiecutter.project_name }} users
came to help others like them
just a little bit more,
it would be much less effort for them.

That's why our templates for requests
include a section
calling authors to action
with improving the {{ cookiecutter.project_name }} ecosystem
the best way they can.
For all purposes,
we believe that
contributions should be done by the person's own accord,
demonstrating a [bias for action][7]
and fitting for
their perceived capacity
for helping.

Therefore,
we have implemented a **Commitment to Help** modus operandi,
kindly asking issue authors
to engage further
and help lessen demand overall.
If for every new request that comes
there is extra action from its author
to help with another project demand,
we strengthen our community
and improve,
bit by bit,
every aspect of {{ cookiecutter.project_name }}:
communication,
agility,
organization,
aggregated value
and more!

If you have opened
or are about to open
a Request for Support
or a Request for Improvement,
we would be extremely grateful
if you could pick one of the options
from the list provided in the template
to commit with additional help
for the project.

We thank you in advance
for your kindness and dedication!

<!-- Anchors -->

[1]: https://img.shields.io/badge/requests_for_support-ed9121?style=for-the-badge
{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=request%3A%3Asupport&type%5B%5D=issue
{% elif cookiecutter.scm_platform == 'GitLab Free' -%}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=rfs&type%5B%5D=issue
{% else -%}
[2]: {{ cookiecutter.__scm_link_url }}/discussions/categories/requests-for-support
{% endif -%}
[3]: https://typer.tiangolo.com/help-typer/#help-others-with-questions-in-github
[4]: https://www.blockchain-council.org/ai/collective-intelligence-framework/
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CODE_OF_CONDUCT.md
[6]: https://stackoverflow.com/help/minimal-reproducible-example
[7]: ../philosophy.md#operate-with-a-bias-for-action
