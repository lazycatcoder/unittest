def get_country(iso_code=None):
    country_dict = {
        'US': {
            'name': 'United States of America'
        },
        'CA': {
            'name': 'Canada'
        },
        'UK': {
            'name': 'United Kingdom'
        },
        'DE': {
            'name': 'Germany'
        },
        'JP': {
            'name': 'Japan'
        },
        'AU' : {
            'name' : 'Australia'
        }
    }

    if type(iso_code) != str:
        raise TypeError('iso_code need to be a string')
    elif len(iso_code) != 2:
        raise ValueError('iso_code need to be 2 characters long')

    if iso_code in country_dict:
        return True, country_dict[iso_code]
    else:
        return False, None