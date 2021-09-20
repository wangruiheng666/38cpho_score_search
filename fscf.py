import requests
import warnings
from typing import *
import tkinter
import tkinter.messagebox as msg

__all__ = ['search_score']
warnings.filterwarnings('ignore')
CONTEST_ID = 234
YEAR = 2021


def search_score(name: str) -> Tuple[str, Dict[str, Any]]:
    for i in range(1, 30):
        for j in range(1, 31):
            w = str(310000 + 100 * i + j)
            url = 'https://www.eduzhixin.com/Searchscore/search'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/85.0.4183.102 Safari/537.36 '
            }
            data = {
                'year': YEAR,
                'contest_id': CONTEST_ID,
                'user_name': name,
                'contest_no': w
            }
            req = requests.post(url, headers=headers, data=data)
            if req.json()['code'] != -1:
                return w, req.json()
    return '查不到', {}


def clicked():
    name = input_name.get()
    res = search_score(name)
    if res[1]:
        result.configure(text=f'查询结果：{res[0]}, 得分{res[1]["score"]}')
        msg.showinfo('查询结果', f'查询到{name},\n得分{res[1]["score"]}')
    else:
        result.configure(text=f'查询结果：未查到')



if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.title('38届物理竞赛复赛北京赛区分数查询')
    tk.geometry('400x100')

    please_input_name = tkinter.Label(tk, text='请输入姓名：')
    input_name = tkinter.Entry(tk, width=20)
    search = tkinter.Button(tk, text='点击查询', command=clicked)
    result = tkinter.Label(tk, text='查询结果：')

    please_input_name.grid(row=0, column=0, sticky='w')
    input_name.grid(row=0, column=1, sticky='w')
    search.grid(row=0, column=2, sticky='w')
    result.grid(row=1, column=0, sticky='w')

    tk.mainloop()
