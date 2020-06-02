import sendgrid
import json

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(API_KEY)


def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    stats = json.loads(response.body)
    max_data = max(stats[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    return (max_data['name'])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2017-07-10 was ' + best_country('2017-07-10'))
    print('Check your results')
