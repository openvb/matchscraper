# Matchscraper
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/openvb/matchscraper?include_prereleases)
![GitHub](https://img.shields.io/github/license/openvb/matchscraper)

Matchscraper, a web scraper, provides a CSV format files of volleyball match statistics from the Web Competition by Data Project website.

# Requirements

- Python 3.8+
- Scrapy 2.7.1

# Installation

$ `git clone git@github.com:openvb/matchscraper.git`

$ `cd matchscraper`

$ `pip install -r requirements.txt`

# Usage

$ `python stats.py <Federation Acronym> <Match ID>`

## Examples

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=1623
    - Federation Acronym: CBV
    - Match ID: 1623
    - Command: $ `python stats.py cbv 1623`
    - Outputs:
        ```
        data/1623_22-10-28_home_fluminense.csv
        data/1623_22-10-28_guest_barueri-volleyball-club.csv
        ```

- Lithuanian Volleyball Federation
    - Data Project website: https://lvf-web.dataproject.com/MatchStatistics.aspx?mID=2093
    - Federation Acronym: LVF
    - Match ID: 2093
    - Command: $ `python stats.py lvf 2093`
    - Outputs:
        ```
        data/2093_2022-11-23_guest_jonavos-sc.csv
        data/2093_2022-11-23_home_svaja-viktorija-lsu.csv
        ```

# Page Locales

- pt-BR
- en-GB

# Scraped data (WIP)

- [x] Match ID
- [x] Match date
- [x] Home Team
- [x] Guest Team
- [ ] Coach
- [ ] Location
- [ ] Final result
- [ ] Result per SET

- Vote
    - [ ] Vote by player
- Points
    - [x] Total Points by player
    - [ ] Total Points by player per SET
    - [x] Break Points by player
    - [x] Win-Lost by player
    - [x] Totals
- Serve
    - [ ] Total Serves by player
    - [ ] Serve Erros by player
    - [ ] Serve Points by player
    - [ ] Totals
- Reception
    - [ ] Total Receptions by player
    - [ ] Reception Erros by player
    - [ ] Positive Pass Percentage by player
    - [ ] Excellent/ Perfect Pass Percentage by player
    - [ ] Totals
- Attack
    - [ ] Total Attacks by player
    - [ ] Attack Erros by player
    - [ ] Blocked Attack by player
    - [ ] Attack Points by player
    - [ ] Attack Points Percentage by player
    - [ ] Totals
- Block
    - [ ] Block Points by player
    - [ ] Totals