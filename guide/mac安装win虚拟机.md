
重要提示！

安装的时候会弹出更新的窗口，关闭该窗口，然后会弹出一个对话窗口
选择「不，使用现有」这个按钮。否则无法破解免费使用。

    ![](./images/windows.png)

为了使该应用程序正常工作，必须禁用 SIP。

说明：
>System Integrity Protection（SIP）是macOS中的一项安全功能，用于保护系统文件和目录，防止未经授权的更改。禁用 SIP 可能会使系统变得更容易受到潜在的威胁，因此在执行此操作之前，请确保您了解潜在的风险。

以下是禁用 SIP 的步骤：

1. **重启 Mac：** 重新启动您的 Mac 并立即按住 Command（⌘） + R 键，直到出现苹果标志。

2. **进入恢复模式：** 进入恢复模式后，选择“实用工具”（Utilities）> “终端”（Terminal）。

3. **在终端中输入命令：** 在终端中输入以下命令，然后按 Enter 键：
   ```
   csrutil disable
   ```

4. **重启 Mac：** 输入完命令后，重启您的 Mac，SIP 将被禁用。

请注意，禁用 SIP 可能会使您的系统处于较低的安全性状态，因此请在确保知晓潜在风险的情况下执行此操作。如果不再需要禁用 SIP，您可以在完成任务后重新启用它，方法是在恢复模式下执行 `csrutil enable` 命令。

安装指南：
  - 打开文件 "ParallelsDesktop-19.2.1-54832.dmg"。
  -  运行 "Install" 并进行标准安装。
  -  安装完成后，安装 Windows 并关闭应用程序，或者仅关闭应用程序而不安装 Windows。
  -  打开文件 "Parallels Desktop Activation Tool.dmg"。
  -  将 Parallels Desktop Activation Tool 移动到 Applications 快捷方式。
  -  打开应用程序文件夹，找到 Parallels Desktop Activation Tool 并启动它。
  -  在程序窗口中，点击 "安装补丁/Install" 按钮，安装补丁将开始，需要输入密码，请等待过程完成，在最后将出现一个带有消息 "安装补丁成功提示：如果第一次启动时出现损坏的提示，请在 '应用程序' 中使用鼠标右键选择 'Parallels Desktop.app'" 的窗口，然后点击 "OK" 按钮，安装补丁完成，将出现主窗口，点击 "退出/Exit" 按钮退出。

可能的错误：
  - 如果在第一次启动应用程序时出现应用程序损坏的消息，并且需要将其移到垃圾桶中，则转到应用程序文件夹，找到 Parallels Desktop，右键单击它，然后点击打开按钮，会出现类似的错误，但还会有一个打开按钮，点击该按钮后应用程序将始终正常打开。


阻止域名：
-  打开终端应用程序。
- 输入或复制并粘贴下面的命令，然后按 "Enter" 键并输入您的 Mac 密码。
 命令：
 ```
 sudo nano /etc/hosts
 ```
- 使用键盘上的箭头键转到列表的末尾到新的一行，然后复制并粘贴下面的所有文本：
```
127.0.0.1 download.parallels.com
127.0.0.1 download.parallels.com.cdn.cloudflare.net
127.0.0.1 update.parallels.com
127.0.0.1 update.parallels.com.cdn.cloudflare.net
127.0.0.1 desktop.parallels.com
127.0.0.1 desktop.parallels.com.cdn.cloudflare.net
127.0.0.1 www.parallels.cn
127.0.0.1 www.parallels.com
127.0.0.1 www.parallels.de
127.0.0.1 www.parallels.es
127.0.0.1 www.parallels.fr
127.0.0.1 www.parallels.nl
127.0.0.1 www.parallels.pt
127.0.0.1 www.parallels.ru
127.0.0.1 www.parallelskorea.com
127.0.0.1 reportus.parallels.com
127.0.0.1 parallels.cn
127.0.0.1 parallels.com
127.0.0.1 parallels.de
127.0.0.1 parallels.es
127.0.0.1 parallels.fr
127.0.0.1 parallels.nl
127.0.0.1 parallels.pt
127.0.0.1 parallels.ru
127.0.0.1 parallelskorea.com
127.0.0.1 pax-manager.myparallels.com
127.0.0.1 myparallels.com
127.0.0.1 my.parallels.com

```
-  然后按 "Ctrl + O" 键，然后按 "Enter" 键保存更改，关闭终端窗口，然后您可以使用 Parallels Desktop。