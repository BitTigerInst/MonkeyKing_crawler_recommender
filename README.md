# MonkeyKing_crawler_recommender

Description
-----------

Inspired by BitTiger's tutorials on crawler and recommender, our goal is to build one to crawl the data from xiaomi appstore.

Plan
----

Based on our experiences on web development and descriptions metioned above, we take __Febrary, 2016__ as the __1st stage__ with the __primary__ goal of __prototyping__ our own crawler and recommender following the [Development Guildlines](https://github.com/BitTigerNY/AraChat/edit/master/README.md#Development Guildlines) metioned below. Here're some tentative schedules.

* __[2016/02/05 - 2016/02/07]__ Project Selection, Plan Discussion, and Proposal Draft Writing
* __[2016/02/08 - 2016/02/24]__ System Design, Resource Discovery, Project Implementation, Document Writing 
  * crawler
    * Follow the code of Bittiger tutorial
    * Modify the code for another appstore, run it locally
    * Modify the code for server (multiple workers)
    * Deploy the code on server
  * recommender
    * Follow the code of Bittiger tutorial
    * Modify the code for another appstore, run it locally
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
  + pylint
  + coverage
+ Test Driven Development (TDD)
  + http://chimera.labs.oreilly.com/books/1234000000754/index.html
  + write test first, and then write code to make the test success
  + for each push, need to ensure the new code does not break any of the tests (add and commit are still ok if the tests fail; just do not push to the github)
  + need to write tests to ensure 100% coverage (waiver is allowed case-by-case) for every new code

Development Guildlines
----------------------

- __Modularity.__ Following the principle _"loose coupling and high cohesion"_, each module should be standalone.

- __Minimalism.__ Each module should be kept short, simple, and concise. Every piece of code should be transparent upon first reading. 
- __Easy extensibility.__ New modules (as new classes and functions) are should be simply add, and existing modules should be extended easily.

Owner
-----

@team: MonkeyKing
