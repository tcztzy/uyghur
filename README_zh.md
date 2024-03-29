# 维吾尔文处理

[English](https://github.com/tcztzy/uyghur/blob/master/README.md)

## 动机

本人因课题需要，需要对维吾尔文进行自然语言处理，但维文的文本是自右向左排版的，在很多时候不利手动处理（如选中复制，虽然应避免手动处理，但仍有场景），而且与其他自左向右的文字混在一起时会出现一些问题（例如显示在在右侧的数字其实一个在句首一个在句末），且很多字母在词首词中词尾和单列时是不一样的，所以有些没有连字字体的系统需要单独定义字符。为了方便我这个小辣鸡我需要一个小工具转换老维文为拉丁维文。

## 术语

UEY
: 老维文，中国新疆官方唯一官方字母表，在公共媒体和日常生活中使用；

UKY
: 西里尔维文，在中亚尤其是哈萨克斯坦使用；

ULY
: 维吾尔语拉丁字母是在2008年推出的，只在计算机相关领域作为辅助书写系统使用，但在所有设备上扩大使用UEY键盘后，现在基本上已经废弃了。

UYY
: 新维字（也叫拼音Yeziⱪi或UPNY），这种字母也是基于拉丁文的，但现在大多数想用拉丁文打字的人都用ULY代替。

## 安装

```sh
$ pip install uyghur
```

## 用法

```python
from uyghur.conversion import uey2uly

print(uey2uly('پلام، جهان'))
```

## 测试

在 CPython 3.8/3.9/3.10 和 Pypy 3.8 测试，如需自行运行测试，执行下列命令

```shell
tox
```

## 待办

* [x] UEY2ULY
* [ ] ULY2UEY
* [ ] UEY2UKY
* [ ] UKY2UEY
* [ ] UEY2UYY
* [ ] UYY2UEY
* [ ] TEXT2SPEECH

## 参考文献

1. DB65/T 3690-2015 现行维吾尔文与拉丁维吾尔文编码字符转换规则
