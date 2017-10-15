import requests  
import json


def givecity(city):  
    url = 'https://api.teleport.org/api/cities/?search=' + city
    response = requests.get(url).json()
    return response


def corr_city(response): 
    while True:
        data = response['_embedded']['city:search-results']
        count = response['count']
        if count == 0:
            print('den uparxei tetoia polh prospathiste ksana\n')
            city = input('Dwse thn polh ksana ')
            response = get_response(city)
        elif count > 1:
            print('--------------------------------')
            for i in range(0, count):
                print(data[i]['matching_full_name'])
            print('--------------------------------')
            print('polles poleis exoun ayto to onoma, kai malista kapoies sundeontai me komma\n')
            print('paradeigma: Delhi, NCT, India\n')
            city = input('Dwse thn polh ksana ')
            response = givecity(city)
        elif count==1:
            href = data[0]['_links']['city:item']['href']
            link = requests.get(href).json()
            if 'city:urban_area' in link['_links']:
                  
                  return href, response
            





def thecityscore(href):      
    link = requests.get(href).json()
    link2scores = link['_links']['city:urban_area']['href'] + 'scores'
    list_of_scores = requests.get(link2scores).json()
    return list_of_scores


def compare_cities(score_1, score_2): 
    count1 = 0
    count2 = 0
    maxlen = len(scores_1['categories'])
    for i in range(0, maxlen):
        if score_1['categories'][i]['score_out_of_10'] > score_2['categories'][i]['score_out_of_10']:
            count1 =count1+ 1
        elif score_1['categories'][i]['score_out_of_10'] < score_2['categories'][i]['score_out_of_10']:
            count2 =count2 + 1
        else:
            pass
    return count1, count2


if __name__ == '__main__':
    city1 = input('Dwse thn polh')
    response1 = givecity(city1)
    href_c1, response1 = corr_city(response1)
   
    citynameone = str(response1['_embedded']['city:search-results'][0]['matching_full_name']).split(", ")
    city2 = input('Dwse thn deyterh polh ')
    print('\n')
    response2 = givecity(city2)
    href_c2, response2 = corr_city(response2)
    
    citynametwo = str(response2['_embedded']['city:search-results'][0]['matching_full_name']).split(", ")
    scores_1 = thecityscore(href_c1)
    scores_2 = thecityscore(href_c2)

  

    if scores_1['teleport_city_score'] > scores_2['teleport_city_score']:
        count_1, count_2 = compare_cities(scores_1, scores_2)

       
        print('{} uperexei {} se {} apo tis 17 kathgories\n'.format(
            citynameone[0],
            citynametwo[0],
            count_1))
        
        print('{} uperexei {} se {} apo tis 17 kathgories\n'.format(
            citynametwo[0],
            citynameone[0],
            count_2))
        
        if(count_1==0 and count_2==0):
           print('den uparxei bathmologia gia , {}({},{}) kai den uparxei bathmologia gia {}({},{})'.format(
            citynameone[0], citynameone[1], citynameone[2],
            citynametwo[0], citynametwo[1], citynametwo[2]))
        elif(count_1==count_2):
            print('  {}({},{}) idia bathmologia me ,   {}({},{})'.format(
             citynameone[0], citynameone[1], citynameone[2],
            citynametwo[0], citynametwo[1], citynametwo[2]))
        else:
            print('H, {}({},{}) pernaei thn {}({},{})'.format(
            citynameone[0], citynameone[1], citynameone[2],
            citynametwo[0], citynametwo[1], citynametwo[2]))
    else:
        count_2, count_1 = compare_cities(scores_2, scores_1)

        
        print('{}  uperexei {} se {} apo tis 17 kathgories\n'.format(
            citynametwo[0],
            citynameone[0],
            count_2))

       
        print('{}  uperexei {} se {} apo tis 17 kathgories\n'.format(
            citynameone[0],
            citynametwo[0],
            count_1))
       
        if(count_1==0 and count_2==0):
           print('den uparxei bathmologia gia , {}({},{}) kai den uparxei bathmologia gia {}({},{})'.format(
                
             citynametwo[0], citynametwo[1], citynametwo[2],
             citynameone[0], citynameone[1], citynameone[2]))
        elif(count_1==count_2):
            print('{}({},{}) idia bathmologia me ,   {}({},{})'.format(
            citynametwo[0], citynametwo[1], citynametwo[2],
            citynameone[0], citynameone[1], citynameone[2]))
        else:
            print('H, {}({},{}) pernaei thn {}({},{})'.format(
            citynametwo[0], citynametwo[1], citynametwo[2],
            citynameone[0], citynameone[1], citynameone[2]))
