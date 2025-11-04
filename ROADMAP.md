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
a summary of the Galactipy [GitLab Milestones][3]
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
and discussions on the project's repository
over GitLab.
Please check the sections
on [Merge Requests][4] and [Roadmap Maintenance][5]
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
Dates provided here
are gross estimations
and might be outdated,
please refer to each milestone
for more accurate information.

Priorities and requirements change based on
community feedback,
roadblocks encountered,
community contributions
etc.
If you depend
on a specific item,
check if it is mapped for development
through the most appropriate milestone.
If not,
open a [**Request for Improvement**][6]
through the Issue Tracker.
We will try our best
to bring updated status information.

| Milestone | Description                                                                                                                                       |                Theme                 |                        Timeline                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------: | :----------------------------------------------------: |
| %1        | Devise and implement automated testing for non-Python file generation, integration tests to validate generated projects serviceability.           | :bullettrain_side: Team Productivity |                          N/A                           |
| %2        | Provide files and boilerplate configuration for managing generated projects documentation.                                                        |       :sparkles: New Features        |                          N/A                           |
| %3        | Update linting tools for project and template to current standards, replacing Black with Ruff.                                                    |  :triangular_ruler: Standardisation  | **Delivered with [`v0.3`][v0.3] :airplane_departure:** |
| %4        | Update Docker features to current standards, provide functional Dockerfile for generated projects.                                                |       :motorway: Improvements        |                          N/A                           |
| %5        | Configure additional GitLab tools for generated projects, close gap between GitLab and GitHub features.                                           |  :triangular_ruler: Standardisation  |                          N/A                           |
| %6        | Update GitHub configuration originally implemented in `python-package-template` with current day standards, include new GitHub Actions and tools. |       :motorway: Improvements        |                          N/A                           |
| %7        | Organise features, documentation and options for releasing `v1.0`.                                                                                |         :gem: Stable Release         |                          N/A                           |
| %8        | Replace `Makefile` with Invoke as the subprocess manager.                                                                                         |       :motorway: Improvements        | **Delivered with [`v0.4`][v0.4] :airplane_departure:** |
| %10       | Write clear-cut user tutorial for project management best practices via documentation.                                                            | :children_crossing: User Experience  |                          N/A                           |
| %11       | Adapt and document relevant GitLab processes and modus operandi to establish standard development philosophy for project and template.            |          :scroll: Policies           |             **Delivered Internally :100:**             |
| %12       | Include additional tools and services for building applications, checking code coverage and obtaining development metrics for releasing `v2.0`.   |       :sparkles: New Features        |                          N/A                           |
| %13       | Structure additional tasks and steps for configuring external services, eliminate the need for additional setup outside the CLI.                  | :children_crossing: User Experience  |                          N/A                           |
| %14       | Integrate Invoke tasks to call the SCM APIs for common project management tasks and housekeeping.                                                 | :bullettrain_side: Team Productivity |                          N/A                           |
| %15       | Expand the developer toolset for automating minor tasks related to style, formatting and policies.                                                | :bullettrain_side: Team Productivity |                          N/A                           |
| %16       | Move Galactipy documentation to dedicated static site.                                                                                            |          :scroll: Policies           |                          N/A                           |

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
read the [guidelines][7] for developers
to situate yourself first
and get to know
how we work as a team.
If you still have any questions,
open a Request for Support
via the [Issue Tracker][8]
so the team can help
with clarifications.

[1]: https://www.cookiecutter.io/
[2]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md
[3]: https://gitlab.com/galactipy/galactipy/-/milestones
[4]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#start-with-a-merge-request
[5]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#roadmap-management
[6]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Improvement
[7]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[8]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Support

[v0.3]: https://gitlab.com/galactipy/galactipy/-/releases/v0.3.0
[v0.4]: https://gitlab.com/galactipy/galactipy/-/releases/v0.4.0
