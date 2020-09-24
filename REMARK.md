这个是项目[nickliqian/cnn_captcha]: https://github.com/nickliqian/cnn_captcha.git 将tensorflow升级到2.0后的版本。

具体的升级方法
tensorflow安装2.0以上的库之后，使用tf_upgrade_v2 --intree cnn_captcha/ --outtree cnn_captcha_v2/ --reportfile report.txt命令，重建项目文件，然后在调用tensorflow库的文件里面添加tf.compat.v1.disable_eager_execution()就可以使用tensorflow2.0版本的了。

使用时按照readme的说明操作就可以，简单来说就是：
1、在本地建好需要的文件目录。
2、配置项目配置文件。
3、收集巨量验证码样本，按照指定格式把图片中的字符填到文件名，放到指定目录。
4、执行verify_and_split_data.py验证和分配样本。
5、执行train_model.py训练出模型。
6、之后就可以使用模型来识别验证码了，例如可以用recognition_object.py识别一个单独的本地验证码。

我自己的实践是数字和大写字母的五位验证码，用3600个样本训练出来的模型虽然显示准确率到百分之九十多，但是实际识别效果并不理想，可能训练样本要上万才比较理想，但是给上万张验证码标上字符文件名真的是吐血，这是这个识别验证码方案最大的缺陷。
