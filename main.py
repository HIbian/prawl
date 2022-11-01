import httpx
import re
from lxml import etree

animation_url = 'https://www.bimiacg4.net/bangumi/bi/{}'
animation_code = '8127'
animation_play_url = 'https://www.bimiacg4.net/bangumi/{}/play/{}/{}/'
m3u8_url = 'https://www.bimiacg4.net/static/danmu/m3u8/play.php?url={}'
_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
# todo 调整常量为变量
advance_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'referer': 'https://www.bimiacg4.net/bangumi/{}/play/{}/{}/'
}


def get_play_thread():
    global _header
    global animation_url
    global animation_code
    response = httpx.get(
        url=animation_url.format(animation_code),
        headers=_header,
        verify=False
    ).content.decode('utf-8')
    html = etree.HTML(response)
    thread_num = 1
    thread_len = len(html.xpath('//*[@id="tab"]//*'))
    if thread_len != 1:
        for n in range(thread_len):
            if html.xpath('//*[@id="tab"]//*')[n].text.__contains__('KK'):
                thread_num = n + 1
    return thread_num


def get_m3u8(tn):
    global _header
    global animation_play_url
    global animation_code
    global m3u8_url
    response = httpx.get(
        # url=animation_play_url.format(animation_code, tn, 1),
        # todo 调整常量为变量
        url='https://www.bimiacg4.net/bangumi/8127/play/2/10/',
        headers=_header,
        verify=False
    ).content.decode('utf-8')
    html = etree.HTML(response)
    var_aaaa_url = html.xpath('//*[@id="video"]/script')[1].text
    url = re.findall(r'url":"(.+?)"', var_aaaa_url)[0]
    return m3u8_url.format(url)


def download_m3u8(d_url):
    global advance_header
    respose = httpx.get(
        url=d_url,
        headers=advance_header,
        verify=False
    )
    with open('d.m3u8', 'w') as f:
        f.write(respose.text)
    print('down')


if __name__ == '__main__':
    # add this to test git
    tn = get_play_thread()
    print(tn)
    m_url = get_m3u8(tn)
    print(m_url)
    download_m3u8(m_url)
