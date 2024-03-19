在本地写一个脚本，自动化的标注英标 然后排版合适，最后倒出文件进行打印。还是利用gpt更好

## 提示词

按照我给的例子排版
```html
A special     shoutout   tonight   goes   to        @alexutopia,  one       of      the     most      awesome 

eɪ  ˈspɛʃəl    ˈʃaʊtaʊt      təˈnaɪt     ɡoʊz    tuː      @alexutopia,  wʌn      ʌv       ðə     ˈmoʊst  ˈɔsəm           

on  His posts      are    always  of      the    highest   quality   and     incredibly    thought provoking.  

ɒn  hɪz  poʊsts     ɑːr    ɔlweɪz   ʌv      ðə    ˈhaɪɪst      ˈkwɑləti   ænd    ɪnˈkrɛdəbli     θɔt       prəˈvoʊkɪŋ.

And  the    same    goes    for    our 

ənd   ðə     seɪm     ɡoʊz    fɔr    aʊr 
```

产出

转成html格式能在浏览器打开
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vertical Alignment Example</title>
<style>
  .align-top {
    vertical-align: top;
  }
</style>
</head>
<body>

<p>
<span class="align-top">A special     shoutout   tonight   goes   to        @alexutopia,  one       of      the     most      awesome </span><br>
<span class="align-top">eɪ  ˈspɛʃəl    ˈʃaʊtaʊt      təˈnaɪt     ɡoʊz    tuː      @alexutopia,  wʌn      ʌv       ðə     ˈmoʊst  ˈɔsəm            </span><br>
<span class="align-top">on  His posts      are    always  of      the    highest   quality   and     incredibly    thought provoking.  </span><br>
<span class="align-top">ɒn  hɪz  poʊsts     ɑːr    ɔlweɪz   ʌv      ðə    ˈhaɪɪst      ˈkwɑləti   ænd    ɪnˈkrɛdəbli     θɔt       prəˈvoʊkɪŋ.</span><br>
<span class="align-top">And  the    same    goes    for    our </span><br>
<span class="align-top">ənd   ðə     seɪm     ɡoʊz    fɔr    aʊr </span>
</p>

</body>
</html>
```

效果：

![](./images/tophonetics,png.png)


A special shoutout tonight goes to @alexutopia, one of the most awesome
eɪ ˈspɛʃəl ˈʃaʊtaʊt təˈnaɪt ɡoʊz tuː @alexutopia, wʌn ʌv ðə ˈmoʊst ˈɔsəm
on His posts are always of the highest quality and incredibly thought provoking.
ɒn hɪz poʊsts ɑːr ɔlweɪz ʌv ðə ˈhaɪɪst ˈkwɑləti ænd ɪnˈkrɛdəbli θɔt prəˈvoʊkɪŋ.
And the same goes for our
ənd ðə seɪm ɡoʊz fɔr aʊr

把音标改成红色，

```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formatted Text</title>
<style>
  .red {
    color: red;
  }
</style>
</head>
<body>

<p>
A special shoutout tonight goes to @alexutopia, one of the most awesome<br>
<span class="red">eɪ</span> <span class="red">ˈspɛʃəl</span> <span class="red">ˈʃaʊtaʊt</span> <span class="red">təˈnaɪt</span> <span class="red">ɡoʊz</span> <span class="red">tuː</span> @alexutopia, <span class="red">wʌn</span> <span class="red">ʌv</span> <span class="red">ðə</span> <span class="red">ˈmoʊst</span> <span class="red">ˈɔsəm</span><br>
on His posts are always of the highest quality and incredibly thought provoking.<br>
<span class="red">ɒn</span> <span class="red">hɪz</span> <span class="red">poʊsts</span> <span class="red">ɑːr</span> <span class="red">ɔlweɪz</span> <span class="red">ʌv</span> <span class="red">ðə</span> <span class="red">ˈhaɪɪst</span> <span class="red">ˈkwɑləti</span> <span class="red">ænd</span> <span class="red">ɪnˈkrɛdəbli</span> <span class="red">θɔt</span> <span class="red">prəˈvoʊkɪŋ.</span><br>
And the same goes for our<br>
<span class="red">ənd</span> <span class="red">ðə</span> <span class="red">seɪm</span> <span class="red">ɡoʊz</span> <span class="red">fɔr</span> <span class="red">aʊr</span>
</p>

</body>
</html>


```
效果：

![](./images/tophonetics.png)