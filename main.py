import sys
from jd_mask_spider_requests import Jd_Mask_Spider

if __name__ == '__main__':
    start_tool = Jd_Mask_Spider()
    a = "1.预约商品\n2.秒杀抢购商品 "
    print(a)
    choice_function = input('选择功能:')
    # choice_function = '2'
    if choice_function == '1':
        start_tool.login()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        start_tool.submit_seckill_order()
    else:
        print('没有此功能')
        sys.exit(1)
