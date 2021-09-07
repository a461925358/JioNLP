# -*- coding=utf-8 -*-

import time
import datetime
import unittest

import jionlp as jio


class TestTimeParser(unittest.TestCase):
    """ 测试时间解析工具 """

    def test_time_parser(self):
        """ test func time_parser """

        _ts_1 = 1623604000
        _ts_2 = 1630480532
        print('time stamp for test: ',
              time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_ts_1)))

        time_string_list = [
            # 标准数字 年、月、日、时、分、秒
            ['2019/04/19', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-04-19 00:00:00', '2019-04-19 23:59:59']}],
            ['2018-11-29 18:59', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2018-11-29 18:59:00', '2018-11-29 18:59:59']}],
            ['2019-05-27 09:36:46', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-05-27 09:36:46', '2019-05-27 09:36:46']}],
            ['2018-12-1209:03', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2018-12-12 09:03:00', '2018-12-12 09:03:59']}],
            ['2019.9.6', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-09-06 00:00:00', '2019-09-06 23:59:59']}],
            ['1994.01-19', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['1994-01-19 00:00:00', '1994-01-19 23:59:59']}],
            ['1999.08-2002.02', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['1999-08-01 00:00:00', '2002-02-28 23:59:59']}],
            ['2008.03-2009', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2008-03-01 00:00:00', '2009-12-31 23:59:59']}],
            ['2019.05.29 15:20-2020.01.12 12:10', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-05-29 15:20:00', '2020-01-12 12:10:59']}],
            ['6·30', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-30 00:00:00', '2021-06-30 23:59:59']}],
            ['2018', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2018-01-01 00:00:00', '2018-12-31 23:59:59']}],

            # 年、月、日（标准）
            ['2015年8月12日', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2015-08-12 00:00:00', '2015-08-12 23:59:59']}],
            ['15年3月2日', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2015-03-02 00:00:00', '2015-03-02 23:59:59']}],
            ['03年2月28日', datetime.datetime(2021, 5, 6), {'type': 'time_point', 'definition': 'accurate', 'time': ['2003-02-28 00:00:00', '2003-02-28 23:59:59']}],
            ['9月30日', [2008, 3, 13], {'type': 'time_point', 'definition': 'accurate', 'time': ['2008-09-30 00:00:00', '2008-09-30 23:59:59']}],
            ['98年4月', [1997, 7, 1, 12, 30, 0], {'type': 'time_point', 'definition': 'accurate', 'time': ['1998-04-01 00:00:00', '1998-04-30 23:59:59']}],
            ['12月30号', {'year': 1837}, {'type': 'time_point', 'definition': 'accurate', 'time': ['1837-12-30 00:00:00', '1837-12-30 23:59:59']}],
            ['零七年八月二十九号', 1509329124., {'type': 'time_point', 'definition': 'accurate', 'time': ['2007-08-29 00:00:00', '2007-08-29 23:59:59']}],
            ['九零年9月十号', 109329124., {'type': 'time_point', 'definition': 'accurate', 'time': ['1990-09-10 00:00:00', '1990-09-10 23:59:59']}],
            ['十二月20号', 109329124., {'type': 'time_point', 'definition': 'accurate', 'time': ['1973-12-20 00:00:00', '1973-12-20 23:59:59']}],
            ['二零零三年十二月', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2003-12-01 00:00:00', '2003-12-31 23:59:59']}],
            ['二〇〇六年十二月', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2006-12-01 00:00:00', '2006-12-31 23:59:59']}],
            ['2023年', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2023-01-01 00:00:00', '2023-12-31 23:59:59']}],
            ['三三年', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2033-01-01 00:00:00', '2033-12-31 23:59:59']}],

            # （限定）年、季度（公历）
            ['07年第三季度', [2008, 3, 2, 0], {'type': 'time_span', 'definition': 'accurate', 'time': ['2007-07-01 00:00:00', '2007-09-30 23:59:59']}],
            ['2021年前两个季度', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2021-06-30 23:59:59']}],
            ['2022年首季度', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2022-01-01 00:00:00', '2022-03-31 23:59:59']}],
            ['九七年一季度', [1999, 9, 2], {'type': 'time_span', 'definition': 'accurate', 'time': ['1997-01-01 00:00:00', '1997-03-31 23:59:59']}],
            ['一季度', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2021-03-31 23:59:59']}],
            ['今年前三季度', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2021-09-30 23:59:59']}],
            ['上个季度', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2021-03-31 23:59:59']}],

            # 年、模糊月份指示信息
            ['19年底', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2019-11-01 00:00:00', '2019-12-31 23:59:59']}],
            ['1993年上半年', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1993-01-01 00:00:00', '1993-06-30 23:59:59']}],
            ['二零二二年伊始', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2022-01-01 00:00:00', '2022-01-31 23:59:59']}],

            # 年（限定）、模糊月
            ['明年初', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2022-01-01 00:00:00', '2022-02-28 23:59:59']}],
            ['明年年初', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2022-01-01 00:00:00', '2022-02-28 23:59:59']}],
            ['次年年末', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2022-11-01 00:00:00', '2022-12-31 23:59:59']}],
            ['去年暑假', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2020-07-01 00:00:00', '2020-08-31 23:59:59']}],
            ['年底', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-11-01 00:00:00', '2021-12-31 23:59:59']}],
            ['年底前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2021-12-31 23:59:59']}],

            # 限定月、日
            ['同月9号17点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-09 17:00:00', '2021-06-09 17:59:59']}],
            ['上个月15号', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-05-15 00:00:00', '2021-05-15 23:59:59']}],
            ['下月九号', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-07-09 00:00:00', '2021-07-09 23:59:59']}],
            ['本月9日', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-09 00:00:00', '2021-06-09 23:59:59']}],

            # 限定月、模糊日
            ['本月初', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-01 00:00:00', '2021-06-05 23:59:59']}],
            ['当月', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-01 00:00:00', '2021-06-30 23:59:59']}],

            # 世纪、年代
            ['18世纪', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1700-01-01 00:00:00', '1799-12-31 23:59:59']}],
            ['上世纪80年代', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1980-01-01 00:00:00', '1989-12-31 23:59:59']}],
            ['十九世纪七十年代', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1870-01-01 00:00:00', '1879-12-31 23:59:59']}],
            ['二十世纪九十年代末期', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1997-01-01 00:00:00', '1999-12-31 23:59:59']}],
            ['11世纪初', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1000-01-01 00:00:00', '1019-12-31 23:59:59']}],
            ['20世纪60年代前期', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1960-01-01 00:00:00', '1962-12-31 23:59:59']}],
            # -> 公元前二世纪，可以检测到，但无法转换为标准时间而报错

            # （限定）年、范围月
            ['2022年前十一个月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2022-01-01 00:00:00', '2022-11-30 23:59:59']}],
            ['70年第8个月', [1965, 10, 1, 12, 30, 0], {'type': 'time_span', 'definition': 'accurate', 'time': ['1970-08-01 00:00:00', '1970-08-31 23:59:59']}],
            ['2005年首月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2005-01-01 00:00:00', '2005-01-31 23:59:59']}],
            ['五八年前七个月', 10, {'type': 'time_span', 'definition': 'accurate', 'time': ['1958-01-01 00:00:00', '1958-07-31 23:59:59']}],
            ['二零二一年后三月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-10-01 00:00:00', '2021-12-31 23:59:59']}],
            ['1967年前两月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['1967-01-01 00:00:00', '1967-02-28 23:59:59']}],
            ['今年前五个月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2021-05-31 23:59:59']}],

            # 年（限定）、月、日
            ['去年3月3号', {'year': 1966}, {'type': 'time_span', 'definition': 'accurate', 'time': ['1965-03-03 00:00:00', '1965-03-03 23:59:59']}],
            ['今年六月', {'year': 1966}, {'type': 'time_span', 'definition': 'accurate', 'time': ['1966-06-01 00:00:00', '1966-06-30 23:59:59']}],
            ['明年3月份', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2022-03-01 00:00:00', '2022-03-31 23:59:59']}],
            ['上一年', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2020-01-01 00:00:00', '2020-12-31 23:59:59']}],

            # 年（模糊限定）
            ['3年后', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['2024-01-01 00:00:00', '2024-12-31 23:59:59']}],
            ['两年前', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['2019-01-01 00:00:00', '2019-12-31 23:59:59']}],
            ['一年半以前', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2019-07-31 23:59:59']}],
            ['一年半以前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2019-12-31 23:59:59']}],
            ['半年之后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-12-01 00:00:00', 'inf']}],
            # ['40多年前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1971-01-01 00:00:00', '1981-12-31 23:59:59']}],
            ['二十几年前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['1991-01-01 00:00:00', '2001-12-31 23:59:59']}],
            ['1000多年之后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['3020-01-01 00:00:00', 'inf']}],
            ['几十年之后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2041-01-01 00:00:00', '2121-12-31 23:59:59']}],

            # time span 式 `从……至……` 年、月、日、时、分、秒
            ['2017年8月11日至8月22日', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2017-08-11 00:00:00', '2017-08-22 23:59:59']}],
            ['2017年8月15日至2018年3月29日', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2017-08-15 00:00:00', '2018-03-29 23:59:59']}],
            ['2017年8月至11月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2017-08-01 00:00:00', '2017-11-30 23:59:59']}],
            ['2017年五月至2018年四月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2017-05-01 00:00:00', '2018-04-30 23:59:59']}],
            ['二〇一九年5月8日起', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-05-08 00:00:00', '2021-06-14 01:06:40']}],
            ['从去年9月起', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2020-09-01 00:00:00', '2021-06-14 01:06:40']}],
            ['从2001年起至今', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2001-01-01 00:00:00', '2021-06-14 01:06:40']}],
            ['从2008年——2018年', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2008-01-01 00:00:00', '2018-12-31 23:59:59']}],
            ['从2015年1月至12月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2015-01-01 00:00:00', '2015-12-31 23:59:59']}],
            ['从2018年12月九号到十五号', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2018-12-09 00:00:00', '2018-12-15 23:59:59']}],
            ['2019年感恩节到2021年母亲节', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-11-28 00:00:00', '2021-05-09 23:59:59']}],
            ['去年春节到元宵节', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-05 00:00:00', '2019-02-19 23:59:59']}],
            ['明年6月之前', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2022-06-30 23:59:59']}],
            ['1985到89年9月', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['1985-01-01 00:00:00', '1989-09-30 23:59:59']}],
            ['2019年4月12-19日', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-04-12 00:00:00', '2019-04-19 23:59:59']}],
            ['9~12点半', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 09:00:00', '2021-06-14 12:30:59']}],
            ['2019年1-五月', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-01-01 00:00:00', '2019-05-31 23:59:59']}],
            ['2018年1－9月份', {'year': 2020}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2018-01-01 00:00:00', '2018-09-30 23:59:59']}],
            ['2020至2025年前', time.time(), {'type': 'time_span', 'definition': 'accurate', 'time': ['2020-01-01 00:00:00', '2025-12-31 23:59:59']}],
            ['从上个月到今天', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-05-01 00:00:00', '2021-06-14 01:06:40']}],

            ['2018年2——4月', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2018-02-01 00:00:00', '2018-04-30 23:59:59']}],
            ['明年底前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2022-12-31 23:59:59']}],
            ['明年初之前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2022-02-28 23:59:59']}],
            ['2025年前', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2025-12-31 23:59:59']}],
            ['二零四九年十月一号以前', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2049-10-01 23:59:59']}],
            ['三年前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2018-01-01 00:00:00', '2018-12-31 23:59:59']}],
            ['二〇三五年前', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2035-12-31 23:59:59']}],

            # 农历年、月、日
            ['二零一二年农历正月十五', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2012-02-06 00:00:00', '2012-02-06 23:59:59']}],
            ['农历二〇二一年六月', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-07-10 00:00:00', '2021-08-07 23:59:59']}],
            ['五月廿二', {'year': 2022}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2022-06-20 00:00:00', '2022-06-20 23:59:59']}],
            ['腊月初十', {'year': 2022}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2023-01-01 00:00:00', '2023-01-01 23:59:59']}],
            ['农历十月', {'year': 2022}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2022-10-25 00:00:00', '2022-11-23 23:59:59']}],
            ['农历闰四月', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-05-23 00:00:00', '2020-06-20 23:59:59']}],
            ['闰四月', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-05-23 00:00:00', '2020-06-20 23:59:59']}],
            ['闰4月', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-05-23 00:00:00', '2020-06-20 23:59:59']}],
            ['廿一', {'year': 2021, 'month': 5}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-30 00:00:00', '2021-06-30 23:59:59']}],
            ['正月', {'year': 2021, 'month': 5}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-02-12 00:00:00', '2021-03-12 23:59:59']}],
            ['去年五月初五', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-06-25 00:00:00', '2020-06-25 23:59:59']}],
            ['后年九月廿二', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2023-11-05 00:00:00', '2023-11-05 23:59:59']}],
            ['明年腊月', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2022-12-23 00:00:00', '2023-01-21 23:59:59']}],
            ['2012年正月初8', time.time(), {'type': 'time_point', 'definition': 'accurate', 'time': ['2012-01-30 00:00:00', '2012-01-30 23:59:59']}],

            # 年、节气
            ['2017年大寒', time.time(), {'type': 'time_point', 'definition': 'accurate', 'time': ['2018-01-20 00:00:00', '2018-01-20 23:59:59']}],
            ['20年小寒', time.time(), {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-01-06 00:00:00', '2021-01-06 23:59:59']}],
            ['芒种', {'year': 2021, 'month': 5}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-05 00:00:00', '2021-06-05 23:59:59']}],

            # 限定年、季节
            ['2021年春', {'year': 2021, 'month': 5}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-02-03 00:00:00', '2021-05-04 23:59:59']}],
            ['冬季', {'year': 2021, 'month': 5}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-11-07 00:00:00', '2022-02-02 23:59:59']}],
            ['大前年夏季', {'year': 2021}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2018-05-05 00:00:00', '2018-08-06 23:59:59']}],

            # 年、月、星期
            ['上周', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-07 00:00:00', '2021-06-13 23:59:59']}],
            ['这周', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-14 00:00:00', '2021-06-20 23:59:59']}],
            ['上上周', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-05-31 00:00:00', '2021-06-06 23:59:59']}],
            ['下周六', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-26 00:00:00', '2021-06-26 23:59:59']}],
            ['下周周六', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-26 00:00:00', '2021-06-26 23:59:59']}],
            ['前两周', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-05-31 00:00:00', '2021-06-14 01:06:40']}],
            ['4个星期之后', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-07-12 00:00:00', '2021-07-18 23:59:59']}],
            ['星期天', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-20 00:00:00', '2021-06-20 23:59:59']}],
            ['下个星期一', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-21 00:00:00', '2021-06-21 23:59:59']}],
            # `第三周周日` 这样的字符串几乎不会出现，因，在虚拟时间表述时，一般缺乏`周`的概念，而在具体时间表述时，会定义清楚周所处的月份。
            # 因此，单独针对`第三周周日`的解析，会默认所处年月为 time_base 的年月。
            ['6月第3个星期日', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-20 00:00:00', '2021-06-20 23:59:59']}],
            ['八月份的第一个周二', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-08-03 00:00:00', '2021-08-03 23:59:59']}],
            ['周二早上', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-15 06:00:00', '2021-06-15 09:59:59']}],
            ['6月1日周六早上10点钟', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-01 10:00:00', '2021-06-01 10:59:59']}],
            ['上个礼拜天', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-13 00:00:00', '2021-06-13 23:59:59']}],

            # 年、月、模糊日
            ['6月上旬', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-01 00:00:00', '2021-06-10 23:59:59']}],
            ['1999年7月下旬', time.time(), {'type': 'time_span', 'definition': 'blur', 'time': ['1999-07-11 00:00:00', '1999-07-31 23:59:59']}],
            ['九月下旬', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-09-11 00:00:00', '2021-09-30 23:59:59']}],
            ['8月初前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2021-08-05 23:59:59']}],
            ['2018年10月底', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2018-10-25 00:00:00', '2018-10-31 23:59:59']}],

            # 限定年、月、模糊日
            ['去年6月上旬', {'year': 2021}, {'type': 'time_span', 'definition': 'blur', 'time': ['2020-06-01 00:00:00', '2020-06-10 23:59:59']}],

            # 限定日
            ['前天', _ts_2, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-08-30 00:00:00', '2021-08-30 23:59:59']}],
            ['后天', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-16 00:00:00', '2021-06-16 23:59:59']}],
            ['今天', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 00:00:00', '2021-06-14 23:59:59']}],
            ['昨晚8时35分', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-13 20:35:00', '2021-06-13 20:35:59']}],
            ['当晚十时', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 22:00:00', '2021-06-14 22:59:59']}],

            # 年，节日
            ['教师节', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-09-10 00:00:00', '2021-09-10 23:59:59']}],
            ['十一', {'year': 2001}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2001-10-01 00:00:00', '2001-10-01 23:59:59']}],
            ['去年元旦', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-01-01 00:00:00', '2019-01-01 23:59:59']}],
            ['去年春节', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-05 00:00:00', '2019-02-05 23:59:59']}],
            ['零六年端午', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2006-05-31 00:00:00', '2006-05-31 23:59:59']}],
            ['明年母亲节', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-05-09 00:00:00', '2021-05-09 23:59:59']}],
            ['2019年感恩节', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-11-28 00:00:00', '2019-11-28 23:59:59']}],
            ['国庆', {'year': 2020}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-10-01 00:00:00', '2020-10-01 23:59:59']}],
            ['农历元宵', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-02-26 00:00:00', '2021-02-26 23:59:59']}],

            # 年月日 时分秒
            ['7月4日晚上7点09分18秒', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-07-04 19:09:18', '2021-07-04 19:09:18']}],
            ['去年7月4日晚上7点09分', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2020-07-04 19:09:00', '2020-07-04 19:09:59']}],
            ['早上7点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 07:00:00', '2021-06-14 07:59:59']}],
            ['下月15号下午6点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-07-15 18:00:00', '2021-07-15 18:59:59']}],
            # 存在6点前，包不包含6点的问题，须设置参数判定
            ['下月15号下午6点前', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2021-07-15 18:59:59']}],
            ['农历8月十五晚8点', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-09-21 20:00:00', '2021-09-21 20:59:59']}],
            ['上周六中午12点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-12 12:00:00', '2021-06-12 12:59:59']}],
            ['大前年七夕节半夜11点', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2018-08-17 23:00:00', '2018-08-17 23:59:59']}],
            # 某日夜晚指第二天夜晚还是当天夜晚，须设置参数判定，原因在于人的认知是早晨才是一天的开始  '21时~凌晨1时'
            ['大前年七夕节半夜1点', {'year': 2021}, {'type': 'time_point', 'definition': 'accurate', 'time': ['2018-08-17 01:00:00', '2018-08-17 01:59:59']}],
            ['下个月9号早上8点到中午12点', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-07-09 08:00:00', '2021-07-09 12:00:00']}],
            ['昨天9点20', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-13 09:20:00', '2021-06-13 09:20:59']}],
            ['上个月23号晚上九点零九', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-05-23 21:09:00', '2021-05-23 21:09:59']}],
            ['12月9日零时至12月16日24时', {'year': 2021}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-12-09 00:00:00', '2021-12-17 00:00:00']}],
            ['13:20~次日05:40', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 13:20:00', '2021-06-15 05:40:59']}],
            ['夜里12点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-15 00:00:00', '2021-06-15 00:59:59']}],
            ['下午5点多钟', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 17:00:00', '2021-06-14 17:59:59']}],

            # 时分秒 标准格式按 `:` 区隔
            ['上月30号12:37', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-05-30 12:37:00', '2021-05-30 12:37:59']}],
            ['35:37', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 01:35:37', '2021-06-14 01:35:37']}],
            ['15:37', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 15:37:00', '2021-06-14 15:37:59']}],
            ['2019年6月28日下午3:00', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-06-28 15:00:00', '2019-06-28 15:00:59']}],
            ['2019年6月28日9:30~11:30', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-06-28 09:30:00', '2019-06-28 11:30:59']}],
            ['中午12：00—14:00', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 12:00:00', '2021-06-14 14:00:59']}],
            ['大前天晚上9~11点', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-11 21:00:00', '2021-06-11 23:00:00']}],
            ['晚上6点', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 18:00:00', '2021-06-14 18:59:59']}],

            # 时、限定性 分
            ['4月26日20时1刻', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-04-26 20:15:00', '2021-04-26 20:15:59']}],
            ['去年十一月廿九下午4点半', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-01-12 16:30:00', '2021-01-12 16:30:59']}],
            ['9日0时至18时三刻', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-09 00:00:00', '2021-06-09 18:45:59']}],

            # 模糊时
            ['夜间至次日上午', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 20:00:00', '2021-06-15 11:59:59']}],
            ['当日午夜', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-14 00:00:00', '2021-06-14 00:59:59']}],
            ['白天', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-14 06:00:00', '2021-06-14 18:59:59']}],
            ['午后', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-14 13:00:00', '2021-06-14 14:59:59']}],

            # 时间段
            ['4周', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 28.0}}],
            ['4周年', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'year': 4.0}}],
            ['四个星期', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 28.0}}],
            ['四个多星期', None, {'type': 'time_delta', 'definition': 'blur', 'time': {'day': 28.0}}],
            ['两年半', None, {'type': 'time_delta', 'definition': 'blur', 'time': {'year': 2.5}}],
            ['17个多月', None, {'type': 'time_delta', 'definition': 'blur', 'time': {'month': 17.0}}],
            ['四年六个月', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'year': 4.0, 'month': 6.0}}],
            ['70多分钟', None, {'type': 'time_delta', 'definition': 'blur', 'time': {'minute': 70.0}}],
            ['270天', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 270.0}}],
            ['27分钟7秒', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'minute': 27.0, 'second': 7.0}}],
            ['2621.2小时', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'hour': 2621.2}}],
            ['五个季度', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'month': 15.0}}],
            ['2000万小时', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'hour': 20000000.0}}],
            ['三十三年', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'year': 33.0}}],
            ['35,000个钟头', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'hour': 35000.0}}],
            ['15个交易日', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'workday': 15.0}}],
            ['五个工作日', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'workday': 5.0}}],
            ['两日', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 2.0}}],
            ['俩礼拜', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 14.0}}],

            # 法律时间
            ['3年以上7年以下', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'year': 3.0}, {'year': 7.0}]}],
            ['十五年以上,30年以下', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'year': 15.0}, {'year': 30.0}]}],
            ['六个月以下', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'zero': True}, {'month': 6.0}]}],
            ['三十年以上', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'year': 30.0}, {'infinite': True}]}],

            # 模糊时间段
            # ['二十来天', None, ],
            # ['几十个小时', None, ],
            # ['无数个小时', None, ],

            # 经过歧义处理的时间段
            ['90日', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 90.0}}],
            ['30日', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-30 00:00:00', '2021-06-30 23:59:59']}],
            ['24年', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2024-01-01 00:00:00', '2024-12-31 23:59:59']}],
            ['30~90日', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'day': 30.0}, {'day': 90.0}]}],

            # 时间段转时间点
            ['20天以后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-07-04 00:00:00', 'inf']}],
            ['20天后', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-07-04 00:00:00', '2021-07-04 23:59:59']}],
            ['两天之前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2021-06-12 23:59:59']}],
            ['三个多月以来', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-03-01 00:00:00', '2021-06-14 01:06:40']}],
            ['20多个月之后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2023-02-01 00:00:00', 'inf']}],
            ['七年半后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2028-12-01 00:00:00', '2028-12-31 23:59:59']}],
            ['七年后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2028-01-01 00:00:00', '2028-12-31 23:59:59']}],
            ['半钟头后', _ts_1, {'type': 'time_point', 'definition': 'accurate', 'time': ['2021-06-14 01:36:40', '2021-06-14 02:06:59']}],
            # '25-35天内' 有两种解析方法， time_span 与 time_delta
            # `60日内` 有两种解析方法， time_span 与 time_delta，
            # `请在 60日内 完成`，指在 time_base + 60 天之前的范围内完成。
            # `25-35天内是我们做这项工作的合理时间安排`，指需要耗费的 time_delta。
            ['5个交易日之后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-21 00:00:00', 'inf']}],
            ['15个工作日内', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2021-07-05 23:59:59']}],
            ['60日内', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2021-08-13 23:59:59']}],

            # 若指定的 time_base 无法具体到 `日`，则指定的推算日期存在模糊和偏差
            ['半年后', [2019, 6], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-11-01 00:00:00', '2019-11-30 23:59:59']}],
            ['一年半后', [2019], {'type': 'time_span', 'definition': 'blur', 'time': ['2020-07-01 00:00:00', '2020-07-31 23:59:59']}],
            ['3年以前', [2019], {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2016-12-31 23:59:59']}],
            ['3年半前', [2019, 5], {'type': 'time_span', 'definition': 'blur', 'time': ['2015-10-01 00:00:00', '2015-10-31 23:59:59']}],
            ['3年半以前', [2019], {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2015-07-31 23:59:59']}],
            ['3年半以后', [2019], {'type': 'time_span', 'definition': 'blur', 'time': ['2022-07-01 00:00:00', 'inf']}],
            ['3年半以内', [2019], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-01-01 00:00:00', '2022-07-31 23:59:59']}],
            ['3年半以内', [2019, 9], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-09-01 00:00:00', '2023-03-31 23:59:59']}],
            ['3年半以来', [2019, 9], {'type': 'time_span', 'definition': 'blur', 'time': ['2016-03-01 00:00:00', '2019-09-30 23:59:59']}],
            ['3年半以来', [2019, 8, 22], {'type': 'time_span', 'definition': 'blur', 'time': ['2016-02-01 00:00:00', '2019-08-22 23:59:59']}],
            ['3年多以来', [2019, 8, 22], {'type': 'time_span', 'definition': 'blur', 'time': ['2016-01-01 00:00:00', '2019-08-22 23:59:59']}],
            ['3个多月以来', [2019, 8, 22], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-05-01 00:00:00', '2019-08-22 23:59:59']}],
            ['两个半月以内', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2021-08-29 23:59:59']}],
            ['两个半月前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-02-27 00:00:00', '2021-03-30 23:59:59']}],
            ['两个半月以前', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2021-03-30 23:59:59']}],
            ['半月以后', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-29 00:00:00', 'inf']}],
            ['十个多月后', [2019, 9], {'type': 'time_span', 'definition': 'blur', 'time': ['2020-07-01 00:00:00', '2020-07-31 23:59:59']}],
            ['十个半月后', [2019, 9], {'type': 'time_span', 'definition': 'blur', 'time': ['2020-07-16 00:00:00', '2020-08-15 23:59:59']}],
            ['17天后', [2019, 2, 18], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-03-07 00:00:00', '2019-03-07 23:59:59']}],
            ['17天内', [2019, 2, 18], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-18 00:00:00', '2019-03-07 23:59:59']}],
            ['7天半以来', [2019, 2, 18], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-10 12:00:00', '2019-02-18 23:59:59']}],
            ['一天半以来', [2019, 2, 18, 7], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-16 19:00:00', '2019-02-18 07:59:59']}],
            ['30天后', [2019, 2, 18, 7], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-03-20 00:00:00', '2019-03-20 23:59:59']}],
            ['6个小时前', [2019, 2, 18, 7], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 00:00:00', '2019-02-18 01:00:00']}],
            ['60小时前', [2019, 2, 18, 7], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-15 18:00:00', '2019-02-15 19:00:00']}],
            ['半小时前', [2019, 2, 18, 7], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 06:00:00', '2019-02-18 06:30:00']}],
            ['半小时以后', [2019, 2, 18, 7], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-02-18 07:30:00', 'inf']}],
            ['一个半小时后', [2019, 2, 18, 7, 18], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 08:48:00', '2019-02-18 09:48:59']}],
            ['半小时内', [2019, 2, 18, 7, 18], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-18 07:18:00', '2019-02-18 07:48:59']}],
            ['17钟头后', [2019, 2, 18, 7, 18], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-19 00:18:00', '2019-02-19 01:18:59']}],
            ['17分钟后', [2019, 2, 18, 7, 18], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 07:35:00', '2019-02-18 07:36:00']}],
            ['90分钟以内', [2019, 2, 18, 7, 18], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-18 07:18:00', '2019-02-18 08:48:00']}],
            ['92分钟以前', [2019, 2, 18, 7, 18], {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2019-02-18 05:46:00']}],
            ['一分钟半以前', [2019, 2, 18, 7, 18], {'type': 'time_span', 'definition': 'blur', 'time': ['-inf', '2019-02-18 07:16:30']}],
            ['一分半钟前', [2019, 2, 18, 7, 18, 40], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 07:16:10', '2019-02-18 07:17:10']}],
            ['十三分半以内', [2019, 2, 18, 7, 18, 40], {'type': 'time_span', 'definition': 'accurate', 'time': ['2019-02-18 07:18:40', '2019-02-18 07:32:10']}],
            ['十三秒后', [2019, 2, 18, 7, 18, 23], {'type': 'time_point', 'definition': 'accurate', 'time': ['2019-02-18 07:18:36', '2019-02-18 07:18:37']}],
            ['十三秒钟以后', [2019, 2, 18, 7, 18, 23], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-02-18 07:18:36', 'inf']}],
            ['三个季度后', [2019, 2, 18, 7], {'type': 'time_span', 'definition': 'blur', 'time': ['2019-11-01 00:00:00', '2019-11-30 23:59:59']}],
            ['4周后', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-07-12 00:00:00', '2021-07-18 23:59:59']}],

            # 序数 time_delta 转 time_point
            ['第三天上午', _ts_1, {'type': 'time_point', 'definition': 'blur', 'time': ['2021-06-16 07:00:00', '2021-06-16 11:59:59']}],
            ['第三天起', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-16 00:00:00', 'inf']}],
            ['第七年', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2027-01-01 00:00:00', '2027-12-31 23:59:59']}],

            # 另一种类型的 time_delta 转 time_span
            # 未来/今后
            ['未来2个月', {'year': 2021, 'month': 7}, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-07-01 00:00:00', '2021-08-31 23:59:59']}],
            ['未来两个月', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2021-08-13 23:59:59']}],
            ['未来5年内', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2026-06-13 23:59:59']}],
            ['未来7天', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2021-06-21 23:59:59']}],
            ['未来48小时', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:06:40', '2021-06-16 01:06:40']}],
            ['未来七十二小时内', {'year': 2021, 'month': 7, 'day': 3, 'hour': 14, 'minute': 32}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-07-03 14:32:00', '2021-07-06 14:32:59']}],
            ['今后10年', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-14 01:06:40', '2031-06-12 23:59:59']}],

            # 过去
            ['过去的一周', {'year': 2021, 'month': 7, 'day': 31, 'hour': 14, 'minute': 32}, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-07-24 00:00:00', '2021-07-31 14:32:59']}],
            ['过去的一年', {'year': 2021, 'month': 7, 'day': 31, 'hour': 14, 'minute': 32}, {'type': 'time_span', 'definition': 'blur', 'time': ['2020-07-31 00:00:00', '2021-07-31 14:32:59']}],
            # 过去5分钟，也可能是表示 度过5分钟，此时，并非静态时间，应当按 5分钟解析。故不支持该表述。
            ['过去5分钟', {'year': 2021, 'month': 7, 'day': 31, 'hour': 14, 'minute': 32}, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-07-31 14:27:00', '2021-07-31 14:32:59']}],
            ['过去的50分钟里', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 00:16:40', '2021-06-14 01:06:40']}],

            # 过
            ['再过半个小时', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 01:36:40', 'inf']}],
            ['过两天', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-06-16 00:00:00', 'inf']}],
            ['过十周', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-08-23 00:00:00', 'inf']}],

            # 前/头
            # “前俩月”、“头三天”: 指给定一个大的 time_span，指定其中的 前 time_delta 时间，返回应当为 time_span，但无具体时间范围。
            # 暂不支持，还有待分析考虑。

            # 近
            # ”近三年“、“近几天”：有 time_span 和 time_delta 两种解析方式。，默认为按 time_span 解析
            ['近30天', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-05-15 00:00:00', '2021-06-14 01:06:40']}],
            ['近三个月', _ts_1, {'type': 'time_span', 'definition': 'blur', 'time': ['2021-03-14 00:00:00', '2021-06-14 01:06:40']}],

            # 特殊时间范围
            ['全天', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-06-14 00:00:00', '2021-06-14 23:59:59']}],
            ['今明两年', _ts_1, {'type': 'time_span', 'definition': 'accurate', 'time': ['2021-01-01 00:00:00', '2022-12-31 23:59:59']}],

            # 特殊时间段
            ['大半天', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'day': 0.5}, {'day': 0.9}]}],
            ['6天5晚', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 6.0}}],
            ['三天三夜', None, {'type': 'time_delta', 'definition': 'accurate', 'time': {'day': 3.0}}],
            ['七载春秋', None, {'type': 'time_delta', 'definition': 'blur', 'time': {'year': 7.0}}],

            # 范围时间段
            ['3天——8天', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'day': 3.0}, {'day': 8.0}]}],
            ['13天—8周', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'day': 13.0}, {'day': 56.0}]}],
            ['13—18天', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'day': 13.0}, {'day': 18.0}]}],
            ['两万四千到3万秒', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'second': 24000.0}, {'second': 30000.0}]}],
            ['3~6个月', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'month': 3.0}, {'month': 6.0}]}],
            ['100到200个小时', None, {'type': 'time_delta', 'definition': 'blur', 'time': [{'hour': 100.0}, {'hour': 200.0}]}],

            # 时间周期
            ['每年', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 1}, 'point': None}}],
            ['每年9月', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 1}, 'point': {'time': ['2021-09-01 00:00:00', '2021-09-30 23:59:59'], 'string': '9月'}}}],
            ['每月4号', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'month': 1}, 'point': {'time': ['2021-06-04 00:00:00', '2021-06-04 23:59:59'], 'string': '4号'}}}],
            ['每半年', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 0.5}, 'point': None}}],
            ['每周三', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 7}, 'point': {'time': ['2021-06-16 00:00:00', '2021-06-16 23:59:59'], 'string': '周三'}}}],
            ['每半个钟头', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'hour': 0.5}, 'point': None}}],
            ['每隔3天', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 3.0}, 'point': None}}],
            ['每年母亲节', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 1}, 'point': {'time': ['2021-05-09 00:00:00', '2021-05-09 23:59:59'], 'string': '母亲节'}}}],
            ['每天晚上8点', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 1}, 'point': {'time': ['2021-06-14 20:00:00', '2021-06-14 20:59:59'], 'string': '晚上8点'}}}],
            ['每个星期天早上9点一刻', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 7}, 'point': {'time': ['2021-06-20 09:15:00', '2021-06-20 09:15:59'], 'string': '周天早上9点一刻'}}}],
            ['每隔200秒', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'second': 200.0}, 'point': None}}],
            ['每年秋天', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 1}, 'point': {'time': ['2021-08-07 00:00:00', '2021-11-06 23:59:59'], 'string': '秋天'}}}],

            # 时间周期与span
            ['每年9月到11月', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'year': 1}, 'point': {'time': ['2021-09-01 00:00:00', '2021-11-30 23:59:59'], 'string': '9月到11月'}}}],
            ['每周六上午9点到11点', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 7}, 'point': {'time': ['2021-06-19 09:00:00', '2021-06-19 11:00:00'], 'string': '周六上午9点到11点'}}}],
            ['每天晚上8点——9点', _ts_1, {'type': 'time_period', 'definition': 'accurate', 'time': {'delta': {'day': 1}, 'point': {'time': ['2021-06-14 20:00:00', '2021-06-14 21:00:00'], 'string': '晚上8点——9点'}}}],

        ]

        for item in time_string_list:
            time_res = jio.parse_time(item[0], time_base=item[1])
            print(item[0])
            self.assertEqual(time_res, item[2])


if __name__ == '__main__':

    suite = unittest.TestSuite()
    test_time_parser = [TestTimeParser('test_time_parser')]
    suite.addTests(test_time_parser)

    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

