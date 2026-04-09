# Our Philosophy

This document defines
the deeper principles we follow
to shape our approach
to {{ cookiecutter.project_name }} development.
This section outlines our _modus operandi_
and provides insight
into the mindset needed
for successful contributions.

Our project's guidelines
are strongly influenced by the [GitLab Handbook][1],
which serves as GitLab's official company manual.
Their best practices
are transferable
to any team,
and we have adopted several
of these principles
to formalise expectations
for contributors
within our development ecosystem.

## Start with a {{ cookiecutter.__mr_term }}

> Adapted from the [Communication][2] section of the GitLab Handbook.

When possible,
it's best practice
to start a discussion
with a {{ cookiecutter.__mr_term }} ({{ cookiecutter.__mr_acronym }})
instead of an issue.
An {{ cookiecutter.__mr_acronym }} is associated
with a specific change
that is proposed
and transparent for everyone
to review
and openly discuss.

The nature of {{ cookiecutter.__mr_acronym }}s
facilitate discussions
around a proposed solution
to a problem that is actionable.
An {{ cookiecutter.__mr_acronym }} is actionable,
while an issue
will take longer
to take action on.

1. **Always** open an {{ cookiecutter.__mr_acronym }}
   for things you are suggesting
   and/or proposing.
   Whether something is not working right
   or we are iterating
   on a new internal process,
   it is worth opening a {{ cookiecutter.__mr_term }}
   with the minimal valuable change
   instead of opening an issue
   encouraging open feedback on the problem
   without proposing any specific change directly.
   Remember,
   an {{ cookiecutter.__mr_acronym }} also invites discussion,
   but it's specific
   to the proposed change
   which facilitates focused decision;
2. Never ask someone
   to create an issue
   when they can default
   to the {{ cookiecutter.__mr_term }};
3. Not every solution
   will solve the problem at hand.
   Keep discussions focused
   by **defining the problem first**
   and **explaining your rationale**
   behind the Minimal Valuable Change (MVC)
   proposed in the {{ cookiecutter.__mr_acronym }};
4. Have a [**bias for action**][3]
   and do not aim for consensus.
   Every {{ cookiecutter.__mr_acronym }} is as-is proposal,
   if an {{ cookiecutter.__mr_acronym }}'s author isn't responsive
   take ownership of it
   and complete it.
   Some improvement is better than none;
5. If submitting a change for a feature,
   **update the description with the final conclusions**
   – why an {{ cookiecutter.__mr_acronym }} was rejected
   or why it was approved.
   This makes it much easier
   to see the current state of an issue
   for everyone involved
   in the implementation
   and prevents confusion
   and discussion
   later on;
6. Submit the **smallest** viable and valuable thing.
   When proposing a change,
   submit the smallest reasonable commit,
   put suggestions
   for other enhancements
   in separate issues/{{ cookiecutter.__mr_acronym }}s
   and link them.
   An {{ cookiecutter.__mr_acronym }} can start off
   as only a problem description
   and `TODO` comments;
7. Do not leave {{ cookiecutter.__mr_acronym }}s open
   for a long time.
   {{ cookiecutter.__mr_acronym }}s should be **actionable**
   – maintainers should have
   a clear understanding
   of what changed
   and what they are
   ultimately approving or rejecting;
8. When submitting a MVC,
   **ask for feedback**
   from your peers.
   If they suggest changes,
   you get the opportunity
   to improve your work
   and propose an alternative solution.
   This promotes collaboration
   and advances everyone's skills;
9. Respond to comments within a **threaded discussion**.
   If there isn't a discussion thread yet,
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
   you can use the Reply to Comment button
{%- else %}
   you can use the Quote Reply button
{%- endif %}
   from the comments to create one.
   This will prevent comments
   from containing many interweaved discussions
   with responses that are hard to follow;
