import scrapy
import os
import re

from . import utils

class StatsHomeSpider(scrapy.Spider):
    name = 'home_stats'

    def __init__(self, fed_acronym='', match_id='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/MatchStatistics.aspx?mID={match_id}']
        self.match_id = match_id
        match_date = ''
        home_team = ''

        super().__init__(**kwargs)

    def parse(self, response):
        match_date_text = response.xpath("normalize-space(//span[@id='Content_Main_LB_DateTime']/text())").get()

        ptBR = response.xpath("//*[contains(@class, 'RCB_Culture_pt-BR')]/span/input/@value").get()
        enGB = response.xpath("//*[contains(@class, 'RCB_Culture_en-GB')]/span/input/@value").get()

        if ptBR == 'PT':
            match_date = utils.parse_ptbr_date(match_date_text)
        elif enGB == 'EN':
            match_date = utils.parse_engb_date(match_date_text)

        home_team_1 = response.xpath("normalize-space(//span[@id='Content_Main_LBL_HomeTeam']/text())").get().replace(' ', '-').lower()
        home_team = re.sub('[^A-Za-z0-9]+', '-', home_team_1)

        home_players = response.xpath("//div[@id='Content_Main_ctl17_RP_MatchStats_RPL_MatchStats_0']/div[3]/div/div/table/tbody/tr")

        for player in home_players:
            player_number = player.xpath("./td[1]/p/span/text()").get()
            player_name = player.xpath("./td[2]/p/span/b/text()").get()
            points_tot = player.xpath("./td[8]/p/span/text()").get()
            points_BP = player.xpath("./td[9]/p/span/text()").get()
            points_WL = player.xpath("./td[10]/p/span/text()").get()

            yield {
                'Match ID': self.match_id,
                'Match Date': match_date,
                'Home Team': home_team,
                'Number': player_number,
                'Name': player_name,
                'Total Points': points_tot,
                'Break Points': points_BP,
                'W-L': points_WL
            }

        self.match_date = match_date
        self.home_team = home_team

    def closed(spider, reason):
        os.rename('data/home_stats.csv', 'data/{}_{}_home_{}.csv'.format(spider.match_id, spider.match_date, spider.home_team))