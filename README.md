# 38cpho_score_search
自动查询38届物理竞赛复赛（北京赛区）成绩。

用法：

1.直接运行fscf.py，出现GUI窗口，输入姓名后等待，若查询到结果会自动弹窗提示；

2.导入fscf.py，使用search_score函数，传入姓名即可。该函数返回一个含有2个元素的元组：若未查到，则元素分别为'未查到'和空字典；若查询到，则元素分别为准考证号和服务器返回的json。

服务器返回的json：{'code': 1,'result': 1,'msg': 'success','data': [],'language': 'zh-cn','contest_id': '234','contest_no': 准考证号,'user_name': 姓名,'school': 学校,'score': 总分,'prize': '','sub_score': {'1': 1得分,'2': 2得分,'3': 3得分,'4': 4得分,'5': 5得分,'6': 6得分,'7': 7得分,'8': 8得分},'ad_content': None,'search_type': None,'ranking': '','result_files': []}
