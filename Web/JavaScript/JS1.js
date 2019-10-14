// 简单的替换p标签的脚本
let x = document.getElementsByTagName("p");
for (let i=0; i<x.length;i++)
{
    x[i].innerText = "大家好，我是华农的兄弟！"
}