10. If your comment or answer
    contains separate topics,
    write separate comments for each,
    so others can address topics independently
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
    using the Reply to Comment button;
{%- else %}
    using the Quote Reply button;
{%- endif %}
11. If you have received any feedback
    or questions on your {{ cookiecutter.__mr_acronym }},
    try to acknowledge comments
    as that's how we ensure
    we create an environment of belonging
    for all team members.
    Merging your {{ cookiecutter.__mr_acronym }} as-is
    without giving an answer
    or any response
    makes the commenters feel
    their opinions are unheard.
    On the other hand,
    having a {{ cookiecutter.__mr_acronym }} with too many comments
    may risk the author falling
    into a perpetual loop of
    changing the {{ cookiecutter.__mr_acronym }} description
    or explaining too much,
    causing people to defer
    rather than working
    with a bias for action.
    This is something we want to avoid.
    When fast decisions are needed,
    we'll have to accept
    that people listened to us
    but don't owe us an explanation
    to have fast decisions
    based on everyone's input.
    The goals are to be transparent
    and collaborative
    – not to lose efficiency.
    Not everyone will agree,
    but we expect all people to
    disagree, commit, and disagree;
12. Even when something is not done,
    share it internally
    so people can comment early
    and prevent rework;
13. Create a **Draft** {{ cookiecutter.__mr_term }}
    to prevent an accidental early merge.
    Only use Draft when merging it
    would **make things worse**,
    which should rarely be the case
    when contributing to the project.
    Most {{ cookiecutter.__mr_term }}s that are in progress
    don't make things worse.
    In this case, do not use Draft;
    if someone merges it
    earlier than you expected
    just create a new {{ cookiecutter.__mr_term }}
    for additional items.
    Never ask someone
    to do a final review
    or merge something
    that still has Draft status.
    At that point
    you should be convinced
    it is good enough to go out;
14. If any follow-up actions are required
    on the issue
    after the {{ cookiecutter.__mr_term }} is merged,
    avoid auto-closing the related issue.

## _Say Why, Not Just What_

> Adapted from the [GitLab Values][4].

Transparent changes
have the reasons for the change
laid out clearly
along with the change itself.
This leads to fewer questions later on
because people already have some understanding.
A change with no public explanation
can lead to a lot of
extra rounds of questioning,
which is less efficient.

