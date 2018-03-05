# -*- coding: utf-8 -*-

categories=['Computers', 'Car', 'Electronics', 'House', 'Video Games', 'Misc.']
locations=['Bakersfield', 'Chico', 'Fresno', 'Gold Country', 'Hanford', 'Inland Empire', 'Las Vegas', 'Los Angeles', 'Mercred', 'Modestro', 'Orange Co', 'Palm Springs', 'Reno', 'Sacramento', 'San luis Obispo', 'Santa Barbara', 'Stockton''San Jose', 'Santa Cruz']

db.define_table('posts',
                Field('title', requires=IS_NOT_EMPTY()),
                Field('interests'),
                Field('offers'),
                Field('category', requires=IS_IN_SET(categories)),
                Field('locations', requires=IS_IN_SET(locations)),
                Field('image', 'upload'),
                Field('User_ID', 'reference auth_user', readable=False, writable=False),
                auth.signature)
                
db.define_table('messages',
                Field('body', 'text'),
                Field('recepient'),
                Field('isRead', 'boolean'),
                auth.signature)
db.define_table('rating',
                Field('User_ID', 'reference auth_user', readable=False, writable=False),
                Field('Rcount', 'float'),
                Field('score', 'float'),
                Field('rating', 'float'))
db.rating.Rcount.default = 1;
db.define_table('votes',
                Field('Rater','reference auth_user', readable=False, writable=False),
                Field('Ratee','reference auth_user'),
                Field('Vtype'),
                Field('score','float'))

db.define_table('profile',
                Field('User_ID','reference auth_user', readable=False, writable=False),
                Field('image','upload'),
                Field('zip_code'),
                Field('age','integer'),
                Field('about_me','text'))
db.profile.zip_code.requires = IS_MATCH('^\d{5}(-\d{4})?$',
         error_message='not a zip code')
