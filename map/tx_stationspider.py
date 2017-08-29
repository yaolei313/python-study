# 长途汽车站(东直门站) ==> 东直门长途汽车站
# 这种统一转换为后者

from urllib import request, parse
import gzip
import json
import time

# get
SEARCH_URL = 'http://apis.map.qq.com/ws/place/v1/search?'

DEFAULT_HEADERS = {
    # 'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip'
}


def construct_param_dict(city, page_index):
    return {
        'boundary': 'region({0}, 0)'.format(city),
        'keyword': '长途汽车站',
        'filter': 'category=长途汽车站',
        'page_size': '20',
        'page_index': '{0}'.format(page_index),
        'orderby': '_distance',
        'key': 'Y75BZ-EIXCD-2SY4J-PX2OE-AFWJ5-GBBCJ'
    }


def single_request_to_tx_map(city, index):
    param_dict = construct_param_dict(city, index)
    param_str = parse.urlencode(param_dict)

    request_obj = request.Request(url=SEARCH_URL + param_str, headers=DEFAULT_HEADERS)
    with request.urlopen(request_obj) as rsp:
        if rsp.info().get('Content-Encoding') == 'gzip':
            rsp_body = gzip.decompress(rsp.read()).decode('utf-8')
        else:
            rsp_body = rsp.read().decode('utf-8')
    return rsp_body


def is_valid_station(station_name):
    # 包含一定不是
    if "进站" in station_name or "候车" in station_name or "公司" in station_name:
        return False

    index = str(station_name).find("(")
    if index == -1:
        index = str(station_name).find("（")

    new_name = station_name
    if index != -1:
        new_name = str(station_name)[:index]

    # 只要结尾一定是
    if new_name.endswith('枢纽') or new_name.endswith('客运中心') or new_name.endswith('客运站') or new_name.endswith('汽运站'):
        return True

    if "汽车" in new_name and new_name.endswith('站') and not ("公交" in new_name or "公共" in new_name or "出租" in new_name):
        return True

    return False


def spider_one_city(city):
    """
    返回一个dict，key为ad_code(int),value为车站元组list，车站元组为(名称,地址,电话,lat,lng)

    :param city:
    :return:
    """
    result_dict = {}
    cur_page = 1
    while True:
        print('spider page ', cur_page)
        body = single_request_to_tx_map(city, cur_page)
        my_dict = json.loads(body)
        if my_dict['status'] == 0:
            total_count = my_dict['count']
            data_list = my_dict['data']
            this_count = len(data_list)
            for item in data_list:
                station_name = item.get('title', '').strip()
                if not is_valid_station(station_name):
                    print("invalid ", item)
                    continue

                station_address = item.get('address', '').strip()
                station_tel = item.get('tel', '').strip()
                location = item.get('location')
                if location:
                    station_lat = str(location.get('lat', ''))
                    station_lng = str(location.get('lng', ''))
                else:
                    station_lat = ''
                    station_lng = ''
                ad_info = item.get('ad_info')
                if ad_info:
                    ad_code = str(ad_info.get('adcode'))
                else:
                    ad_code = None

                if not ad_code:
                    raise Exception('data invalid', body)

                station_tuple = (station_name, station_address, station_tel, station_lat, station_lng)
                if not result_dict.get(ad_code):
                    result_dict[ad_code] = list()
                result_dict.get(ad_code).append(station_tuple)
            if this_count == 20:
                # 下一个页面请求
                cur_page += 1
                time.sleep(1)
            elif this_count < 20:
                break
            else:
                raise Exception('what happened?')
        else:
            raise Exception('call fail', body)
    print('total count {} from {}'.format(total_count, city))
    return result_dict


if __name__ == "__main__":
    my_dict = spider_one_city('广州市')
    print(json.dumps(my_dict))
    # print(single_request_to_tx_map('东城区', 1))
    # is_valid_station('太平场汽车站茶烟酒区')
