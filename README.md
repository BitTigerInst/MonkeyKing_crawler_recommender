# MonkeyKing_crawler_recommender
@team: MonkeyKing01 (team leader: Steven Yan)

Description
-----------

Inspired by BitTiger's tutorials on crawler and recommender, our goal is to build them to crawl the data from xiaomi appstore.

Plan
----

Here're some tentative schedules.

* __[2016/03/01 - 2016/03/05]__ Project Selection, Plan Discussion, and Proposal Draft Writing
* __[2016/03/06 - 2016/03/24]__ System Design, Resource Discovery, Project Implementation, Document Writing 
  * crawler
    * crawler locally run __(previous project)__
      * Follow and learn the code of Bittiger tutorial
      * Re-write for another appstore, run it locally
      * Save results into MongoDB
    * crawler running on server
      * Modify the code for server (multiple workers)
      * Deploy the code on server
  * recommender __(next project)__
    * recommender locally run __(next project)__
      * Follow and learn the code of Bittiger tutorial
      * Re-write the code for another appstore, run it locally
    * recommender running on server __(next project)__
* __[2016/03/25 - 2016/03/30]__ User Manual Writing and Video Presentation Making

_Details of each schedule and task will be added later._

Resource
--------

1. __[BitTiger Project: AppStore - Crawler]__ https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e
1. __[BitTiger Project: AppStore - Recommender]__ https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e

Language, Framework & Methodology
--------------------

+ Python 2.7.10, and 'pip install' following:
  + scrapy
  + pylint (use it to check code quality, and preferrably pass the check)
  + pymongo
+ Teamworking
  + Issues on github repo are used to create to-do lists and assign owners
    + Each team member can create issues 
    + Comments in issues are used to discuss and elaborate
    + Each team member can assign to themselves issues to resolve
  + Members can also discuss on a slack group
+ build necessary tests
  + write tests to ensure the main function of one's own code works
  + one can push the code even it does not pass the tests; just write something in the commit info to explain, so that others can help

Development Guildlines
----------------------

- __Modularity.__ Following the principle _"loose coupling and high cohesion"_, each module should be standalone.

- __Minimalism.__ Each module should be kept short, simple, and concise. Every piece of code should be transparent upon first reading. 
- __Easy extensibility.__ New modules (as new classes and functions) are should be simply add, and existing modules should be extended easily.



