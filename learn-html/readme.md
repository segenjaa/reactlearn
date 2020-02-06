##### 1、vscode快捷键

快速初始化html页面：输入英文感叹号! 回车
vscode浏览器打开插件open in browser

快速格式化：shift+alt+f



##### 2、html学习记录

p为块级元素、br实现换行
20190929 截止章节https://www.runoob.com/html/html-head.html
20191008 截止章节https://www.runoob.com/html/html-layouts.html
20191026 截止章节https://www.runoob.com/html/html-colorvalues.html
20191103 截止章节html学习完毕



html5学习记录
20191103 https://www.runoob.com/html/html5-canvas.html
20191104 html5结束，进入测试https://www.runoob.com/quiz/html5-quiz.html



常用单位px、em等



##### 3、css学习记录

###### 3.1 css

20191106 https://www.runoob.com/css/css-tutorial.html

20191106 https://www.runoob.com/css/css-background.html

20191107 https://www.runoob.com/css/css-link.html

20191207 https://www.runoob.com/css/css-outline.html

20191228 https://www.runoob.com/css/css-display-visibility.html

20200114 https://www.runoob.com/css/css-combinators.html

20200115 https://www.runoob.com/css/css-dropdowns.html

20200119 https://www.runoob.com/css/css-tooltip.html

20200123 https://www.runoob.com/css/css-mediatypes.html

20200124 https://www.runoob.com/css/css-website-layout.html

20200125 https://www.runoob.com/css/css-summary.html

20200126 https://www.runoob.com/css3/css3-text-effects.html

css考试：盒子模型、组合选择器

position定位类型：static、relative、fixed、absolute、sticky

z-index决定元素的z序展示，需要与absolute配合使用

overflow设置超过内容的处理方法，scroll出滚动条，hidden进行隐藏

float浮动，用于图像排序和布局，只能左右移动，不能上下移动

clear:left、right、both、none、inherit

div水平对齐：margin为auto，width设置50% margin:0 auto

文字水平对齐：text-align为center

垂直居中：padding:70px 0;

选择器组合模式：后代选择器（空格）、子元素选择器（大于号>）、相邻兄弟（加号+）、普通兄弟（破折号~）

opacity可以设置透明



###### 3.2 css3

20200128 https://www.runoob.com/css3/css3-2dtransforms.html

20200129 https://www.runoob.com/css3/css3-multiple-columns.html

20200131 https://www.runoob.com/css3/css3-images.html

20200203 https://www.runoob.com/css3/css3-pagination.html



text-overflow: ellipsis 支持截断长度

word-wrap:break-word 支持截断换行

@font-face可以指定自定义字体

2d变换transform：translate、rotate、scale、skew、matrix

3d变换transform：totateX、totateY

@keyframes自定义动画

-webkit-filter可以添加各种滤镜效果

使用font-size设置按钮大小

使用border-radius设置圆角按钮

使用hover设置悬停效果



###### 3.3 scss

20200204 https://www.sass.hk/guide/

可以使用变量

选择器可以进行嵌套、属性可以进行嵌套

支持@import操作

支持静默注释//



###### 3.4 less

20200204 https://less.bootcss.com/

less：leaner style sheets

less.js将less转换成css

支持变量、嵌套、运算



less在react中生效

安装less

`yarn add less less-loader --save`

暴露react的配置

`yarn eject`

配置webpack.config.js参数

```
const cssRegex = /\.(css|less)$/; //增加less
const cssModuleRegex = /\.module\.(css|less)$/;

{
    test: cssRegex,
    exclude: cssModuleRegex,
    use: getStyleLoaders({
            importLoaders: 2,// 改成2
            modules: true,//使用模块方式访问样式
            sourceMap: isEnvProduction && shouldUseSourceMap
        },
        "less-loader" //增加loader
    ),
    // Don't consider CSS imports dead code even if the
    // containing package claims to have no side effects.
    // Remove this when webpack adds a warning or an error for this.
    // See https://github.com/webpack/webpack/issues/6571
    sideEffects: true
}
```

应用less文件

`import myless from './App.less'; `



使用的地方如下

```
<div className={myless.App}>
      <header className={myless.Appheader}>
```



注意点，对应的名称命名不能包含-，例如App-header



##### 4、javascript学习记录

typescript、redux



###### JavaScript教程

https://wangdoc.com/javascript/



###### es6学习记录

《ECMAScript 6 入门教程》阮一峰

20200206 http://es6.ruanyifeng.com/#docs/destructuring



ECMA：European Computer Manufacturers Association，欧洲计算机制造商协会，评估、开发和认可电信和计算机标准。总部在日内瓦

TC39委员会 https://github.com/tc39/ecma262

let声明变量、const声明常量

es6声明变量六种方法：var、function、let、const、import、class



箭头函数

##### 5、后续技术路线
less

webpack

babel

eslint

react

antd

echart



##### 6、react项目

react-motion https://github.com/chenglou/react-motion



##### 内容总结

把最有感触的总结一下

