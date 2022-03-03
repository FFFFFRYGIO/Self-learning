def generate_bc(url, separator):
    words_ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    keys_remove = ["https://","http://"]
    for key in keys_remove:
        if key in url:
            url = url.replace(key,'')
    if url[-1] == '/':
        url = url[:-1]
    print(url, separator)
    result = ''
    adresses = []
    adress = ''
    aname = ''
    anames = []
    for c in url:
        if c != '/':
            adress += c
            aname += c
        else:
            if len(aname) > 30:
                newaname = ''
                words = aname.split('-')
                for word in words:
                    if word not in words_ignore:
                        newaname += word[0]
                print(newaname)
                aname = newaname
            if '-' in aname:
                aname = aname.replace('-',' ')
            if len(adresses) > 1:
                adresses.append(adresses[-1] + '/' + adress)
            else:
                adresses.append(adress)
            adress = ''
            anames.append(aname)
            aname = ''

    adresses.append(adress)
    anames.append(aname)
    for i in range(len(adresses)):
        print(adresses[i], anames[i])
    
    if 'index' in adresses[-1]:
        adresses.pop(-1)
        anames.pop(-2)
    
    first = 1
    for i in range(len(adresses)):
        if first:
            if len(adresses) == 1:
                result += '<span class="active">HOME</span>'
            else:
                result += '<a href="/">HOME</a>'
            first = 0
        else:
            if adresses[i] == adresses[-1]:
                adresses[i] = adresses[i].split('/')[-1]
                link = ''
                for c in adresses[i]:
                    if c in '.#?':
                        break;
                    else:
                        link += c
                if len(link) > 30:
                    newaname = ''
                    words = link.split('-')
                    for word in words:
                        if word not in words_ignore:
                            newaname += word[0]
                    print(newaname)
                    link = newaname
                if '-' in link:
                    link = link.replace('-',' ')
                result += separator + '<span class="active">' + link.upper() + '</span>'
            else:
                result += separator + '<a href="/' + adresses[i] + '/">' + anames[i].upper() + '</a>'
    print(result)
    return result
