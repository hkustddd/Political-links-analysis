# Political-links-analysis 1.0
从高管简历出发分析企业政治连接的情况
指标度量参考

> A Dual-Agency Model of Firm CSR in Response to Institutional Pressure: Evidence from Chinese Publicly Listed Firms

> Government Initiated Corporate Social Responsibility Activities: Evidence from a Poverty Alleviation Campaign in China

这个项目是基于很多在管理学研究中需要用到企业政治连接情况作为研究的变量，但这个在指标在wind， CSRMAR等数据库中不能直接获得，只能通过人工的coding，得出相应的指标。
那么我们就希望能够减少coding过程花费的时间，这个版本是最原始的版本，希望后面能更加完善，也希望有更多大神一起分享 update这个项目（盲猜大佬用ML的方法能做的更好）

我们的做法算是基于字典的文本分析，很直观，下面简单介绍一下怎么用。

## 准备
类似下面有高管简历的csv文件

![Alt text](https://github.com/hkustddd/Political-links-analysis/blob/main/2021-02-04-00022.png "csv文件")
## 过程讲解

接下来运行我们的 py 程序就好

### 1 字典
我们自己整理的一个字典dictionary.txt，匹配出的结果是 absolute
字典来源：
> CPC 新闻网 http://cpc.people.com.cn/n1/2021/0106/c64387-31991429.html

> 中国机构编制网 http://www.scopsr.gov.cn/

> 部分地方政府网站

逻辑是，匹配到这个字典里出现的词极大概率证明政治连接的存在

这时absolute=1  否则 absolute=0
同时我们关键词 匹配到的内容 放在了 absolute 的左边一列 用 “关键词：【匹配内容】” 形式给出，供人工核查


![Alt text](https://github.com/hkustddd/Political-links-analysis/blob/main/abso.png "absolute")
### 2 模糊匹配的方法

第二种匹配是模糊的匹配，由于政治连接的表现形式各种各样，我们用一些常见的关键词进行匹配
匹配成功，以为该简历有较大概率存在政治连接，当然这里一定要进行人工筛查。
结果显示为 relative=1 否则 relative=0
同样的我们在旁边的一列给出了模糊匹配的所有匹配结果，供筛查

![Alt text](https://github.com/hkustddd/Political-links-analysis/blob/main/rela.png "rela")


### 政治身份匹配（人大政协）
这个匹配的结果 准确度很高 因为只有人大代表 和政协委员 以及党代表 三种情况
结果显示为 political status= 1 或 0


![Alt text](https://github.com/hkustddd/Political-links-analysis/blob/main/poli.png "dic")

## 总结
当absolute=0  relative=0 和 status=0 时， 我们基本可以排除掉有政治连接可能性 
至于absolute 匹配 和 relative 匹配 建议人工再筛

希望后面字典更加完善或者找到更好的方法时，能够更加准确的匹配。 欢迎大家update



Author： DUAN Bright， Li JL
