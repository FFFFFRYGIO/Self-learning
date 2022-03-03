def snail(snail_map):
    print(snail_map)
    result = []
    action = 'first line'
    while len(snail_map):
        if action == 'first line':
            for i in snail_map[0]:
                result.append(i)
            snail_map.pop(0)
            print(result)
            pass
            action = 'last column'
        
        elif action == 'last column':
            lc = len(snail_map[0]) - 1
            for i in range(len(snail_map)):
                result.append(snail_map[i][lc])
                snail_map[i].pop(lc)
            print(result)
            pass
            action = 'last line'
        
        elif action == 'last line':
            ll = len(snail_map) - 1
            for i in snail_map[ll][::-1]:
                result.append(i)
            snail_map.pop(ll)
            print(result)
            pass
            action = 'first column'
        
        elif action == 'first column':
            for i in range(len(snail_map)-1,0,-1):
                result.append(snail_map[i][0])
                snail_map[i].pop(0)
            print(result)
            pass
            action = 'first line'
    
    return result