import math
def get_page(total,p):
  show_page = 5  # 显示的页码数
  pageoffset = 2 # 偏移量
  start = 1  #分页条开始
  end = total #分页条结束

  if total > show_page:
    if p > pageoffset:
      start = p - pageoffset
      if total > p + pageoffset:
        end = p + pageoffset
      else:
        end = total
    else:
      start = 1
      if total > show_page:
        end = show_page
      else:
        end = total
    if p + pageoffset > total:
      start = start - (p + pageoffset - end)
  #用于模版中循环
  dic = range(start, end + 1)
  return dic


@user.route("/user_list",methods=['POST','GET'])
def user_list():
  p = g.args.get("p", '') #页数
  show_shouye_status = 0 #显示首页状态

  if p =='':
    p=1
  else:
    p=int(p)
    if p > 1:
      show_shouye_status = 1

  mdb = db_session()
  limit_start = (int(p)-1)*10#起始

  sql ="select * from page_text limit {0},10".format(limit_start)
  user_list=mdb.getMany(sql)

  sql="select count(id) as total from page_text"
  count = mdb.getOne(sql)['total'] #总记录
  total = int(math.ceil(count/10.0)) #总页数

  dic = get_page(total,p)
  datas={
    'user_list':user_list,
    'p': int(p),
    'total': total,
    'show_shouye_status': show_shouye_status,
    'dic_list': dic

  }
  return render_template("user_list.html",datas=datas)