This also helps
with institutional memory:
a year from now
when you want to know
why a decision was made,
or not,
the issue or {{ cookiecutter.__mr_acronym }} that has the decision
also shares why the decision was made.
This is related to [Chesterton's fence][5]
– it's much easier
to suggest removing
or changing something
if you know
why it exists
in the first place.

If you use generalised terms
such as "industry standard"
or "best practices",
be sure to give context,
as without context
they can be seen
as potentially vague
or opaque.

Saying why and not just what
enables discussion around topics
that may impact
more than one front.
When decisions align
with more than a single project goal,
they are easy to discuss
and decide.
When there are multiple goals
involved for a change,
directly discussing the trade-offs
is easier
with more context.

Articulating why
also helps people understand
how something changed
when you articulate
that you changed your mind.

Saying why does not mean
justifying a decision against all other suggestions.
The maintainers are responsible
for their decision.
The maintainers are not responsible
for convincing other people,
but they should be able
to articulate their reasoning
for the change.

When a contributor comes across
{{ cookiecutter.__roadmap_item_indefinite }},
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
{{ cookiecutter.__mr_term }}
{%- else %}
{{ cookiecutter.__mr_term }},
discussion
{%- endif %}
or issue
that does not provide a "why"
with sufficient context,
the team member is responsible
for getting the why
and, if needed,
working with the maintainers
to ensure that
it is adequately documented
and communicated
to give context
to other team members.
In the absence of a why,
team members may
speculate the why.
This is something
that can lead to disruption
and inefficiency.

## Operate with a Bias for Action

> Adapted from the [GitLab Values][6].

It's important that
we keep our focus on action,
and don't fall into the trap
of analysis paralysis
or sticking to
a slow, quiet path
without risk.
Decisions should
be thoughtful,
but delivering fast results
requires the fearless acceptance
of occasionally making mistakes;
our bias for action
also allows us
to course correct quickly.
Try to get results
as fast as possible,
but without compromising
consistency,
quality
or jostling
our general practices
when working together.

## Interactions Enable Insights

At {{ cookiecutter.project_name }},
we approach every single interaction
– with other contributors,
users,
the codebase,
the configuration files
and documentation –
as a stimulant
to keep our minds acute,
allowing us
to tie elements previously unnoticed
that echo through the project.

Interact with elements of the project
with an observant spirit,
there is always an unseen factor.
Capture insights
and reflect upon their meaning
and implications
for the project
and your work.
Software development is human
at its core,
and [**human systems are inherently complex**][7].
We should not let
all the code,
interfaces
and systems
we handle on our work
obscure the fact
that we pursue
building a template
so it can be useful
and cherished by others.

## Sharing Insights Drives Progress

By extracting the root
of those four values,
we have conceived
a fifth value of our own
to steer our development philosophy.
This principle is fundamental
to how we approach
collaboration,
documentation,
and community engagement.
It emphasises the importance of
actively sharing knowledge,
experiences,
and ideas
to foster a culture
keen to exercising **continuous improvement**.
By embracing this value,
we aim to create
an environment
where both contributors
and users
feel empowered
to learn,
cooperate
and grow together.

In practical terms,
this means that
we prioritise clear and concise documentation of knowledge,
ensuring that
relevant information
is easily accessible
to all interested parties.
This includes
maintaining up-to-date
guides,
tutorials
and reference materials
that reflect the current state of the project;
articulating thought processes,
design decisions
and problem-solving strategies
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
in issue and {{ cookiecutter.__mr_term }} discussions;
{%- else %}
in issues, discussions and {{ cookiecutter.__mr_term }}s;
{%- endif %}
providing the adequate guidance
for new contributors
to succeed in their first development;
storing ideas
generated from discussions
into work items
for future prioritisation.

By doing so,
we facilitate
a deeper understanding
of the project's internals
and evolution,
making it easier for new contributors
to get started
and for users
to understand
how to make the most
out of our project.
This also reinforces that
recognising even small efforts,
such as adding a link
to a useful resource
or explaining a complex concept
in simpler terms,
can significantly impact
the value of the project
to someone else.

{% if cookiecutter.licence != 'nos' -%}
## There Are no Good First Issues

The concept of
labelling issues in open source projects
to mark potential good contributions
for a first timer
has its origins in the [First Timers Only][8] initiative
by Kent C. Dodds.

At {{ cookiecutter.project_name }},
we tackle the notion of Good First Issues
in a different way.
We believe that
enabling development from new contributors
is an integral part
of keeping an open source project active,
but it takes more
than a label in an issue tracker
to succeed.
The notion that
people can just browse repositories
and search for a contribution
is invalid,
most of what is labelled
needs more context
for any one new contributor
to approach it.
This is represented by our philosophy:

<div align="center">

<i>The best good first issues are the ones you open yourself.</i>

</div>

- For **upstream developers**,
  this means understanding that
  not all developments mapped by you
  should be _delivered_ by you.
  If the change in question
  can be considered relevant
  for introducing a new contributor
  to the project,
  time should be dedicated
  in ensuring the change
  _can_ be delivered by them,
  through work item refinement
  and clear steps
  to conclude the demand,
  instead of being delivered
  without ever
  granting an opportunity for someone
  – and the community –
  to grow.
  This also means
  being available
  to [orient][9] contributors
  should they feel lost
  and reassure [clear communication][10]
  with them;
- For **{{ cookiecutter.project_name }} users**
  who have opened a request
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  on the Issue Tracker,
{%- else %}
  on the Issue Tracker
  or GitHub Discussions,
{%- endif %}
  this means that
  the best solution to your request
  is to deliver it yourself!
  By approaching your requests
  as a gateway to contributing to the project,
  you generate growth opportunities
  to yourself and the team.
  If upon opening your request
  you feel inclined
  to come forward and help resolve it yourself,
  mark it with the appropriate label
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  by adding `/label ~"up-for-a-change"`
  to the request description
{%- else %}
  by adding the `up-for-a-change` label
  to the request being opened
{%- endif %}
  so that a developer can mentor you
  on the solution.

{% endif -%}
<!-- Anchors -->

[1]: https://handbook.gitlab.com/
[2]: https://handbook.gitlab.com/handbook/communication/#start-with-a-merge-request
[3]: #operate-with-a-bias-for-action
[4]: https://handbook.gitlab.com/handbook/values/#say-why-not-just-what
[5]: https://theknowledge.io/chestertons-fence-explained/
[6]: https://handbook.gitlab.com/handbook/values/#operate-with-a-bias-for-action
{%- if cookiecutter.licence != 'nos' %}
[7]: https://conversational-leadership.net/we-human-beings-are-complex/
[8]: https://kentcdodds.com/blog/first-timers-only
[9]: #fostering-an-inviting-community
[10]: #how-to-behave-among-other-contributors
{%- endif %}
