email = "taimurlukas@gmail.com"
password = "mlhmlh"
clientID = "938"
clientSecret = "bkzasRJgHn9tcvT3"

from mendeley import Mendeley

mendeley = Mendeley(clientID, clientSecret)
session = mendeley.start_client_credentials_flow().authenticate()

doi = raw_input('Enter a DOI: ')

doc = session.catalog.by_identifier(doi=doi, view='all')

print doc.link

#print '"%s" has %s readers.' % (doc.title, doc.reader_count)


