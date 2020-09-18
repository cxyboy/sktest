# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/22 18:17


header = {
    "编号": "ID",
    "标题": "TITLE",
    "前置条件": "CONDITION",
    "步骤": "STEP",
    "操作": "OPERATION",
    "页面": "PAGE",
    "元素": "ELEMENT",
    "测试数据": "DATA",
    "自动化标记": "FLAG",
    "步骤执行结果": "RESULT",
    "用例预期结果": "EXPECTED",
    "执行时间": "RUNTIME",
}

keywords = {
    "打开": "OPEN",
    "OPEN": "OPEN",
    "输入": "INPUT",
    "INPUT": "INPUT",
    "点击": "CLICK",
    "CLICK": "CLICK",
    "关闭": "CLOSE",
    "CLOSE": "CLOSE",
    "清除": "CLEAR",
    "CLEAR": "CLEAR",
    "选择": "SELECT",
    "SELECT": "SELECT",
    "滚动": "SCROLL",
    "SCROLL": "SCROLL",
    "上传": "UPLOAD",
    "UPLOAD": "UPLOAD",
    "悬停": "HOVER",
    "移动到": "HOVER",
    "识别": "RECOGNITION",
}

result_col = 10

element_wait_time = 10  # 元素查找超时时间 s
page_flash_timeout = 90  # 页面刷新超时时间 s

# driver路径
# ie_executable_path = ''
# chrome_executable_path = ''
# firefox_executable_path = ''
