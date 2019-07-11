# coding:utf-8
# 爬虫获取知网信息
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv

# 设置谷歌浏览器的驱动环境
options = webdriver.ChromeOptions()
# 设置Chrome不加载图片，提高速度
options.add_experimental_option(name='prefs', value={'profile.managed_default_content_settings.images': 2})
# 创建一个谷歌浏览器
browser = webdriver.Chrome(options=options, executable_path='/Users/zhangyajun/Desktop/Python/chromedriver')
# browser = webdriver.Chrome(options=options, executable_path=r'‎/Users/zhangyajun/Desktop/Python_learn/BuXianXian/chromedriver')
# 最小化窗口
browser.minimize_window()
url = 'http://wap.cnki.net/touch/web/guide'


def start_spoder(page):
    # 请求url
    browser.get(url)
    # 显示等待输入框是否加载完成
    WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located(By.ID, 'keyword'))
    # 找到输入框的ID，并输入关键字
    word = input("请输入要检索的关键字：")
    print('\n请稍等片刻！')
    browser.find_element_by_id('btnSearch').click()
    print(browser.page_source)
    # 显示等待文献是否加载完成
    WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'g-search-body')))
    # 声明一个标记，用来标记翻页几页
    count = 1
    while True:
        # 显示等待加载更多按钮加载完成
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'c-company__body-item-more')))
        # 获取加载更多按钮
        btn = browser.find_element_by_class_name('c-company__body-item-more')
        # 显示等待该信息加载完成
        # WebDriverWait(browser,1000).until(EC.presence_of_all_elements_locateelements_located((By.XPATH,'//div[@id="searchlist_div"]')))
        WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))))
        divs = browser.find_elements_by_xpath(
            '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2 * count - 1))
        # 遍历循环
        for div in divs:
            # 获取文献的题目
            name = div.find_element_by_class_name('c-company__body-title').text
            # 获取文献的作者
            author = div.find_element_by_class_name('c-company__body-title').text
            # 获取文献的来源和日期、文件类型等
            text = div.find_element_by_class_name('c-company__body-name').text.split()
            if (len(text) == 3 and text[-1] == '优先' or len(text) == 2):
                source = text[0]
                datetime = text[1]
                literature_type = text[2]
            else:
                source = text[0]
                datetime = text[2]
                literature_type = text[1]

            data = (name, author, source, datetime, literature_type)
            with open('‎/Users/zhangyajun/Desktop/Python/data.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)

        if not btn:
            break
        else:
            btn.click()

        if count == page:
            break
        count += 1
        time.sleep(3)


if __name__ == '__main__':
    with open('/Users/zhangyajun/Desktop/Python/data.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('文献名', '作者', '来源', '发表日期', '文件类型'))
        # f.write(('文献名', '作者', '来源', '发表日期', '文件类型'))

    # start_spider(page=eval(0))
    browser.close()
    print("爬取完成，请到相应的文件夹查看")
