# search, findall匹配
import re
html1 = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> HTML程序测试... </title>
        <style type="text/css">
            .bold{font-weight: bolder}
            .italic{font-style: italic}
        </style>
        <style>
            table{
                border: 1px solid blue;
                border-collapse: collapse;
            }
            th,td{
                border: 1px solid green;
                padding: 5px ;
            }
            th{
                background: grey;
                color: white;
            }
            caption{
                padding: 5px;
            }

        </style>
    </head>
    <body>
        <h1> Hello, world!</h1>
        <img alt="童年" src="Picture/running.png" width="800px" height="1000px"/>

        <a href = "http://www.baidu.com" target = "_blank"> <br> 百度一下，你就知道。 </a>
        <p> 大家好，我是 <br> <span> 老四 </span> </p>
        <p> 大家好，我是 <br> <span> 阿峰 </span> </p>
        <pre>
            <code>
                for(var i = 0 ; i < 99 ;i++)
                {
                    document.write("我爱鱼C");
                }
            </code>
        </pre>
        <blockquote>
            <p> 定义一个变量 <var> user_input </var> 用于接收用户输入 </p>
            <p> 若用户输入为： <kbd> 苹果 </kbd> 则程序将打印：<samp> 你最喜欢吃的是：苹果  </samp> </p>
            <p> <cite> 阿雄：</cite> <q> 这么小一只石九公啊！</q>  </p>
            <p> <abbr title="赶海天王"> 阿雄：</abbr> <q> 这么小一只石九公啊！</q>  </p>
            <p> <dfn> 阿雄 </dfn> <q> 是赶海天王！</q>  </p>
        </blockquote>
        <address>
            <strong> 长按素质三连！</strong> <br>
            B站号：<a href = "https://space.bilibili.com/406309142/dynamic" target = "_blank"> 老渔民阿雄 </a> <br>
            <b>西瓜视频</b>：xigua123.com <br>
            <em> 微博号：老渔民阿雄 </em> <br>
            <i> 抖音号：1008611</i>
        </address>
        <!-- 从右往左显示 -->
        <!-- 注音 -->
        <bdo dir="rtl">
            <ruby>魑<rp> (</rp> <rt> chi </rt> <rp>) </rp> </ruby>
            <ruby>魅<rp> (</rp> <rt> mei </rt> <rp>) </rp> </ruby>
            <ruby>魍<rp> (</rp> <rt> wang </rt> <rp>) </rp> </ruby>
            <ruby>魉<rp> (</rp> <rt> liang </rt> <rp>) </rp> </ruby>
        </bdo>
        <p class="bold"> 字体变粗(调用CSS)</p>
        <p class="italic"> 字体变倾斜(调用CSS)</p>
        <p> 常用搜索引擎从 <del> https://www.baidu.com </del> 换成了 <ins> https://www.google.com/ </ins> </p>
        <p> <s> 打工是不可能打工的 </s> </p>
        <p> <u> 做生意又不会做 </u> </p>
        <p> <mark> 个个都是人才 </mark> </p>
        <p> <u> 做生意又不会做 </u> </p>
        <p> E = mc <sup> 2 </sup> </p>
        <p> Mg + ZnSo<sub>4</sub> = MgSO<sub>4</sub> </p>
        <P> <small> 本程序最终解释权归xxx所有 </small></P>
        <ul>
            <li>老四
                <ul>
                    <li>中华锦绣龙虾</li>
                    <li>石斑鱼</li>
                    <li>椰子螺</li>
                </ul>
            </li>
            <li>阿雄
                <ul>
                    <li>石九公</li>
                    <li>鲈鱼</li>
                    <li>黄瓜鱼</li>
                </ul>
            </li>
            <li>阿峰
                <ol>
                    <li>青蟹</li>
                    <li>塔螺</li>
                    <li>魔鬼鱼</li>
                </ol>
            </li>
        </ul>
        <ol>
            <li> 华农 </li>
            <li> 兄弟 </li>
            <li> 竹鼠 </li>
        </ol>
        <dl>
            <dt> 老四 </dt>
            <dd> 海南赶海人 </dd>
        </dl>
        <dl>
            <dt>abc "name"=阿雄 
            <u> 石九公 </u> 
            </dt>
            <dt>def "name"=阿峰 <u> 鲈鱼 </u> </dt>
            <dt>gij "name"=老四 <u> 黄瓜鱼 </u> </dt>
        </dl>
        <dl>
            <dt> 阿雄 </dt>
            <dd> 知名Up主 </dd>
            <dd> 福建赶海人 </dd>
        </dl>
        <table>
            <caption> 自媒体代表 </caption>
            <tr>
                <th>平台</th>
                <th>姓名</th>
                <th>名言</th>
            </tr>
            <tr>
                <td>B站</td>
                <td>华农兄弟</td>
                <td>兄弟家的xxx成熟了，我们去摘亿点回来。</td>
            </tr>
            <tr>
                <td>西瓜视频</td>
                <td>王刚</td>
                <td>战术总结，竹鼠必宽油！</td>
            </tr>
        </table>
    </body>
</html>
'''
# result1 = re.search(r'<dt>\w+.*?"name"=([\u4e00-\u9fa5]+).*?<u>.*?([\u4e00-\u9fa5]+).*?</u>', html1, re.S)
# print(result1)
# print(result1.group(1), result1.group(2))
result2 = re.findall(r'<dt>\w+.*?"name"=([\u4e00-\u9fa5]+).*?<u>.*?([\u4e00-\u9fa5]+).*?</u>', html1, re.S)
print(result2)
for res in result2:
    print(res[0], res[1])

