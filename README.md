# MonkeyKing_crawler_recommender

Description
-----------

Inspired by BitTiger's tutorials on crawler and recommender, our goal is to build one to crawl the data from xiaomi appstore.

Plan
----

Based on our experiences on web development and descriptions metioned above, we take __Febrary, 2016__ as the __1st stage__ with the __primary__ goal of __prototyping__ our own crawler and recommender following the __Development Guildlines__ metioned below. Here're some tentative schedules.

* __[2016/02/05 - 2016/02/07]__ Project Selection, Plan Discussion, and Proposal Draft Writing
* __[2016/02/08 - 2016/02/24]__ System Design, Resource Discovery, Project Implementation, Document Writing 
  * locall run
    * crawler
      * Follow and learn the code of Bittiger tutorial
      * Re-write the simple code for another appstore, run it locally
      * Save results into MongoDB
    * recommender __(next project)__
      * Follow and learn the code of Bittiger tutorial
      * Re-write the code for another appstore, run it locally
  * run on server __(next project)__
    * crawler
      * Modify the code for server (multiple workers)
      * Deploy the code on server
    * recommender
      * Modify the code for server (multiple workers)
      * Deploy the code on server
* __[2016/02/25 - 2016/02/29]__ User Manual Writing and Video Presentation Making

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

Owner
-----

@team: MonkeyKing
