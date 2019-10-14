# taobao 匹配
import re
html1 = 'g_page_config = {"pageName":"mainsrp","mods":{"shopcombotip":{"status":"hide"},"phonenav":{"status":"hide"},"debugbar":{"status":"hide"},"shopcombo":{"status":"hide"},"itemlist":{"status":"show","data":{"postFeeText":"运费","trace":"msrp_auction","auctions":[{"p4p":1,"p4pSameHeight":true,"nid":"594381462179","category":"","pid":"","title":"【3期免息 至高立省200】vivo Z5x极点全面屏高通骁龙710大电池智能\u003cspan class\u003dH\u003e手机\u003c/span\u003e官方正品\u003cspan class\u003dH\u003e手机\u003c/span\u003e新品vivoz5x限量版 z3x","raw_title":"vivoz5x官网新手机 vivo手机vivoz5pro手机","pic_url":"//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i3/31676741/O1CN010CB7I71zfQQdO3ZBq_!!0-saturn_solar.jpg","detail_url":"https://click.simba.taobao.com/cc_im?p\u003d%CA%D6%BB%FA\u0026s\u003d2141964519\u0026k\u003d633\u0026e\u003dhsCA3DTYNEnkamWYinjcgU44SChoRmipy3vWfgqFwFZB%2FkJNe%2BuN6D0sMQAFD%2BeJ9XBiKvD%2Fk7hdVUCn0SYQS7xXKiRTH1C%2BnvpIMVC1bXdxAUWKvkXqGEfGK2rNaTnYkGWAYgP8KE0T89bu9nakBNRa1ZAA6QG%2BCctjqXFJvAST34iW8%2Bink9UMgcwWeboiI8eWlgphy%2F8mZX5taEfOymp8avL2NmfbIZdBH0n8VpdRzezX177kHZQb6%2FZDFBCyFnH%2BLGASFZN9Obg%2F6WQD4wyNIASsMLnNzhZBufdzrzNI1xVxE2fXD%2BRPU84D%2F3akctwHkXZ7TcNlkJRVDSaQtPZG8XwORiftuWNPkH%2BIc1RegOPRKpZudRT7c9TUt6g3PeeYXBYS1OIf24aui5OEASvcY4loB7J5vvk0h5d1elqr0o5r2zQpQk%2Bm%2Fcn4d8Vjc43dqDMxY9N%2FFHm4bzeJQ0JbL9XLLANTsw4p3xuR0eGr9NZw%2Fh8cRaIW1DQCXAOo7HoFGT0Y9Lj2RvF8DkYn7csnDWBzujVhk%2BO7MZaZQSntRmCFj2%2FfaGUajV7vS3YIp2JQGHCJB2M7WaV%2BEXVupiH1OKYVy%2BavbMRpSEyB5qFsPjwFZ%2B%2BUEQ%3D%3D","view_price":"1298.00","view_fee":"0.00","item_loc":"广东 东莞","view_sales":"2.0万+人付款","comment_count":"","user_id":"883737303","nick":"vivo官方旗舰店","shopcard":{"levelClasses":[],"isTmall":true,"delivery":[0,1,811],"description":[0,1,1221],"service":[0,1,579],"encryptedUserId":"UOmgGMGvuvGNG"},"icon":[{"title":"掌柜热卖宝贝","dom_class":"icon-service-remai","position":"1","show_type":"0","icon_category":"baobei","outer_text":"0","html":"","icon_key":"icon-service-remai","trace":"srpservice","traceIdx":0,"innerText":"掌柜热卖宝贝","url":"//re.taobao.com/search?keyword\u003d%CA%D6%BB%FA\u0026refpid\u003d420432_1006\u0026frcatid\u003d\u0026"},{"title":"尚天猫，就购了","dom_class":"icon-service-tianmao","position":"1","show_type":"0","icon_category":"baobei","outer_text":"0","html":"","icon_key":"icon-service-tianmao","trace":"srpservice","traceIdx":1,"innerText":"天猫宝贝"}],"isHideIM":true,"isHideNick":false,"comment_url":"https://click.simba.taobao.com/cc_im?'

# result1 = re.search(r'"raw_title":"(.*?)"', html1, re.S)
# result2 = re.search(r'"view_price":"(.*?)"', html1, re.S)
# print(result1)
# print(result1.group(1))
# print(result2)
# print(result2.group(1))

content1 = '2016-12-05 12:00'
content2 = '2016-12-05 12:00'
pattern = re.compile(r'\d{2}:\d{2}')
print(pattern)
