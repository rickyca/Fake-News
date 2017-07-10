from raw_data_reader import *
import pandas as pd

def dict_trimmer(news, wanted_keys):
    news_dict = {}
    for key in news.keys():
        if type(news[key]) == dict:
            for sub_key in news[key].keys():
                if sub_key in wanted_keys and sub_key not in news_dict.keys():
                    news_dict[sub_key] = news[key][sub_key]
        else:
            if key in wanted_keys and key not in news_dict.keys():
                news_dict[key] = news[key]
    news_dict['type'] = 'normal'
    return news_dict

def dict_keys_check(news, wanted_keys):
    return [a for a in wanted_keys if a not in news.keys()]

def dict_social_replacer(news):
    temp = news['social']['facebook']
    del news['social']
    news = dict(news.items() + temp.items())
    return news

def dict_maker(news, wanted_keys):
    news = dict_trimmer(news, wanted_keys)
    news = dict_social_replacer(news)
    return news

def parse():

    raw_data = read_raw_data('raw_data_4.p')

    original_wanted_keys = [u'uuid', u'ord_in_thread', u'author', u'published', u'title', u'text',
                            u'language', u'crawled', u'site_url', u'country', u'domain_rank',
                            u'thread_title', u'spam_score', u'main_img_url', u'replies_count',
                            u'participants_count', u'likes', u'comments', u'shares', u'type']

    # Changing site_url to site,
    # Changing thread_title to section_title (check this),
    # Replacing likes, comments, shares with social
    # Erasing type (manually put in the function)
    # Chaging main_img_url to main_image
    wanted_keys = [u'uuid', u'ord_in_thread', u'author', u'published', u'title', u'text',
                   u'language', u'crawled', u'site', u'country', u'domain_rank',
                   u'section_title', u'spam_score', u'main_image', u'replies_count',
                   u'participants_count', u'social']

    news_dict_list = []
    for entry in raw_data:
        for news in entry:
            news_dict_list.append(dict_maker(news, wanted_keys))

    df = pd.DataFrame(news_dict_list)
    df.to_csv('parsed_data.csv', encoding='utf-8', index=False)

    return

if __name__ == '__main__':
    parse()
