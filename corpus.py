import twint

# Twint has been fixed by hand, version as per requirements.txt has broken format.py and url.py
# I advise using someone's fork of twint or a different library altogether as twint is evidently abandoned

c = twint.Config()

c.Links = 'exclude'
c.Limit = 1000
c.Lang = 'en'
c.Format = "{tweet}"
c.Output = 'corpusPS.txt'
c.Search ='#PS5 OR #PlayStation'
twint.run.Search(c)

c.Output = 'corpusXB.txt'
c.Search ='#Xbox'
twint.run.Search(c)
