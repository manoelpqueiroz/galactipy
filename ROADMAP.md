# :map: Galactipy Roadmap

## About Galactipy

Galactipy is a [Cookiecutter][1] template
for generating boilerplate files
and creating Python software,
especially CLI applications.
By running Cookiecutter,
users can have an initial set of files
to jumpstart their project development,
reducing the need
for tool and service setup
to a bare minimum.

### Project Mission

Provide a comprehensive set of files
for developers to use
with their newly created projects,
encompassing configuration files,
developer productivity tools
and ready-to-use scripts
for Continuous Integration and Continuous Deployment,
reducing overhead
and accelerating actual development
of new software.

### How to Get Involved

This file is mainly used
for informational purposes.
If you wish to know
how to get involved with Galactipy,
check out the [`CONTRIBUTING`][2] file,
where you can get acquainted
with the many ways
of helping the project.

## About this Document

This document provides
a summary of the Galactipy [GitLab Epics][3]
that serve as the up-to-date description of items
that are in the project's release pipeline.
Most items are gathered
from the community
or include a feedback loop
with the community.
This should serve
as a reference point
for Galactipy users and contributors
to understand where the project is heading,
and help determine
if a contribution could be conflicting
with a longer term plan.

### How to Help

Discussion on the roadmap takes place
via Merge Requests
and discussions on the [Templates][4] repository
over GitLab.
Please check the sections
on [Merge Requests][5] and [Roadmap Maintenance][6]
of the `CONTRIBUTING` file
for further clarification
on how to proceed
if you believe a discussion
surrounding the project's direction
should take place,
whether you want
to provide suggestions
or just feedback to an item
in the roadmap.

Please review the roadmap
to avoid potential duplicated effort.

## Roadmap History

The following table includes
the current roadmap for Galactipy
for summarisation
and discussion purposes only.
Please refer to each epic
for additional information.
Also look at the list of epics
[encompassing multiple projects][7],
as those might contain developments
related to Galactipy.

Priorities and requirements change based on
community feedback,
roadblocks encountered,
community contributions
etc.
If you depend
on a specific item,
check if it is mapped for development
through the most appropriate epic.
If not,
open a [**Request for Improvement**][8]
through the Issue Tracker.
We will try our best
to bring updated status information.

```glql
display: table
fields: title, state, start, due, updated, labels, confidential
query: group = "galactipy" AND type = epic AND label in (~"project::galactipy", ~"project::cookiecutter")
sort: created
```

You can also help us
deliver that feature
by contributing directly to Galactipy,
we are always
looking for contributors
that will help us reduce
technical,
automation,
and documentation debt.
If you don't know where to start,
read the [guidelines][9] for developers
to situate yourself first
and get to know
how we work as a team.
If you still have any questions,
open a Request for Support
via the [Issue Tracker][10]
so the team can help
with clarifications.

[1]: https://www.cookiecutter.io/
[2]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md
[3]: https://gitlab.com/groups/galactipy/-/epics
[4]: https://gitlab.com/galactipy/templates/-/merge_requests/?state=all&label_name%5B%5D=internals%3A%3Apolicies
[5]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#start-with-a-merge-request
[6]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#roadmap-management
[7]: https://gitlab.com/groups/galactipy/-/epics?state=opened&label_name%5B%5D=project%3A%3Amultiple
[8]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Improvement
[9]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[10]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Support
