{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
---

{% endraw -%}
# Roles and Attributions
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#roles-and-attributions

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

## The Responsibility of the {{ cookiecutter.__mr_term }} Author
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#the-responsibility-of-the-{{ cookiecutter.__mr_term_slug }}-author

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

The responsibility to
find the best solution
and implement it
lies with the {{ cookiecutter.__mr_term }} author.
The author stays assigned
to the {{ cookiecutter.__mr_term }}
as the assignee
throughout the code review lifecycle.
If you are unable
to set yourself as an assignee,
ask a reviewer
to do this for you.

Before requesting
a review from a maintainer
to approve and merge,
they should be confident that:

- It actually solves the problem
  it was meant to solve;
- It does so
  in the most appropriate way;
- It satisfies all requirements;
- There are no remaining
  bugs,
  logical problems,
  uncovered edge cases,
  or known vulnerabilities.

The best way to do this,
and to avoid
unnecessary back-and-forth
with reviewers,
is to perform a self-review
of your own {{ cookiecutter.__mr_term }},
following the [Code Review][1] guidelines.
During this self-review,
try to include
comments in the {{ cookiecutter.__mr_acronym }} on lines
where decisions or trade-offs were made,
or where a contextual explanation
might aid the reviewer
in more easily
understanding the code.

To reach
the required level of confidence
in their solution,
an author is expected
to involve other people
in the investigation
and implementation processes
as appropriate,
with the goal of:

- Discussing different solutions
  or getting an implementation reviewed;
- Getting an in-depth review
  of the solution;
- Clearing up confusion
  or verify that
  the end result matches
  what the team
  had in mind.

If you know
you'll need many {{ cookiecutter.__mr_term }}s
to deliver a feature
– for example,
you created a proof of concept
and it is clear the feature
will consist of 10+ {{ cookiecutter.__mr_term }}s –,
consider identifying reviewers and maintainers
who possess the necessary understanding
of the feature
(you share the context with them).
Then direct all {{ cookiecutter.__mr_term }}s
to these reviewers.
Having stable reviewer counterparts
for multiple {{ cookiecutter.__mr_term }}s with the same context
improves efficiency.

Before the review,
the author is requested
to submit comments
on the {{ cookiecutter.__mr_term }} diff
alerting the reviewer
to anything important
as well as for anything
that demands further explanation
or attention.
Examples of content
that may warrant a comment
could be:

- The addition of a linting rule;
- The addition of a dependency;
- Where not obvious,
  a link to
  the parent class
  or method;
- Any benchmarking performed
  to complement the change;
- Potentially insecure code.

If there are any
projects,
snippets,
or other assets
that are required for a reviewer
to validate the solution,
ensure they have access
to those assets
before requesting review.

When assigning reviewers,
it can be helpful
to add a comment indicating
which _type_ of review
you are looking for that reviewer.
Explicitness around {{ cookiecutter.__mr_acronym }} review types
is efficient for the {{ cookiecutter.__mr_acronym }} author
because they receive the type of review
that they are looking for
and it is efficient for the {{ cookiecutter.__mr_acronym }} reviewers
because they immediately know
which type of review to provide.

Avoid:

- Adding `TODO` comments
  directly to the source code
  unless the reviewer requires you
  to do so.
  If `TODO` comments are added
  due to an actionable task,
  include a link
  to the relevant issue;
- Adding comments
  which only explain
  what the code is doing.
  If non-`TODO` comments are added,
  they should explain [why, not what][2];
- Requesting maintainer reviews
  of {{ cookiecutter.__mr_term }}s with failed tests.
  If the tests are failing
  and you have to
  request a review,
  ensure you leave a comment
  with an explanation.

This saves reviewers time
and helps authors catch mistakes earlier.

### Recommendations to Get Your Changes Merged Faster
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#recommendations-to-get-your-changes-merged-faster

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

1. Make sure
   to follow best practices:
   - Write
     efficient instructions,
     add screenshots,
     steps to validate
     etc.;
   - Follow the acceptance checklist
     for the {{ cookiecutter.__mr_acronym }} template;
2. Follow the {{ cookiecutter.project_name }} patterns,
   even if you think there's a better way.
   Discussions often delay merging code.
   If a discussion is getting too long,
   consider following
   the documented approach
   or the maintainer's suggestion,
   then open a separate {{ cookiecutter.__mr_acronym }}
   to implement your approach
   as part of our best practices
   and have the discussions there;
3. Consider splitting big {{ cookiecutter.__mr_acronym }}s
   into smaller ones.
   Around 200 lines is a good threshold:
   - Smaller {{ cookiecutter.__mr_acronym }}s reduce cognitive load
     for authors and reviewers;
   - Reviewers tend
     to pick up smaller {{ cookiecutter.__mr_acronym }}s
     to review first
     (a large number of files
     can be scary);
   - Discussions on one particular part of the code
     will not block
     other parts of the code
     from being merged;
   - Smaller {{ cookiecutter.__mr_acronym }}s are often simpler,
     and you can consider
     skipping the first review
     and sending directly
     to the maintainer,
     or skipping one of the suggested domains
     (e.g.,
     CI,
     backend,
     frontend
     etc.);
   - :warning: Split {{ cookiecutter.__mr_acronym }}s with caution:
     {{ cookiecutter.__mr_acronym }}s that are too small
     increase the number of total reviews,
     which can cause the opposite effect;
4. Minimise the number of reviewers
   in a single {{ cookiecutter.__mr_acronym }}.

### Recommendations for Facilitating Reviews
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#recommendations-for-facilitating-reviews

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Keep in mind that
code review is a process
that can take multiple iterations,
and reviewers may spot things
later that they may not have seen
the first time.

- The first reviewer of your code is you.
  Before you perform that first push
  of your shiny new branch,
  read through the entire diff.
  Does it make sense?
  Did you include something
  unrelated to the overall purpose
  of the changes?
  Did you forget to
  remove any debugging code?
- Write a detailed description
  as outlined in the [{{ cookiecutter.__mr_term }} guidelines][3].
  Some reviewers may not be familiar
  with the product feature
  or area of the codebase.
  Thorough descriptions help all reviewers
  understand your request
  and test effectively;
- If you know your change depends
  on another being merged first,
  note it in the description
  and set a {{ cookiecutter.__mr_term }} dependency;
- Be grateful
  for the reviewer's suggestions
  ("Good call. I'll make that change.");
- Don't take it personally.
  The review is of the code,
  not of you;
- Explain [why][2] the code exists
  ("It's like that because of these reasons.
  Would it be more clear
  if I rename this class/file/method/variable?");
- Extract unrelated changes
  and refactoring tasks
  into future {{ cookiecutter.__mr_acronym }}s/issues;
- Seek to understand
  the reviewer's perspective;
- Try to respond to every comment;
- The {{ cookiecutter.__mr_term }} author
  resolves only the threads
  they have fully addressed.
  If there's
  an open reply,
  an open thread,
  a suggestion,
  a question,
  or anything else,
  the thread should
  be left to be resolved
  by the reviewer;
- It should not be assumed
  that all feedback requires their recommended changes
  to be incorporated into the {{ cookiecutter.__mr_acronym }}
  before it is merged.
  It is a judgment call
  by the {{ cookiecutter.__mr_acronym }} author
  and the reviewer
  as to if this is required,
  or if a follow-up issue
  should be created
  to address the feedback
  in the future
  after the {{ cookiecutter.__mr_acronym }} in question is merged;
- Request a new review
  from the reviewer
  once you are ready
  for another round of review.
  If you do not have
  the ability to request a review,
  `@` mention the reviewer instead.

## The Responsibility of the Reviewer
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#the-responsibility-of-the-reviewer

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

All {{ cookiecutter.project_name }} contributors
who choose to review
and provide feedback on {{ cookiecutter.__mr_term }}s
have a responsibility to
both the project
and the individual making the contribution.
Reviews and feedback must be
helpful,
insightful,
and geared towards
improving the contribution
as opposed to
simply blocking it.
Do not expect
to be able to block a {{ cookiecutter.__mr_term }}
from advancing simply
because you say "No" without [giving an explanation][2].
Be open to having your mind changed.
Be open to working with the contributor
to make the {{ cookiecutter.__mr_term }} better.

Reviews that are
dismissive
or disrespectful
of the contributor
or any other reviewers
are strictly counter
to the [Code of Conduct][4].

When reviewing a {{ cookiecutter.__mr_term }},
the primary goals are
for the codebase to improve
and for the person submitting the request to succeed.
Even if a {{ cookiecutter.__mr_term }} does not land,
the submitters should come away from the experience
feeling like their effort
was not wasted
or unappreciated.
Every {{ cookiecutter.__mr_term }} from a new contributor
is an opportunity to grow the community.

Review a bit at a time,
do not overwhelm new contributors.
It is tempting to micro-optimise
and make everything about
relative performance,
perfect grammar,
or exact style matches.
Do not succumb to that temptation.

Focus first
on the most significant aspects of the change:

- Does this change make sense for {{ cookiecutter.project_name }}?
- Does this change make {{ cookiecutter.project_name }} better,
  even if only incrementally?
- Are there clear bugs
  or larger scale issues
  that need attending to?
- Are the commit messages
  readable and correct?
- If it contains a breaking change,
  is it clear enough?

Understand why the change is necessary
(fixes a bug,
improves the user experience,
refactors the existing code).
Then:

- Try to be thorough in your reviews
  to reduce the number of iterations;
- Communicate
  which ideas you feel strongly about
  and those you don't;
- Identify ways
  to simplify the code
  while still solving the problem;
- Offer alternative implementations,
  but assume the author
  already considered them
  ("What do you think about using a custom validator here?");
- Seek to understand
  the author's perspective;
- Check out the branch,
  and test the changes locally.
  You can decide how much manual testing
  you want to perform.
  Your testing might result
  in opportunities
  to add automated tests;
- If you don't understand a piece of code,
  _say so_.
  There's a good chance someone else
  would be confused by it
  as well;
- Ensure the submitter is clear on
  what is required from them
  to address/resolve the suggestion;
- Ensure there are no open dependencies.
  Check linked issues for blockers.
  Clarify with the submitters if necessary.
  If blocked by one or more open {{ cookiecutter.__mr_acronym }}s,
  mention the blocking {{ cookiecutter.__mr_acronym }}
  in the discussion;
- After a round of line notes,
  it can be helpful
  to post a summary note
  such as "Looks good to me",
  or "Just a couple things to address";
- Let the submitter know
  if changes are required following your review.

When changes are necessary,
**request** them,
do not _demand_ them,
and do not assume
that the submitter already knows
how to add a test
or run a benchmark.

Specific
performance optimization techniques,
coding styles,
and conventions
change over time.
**The first impression you give to a new contributor never does.**

[Nits][5]
(requests for small changes
that are not essential)
are fine,
but try to avoid
stalling the {{ cookiecutter.__mr_term }}.
Most nits can typically be fixed by the reviewer
but they can also be
an opportunity for the contributor
to learn a bit more about the project.

It is always good to
clearly indicate nits
when you comment
(e.g.,
`Nit: change foo() to bar(). But this is not blocking.`).

**Be aware of the person behind the change:**
_how_ you communicate requests and reviews in your feedback
can have a significant impact
on the success of the {{ cookiecutter.__mr_term }}.
Yes,
we may land a particular change
that makes {{ cookiecutter.project_name }} better,
but the individual might just not want
to have anything to do with {{ cookiecutter.project_name }}
ever again.
The goal is not just
having good code,
you should guide the author
towards succeeding
with their contributions,
whether the {{ cookiecutter.__mr_acronym }} is approved or not
in the end.

Lastly,
**accept that there are different opinions about what belongs in {{ cookiecutter.project_name }}.**
It is not uncommon for contributors
to suggest new features they feel
would make {{ cookiecutter.project_name }} better.
These may or may not make sense to add,
but as with all changes,
be courteous in
how you communicate your stance on these.
Comments that make the contributor feel
like they should have "known better"
or ridiculed for even trying
run counter to the [Code of Conduct][4].

### The Right Balance
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#the-right-balance

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

One of the most difficult things
during code review
is finding the right balance
in how deep the reviewer
can interfere with the code
created by a submitter.

- Learning how to find the right balance takes time;
  that is why we have reviewers
  that become maintainers
  after some time spent
  on reviewing {{ cookiecutter.__mr_term }}s;
- Finding bugs is important,
  but thinking about good design
  is important as well.
  Building abstractions and good design
  is what makes it possible
  to hide complexity
  and makes future changes easier;
- Enforcing and improving [codestyle][6]
  should be primarily done
  through automation
  instead of review comments;
- Asking the submitter
  to change the design
  sometimes means
  the complete rewrite
  of the contributed code.
  It's usually a good idea
  to ask another maintainer or reviewer
  before doing it,
  but have the courage to do it
  when you believe it is important;
- In the interest of iteration,
  if your review suggestions are
  non-blocking changes,
  or personal preference
  – not a documented or agreed requirement –,
  consider approving the {{ cookiecutter.__mr_term }}
  before passing it back
  to the submitter.
  This allows them
  to implement your suggestions
  if they agree,
  or allows them to pass it
  onto the maintainer for review
  straight away.
  This can help
  reduce our overall time-to-merge;
- There is a difference
  in doing things right
  and doing things _right now_.
  Ideally,
  we should do the former,
  but in the real world
  we need the latter as well.
  A good example
  is a security fix
  which should be released
  as soon as possible.
  Asking the submitter
  to do a major refactoring
  in a {{ cookiecutter.__mr_term }} that is an urgent fix
  should be avoided;
- Doing things well today is usually better
  than doing something perfectly tomorrow.
  Shipping a kludge today is usually worse
  than doing something well tomorrow.
  When you are not able
  to find the right balance,
  ask other people
  about their opinion
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  and use the [`seeking-contributors::opinion`][7] label.
{%- else %}
  and use the [`seeking-input`][7] label.
{%- endif %}

## The Responsibility of the Maintainers
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#the-responsibility-of-the-maintainers

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Maintainers are responsible for
the overall health,
quality,
and consistency
of the {{ cookiecutter.project_name }} codebase.

Consequently,
their reviews focus primarily
on things like
overall architecture,
code organization,
separation of concerns,
tests,
DRYness,
consistency,
and readability.

Because a maintainer's job only depends
on their knowledge of the overall {{ cookiecutter.project_name }} codebase,
and not that of any specific domain,
they can review,
approve,
and merge {{ cookiecutter.__mr_acronym }}s
from any type of changes.

Maintainers are the responsible individuals
of assuring that the acceptance criteria of a {{ cookiecutter.__mr_term }}
are reasonably met.
In general,
quality is everyone's responsibility,
but maintainers are held responsible
for ensuring that an {{ cookiecutter.__mr_acronym }}
meets those general quality standards.
This includes
avoiding the creation of technical debt
in follow-up issues.

Maintainers do their best
to also review the specifics
of the chosen solution
before merging,
but as they are not necessarily domain experts,
they may be poorly placed to do so
without an unreasonable investment of time.
In those cases,
they defer to the judgment
of the submitter and earlier reviewers,
in favour of focusing
on their primary responsibilities.

If a developer who happens to also be a maintainer
was involved in a {{ cookiecutter.__mr_term }} as a reviewer,
it is recommended that
they are not also picked
as the maintainer to
ultimately approve and merge it.

Maintainers should check before merging
if the {{ cookiecutter.__mr_term }} is approved
by the required approvers.
If still awaiting further approvals from others,
`@` mention the submitter
and explain why in a comment.

<!-- Anchors -->

[1]: ./review.md
[2]: ../philosophy.md#say-why-not-just-what
[3]: ./prepare.md#opening-admissible-{{ cookiecutter.__mr_term_slug }}s
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/CODE_OF_CONDUCT.md
[5]: https://josipmisko.com/posts/code-review-nit
[6]: ../policies/styling.md#codestyle
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[7]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors%3A%3Aopinion&type%5B%5D=issue
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[7]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors&label_name%5B%5D=seeking-input&type%5B%5D=issue
{%- else %}
[7]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Aseeking-contributors%20label%3Aseeking-input
{%- endif %}
