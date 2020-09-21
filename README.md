# sktest
基于selenium的关键字ui快速测试框架,旨在让测试不用再花费大量的时间去编写测试代码或维护代码，只需要设计好你的测试用例，自动化的执行交给我们。
1. 使用excel编写并维护用例
2. 以业实际务流程驱动测试
3. 定位每一个业务步骤的执行情况
4. 自动生成测试报告，并将用例执行情况及报告发送到指定邮箱
***
# 运行环境
- 操作系统：Windows
- python版本：3.5+
- 浏览器：兼容chrome（默认）、Firefox、ie
- 注：请确保你的driver在环境变量PATH,或者你应该指定executable_path
***
# 安装
> pip install sktest
***
# 快速使用
1. 新建一个测试项目
2. 安装sktest
3. 在项目下新建两个目录---testcase、report
4. 将测试用例的excel文件放入testcase目录下
5. 新建一个py文件，编写代码:'from sktest import run'
6. 运行这个py文件
***
## 测试用例示例
![case](http://m.qpic.cn/psc?/V54ePMDp3lDEZw32DPWK2XO6Tg3SZLRl/bqQfVz5yrrGYSXMvKr.cqbQQiYgAxkNv38AXv9gnccg2IsXqCs9QT2tlRC2PLHPBkWrD5HqJGWlkUGG.qPTpzms2NUzK*sNem3FaDRKvREg!/b&bo=wgREAwAAAAADB6M!&rf=viewer_4)
![elements](http://m.qpic.cn/psc?/V54ePMDp3lDEZw32DPWK2XO6Tg3SZLRl/bqQfVz5yrrGYSXMvKr.cqSFcGtB5ax2hODaPrUSJ3QekZao.31sONPhDVpXB1SYZEqNBd1nKQZzTW1Q*eUDVcyXz5OmzdLio0YW4gDp94OM!/b&bo=sANEAwAAAAADB9Y!&rf=viewer_4)
- 重点：
    - 编写用例的sheet 名字必须是你所指定sheet_name，如果没有配置默认是 'case'
    - 存放元素的sheet 名字必须是 'elements'
    - 用例表单页面和元素列的名字必须和元素表page和element保持一致
***
# 自定义配置信息
    或者你可以尝试自己配置一些信息，在你创建的py文件修改这些配置信息
1. 自行配置测试用例文件的路径(cfn.excel_file_path)，无需再创建testcase目录
2. 配置浏览器及driver(cfn.browser_name、cfn.executable_path)
3. 配置邮件信息(cfn.email_account、email_password、email_receiver、case_object_name)