#adaptove information process kr sktey hain
def build_profile(first, last, **user_info):

    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile
user_profile = build_profile('muhammad', 'zahid',
 location='karachi',
 field='computer',
  age='23',
  mariatl_status='Single'  )
print(user_profile)