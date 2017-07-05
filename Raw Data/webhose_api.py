import webhoseio

def get_raw_data_api():
    # Personal API Key
    API_key = #Personal Key

    # Config API Key
    webhoseio.config(token=API_key)

    # Filters + sites
    filters = 'language:english thread.country:US site_type:news spam_score:<0.5 '
    sites = 'site:(economist.com OR bbc.com OR npr.org OR pbs.org OR wsj.com OR cbsnews.com OR nbcnews.com)'

    query_param = filters + sites

    # Perform Query
    r = webhoseio.query("filterWebContent", {'q': query_param})

    # Save result in posts
    posts = r['posts']

    return posts

if __name__ == '__main__':
	get_raw_data_api()
