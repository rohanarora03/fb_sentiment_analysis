import metadata_parser
l=['photos','videos','posts']
class page_id(object):

    def return_id(self,URL):
        s = ""

        page = metadata_parser.MetadataParser(url=URL)
        meta = page.metadata

        # print meta['meta']['al:ios:url']

        s = meta['meta']['al:ios:url']
        return s.strip("fb://page/?id=")

a = page_id()
url='https://www.facebook.com/georgehtakei/photos/a.223098324386295.105971.205344452828349/2295909770438463/?type=3&theater'
x=url.split("/")
print(x)
for i in x:
    if i in l:
        initial = url.split(i)
        z=initial[0]+i
        print(z)
print(a.return_id(z))